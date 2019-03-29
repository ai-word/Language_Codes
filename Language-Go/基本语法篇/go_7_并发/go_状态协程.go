package main

import (
	"math/rand"
	"sync/atomic"
	"time"
	"fmt"
)

type readOp struct {
	key  int
	resp chan int
}

type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {
	var ops int64

	reads := make(chan *readOp, 10)
	writes := make(chan *writeOp, 10)

	go func() {
		//让单独的一个协程拥有state
		var state = make(map[int]int)
		for {
			select {
			//等待读取消息到达
			case read := <-reads:
				//回复需要读取的结果
				read.resp <- state[read.key]
				//等待写入消息到达
			case write := <-writes:
				//将需要写入的结果放入map
				state[write.key] = write.val
				//写入完成，通知其他协程
				write.resp <- true
			}
		}
	}()

	//100个读取协程
	for r := 0; r < 100; r++ {
		go func() {
			for {
				//需要读取结果，将其指针传递过去，让state拥有者填充查询结果
				read := &readOp{
					key:  rand.Intn(5),
					resp: make(chan int),
				}
				reads <- read
				//等待查询结果
				<-read.resp
				atomic.AddInt64(&ops, 1)
			}
		}()
	}

	for w := 0; w < 10; w++ {
		go func() {
			//将需要写入的变量的地址传递state拥有者
			write := &writeOp{
				key:  rand.Intn(5),
				val:  rand.Intn(100),
				resp: make(chan bool),
			}
			writes <- write
			//等待写入state操作完成
			<-write.resp
		}()
	}
	time.Sleep(time.Second)
	opsFinal := atomic.LoadInt64(&ops)
	fmt.Println("ops:", opsFinal)

}
