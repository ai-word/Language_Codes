package main

import (
	"fmt"
	"time"
)

func worker(done chan bool){
	fmt.Println("working..........")
	time.Sleep(time.Second)
	fmt.Println("done")
	//只要往里面填充值即可，什么值无所谓
	done <- true
}

func main(){
	//获取chan
	done := make(chan bool)
	//启动协程
	go worker(done)
	//等待结果
	<- done
}
