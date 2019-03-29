package main

import (
	"fmt"
	"time"
)

func Worker(id int, jobs <-chan int, result chan<- int) {
	for j := range jobs {
		fmt.Println("worker id:", id, "processing job:", j)
		time.Sleep(time.Second)
		result <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	result := make(chan int, 100)

	//启动三个协程处理
	for w := 1; w <= 3; w++ {
		go Worker(w, jobs, result)
	}

	//向任务队列里面添加任务
	for j := 1; j <= 9; j++ {
		jobs <- j
	}
	//关闭任务通道
	close(jobs)

	//同步等待结果
	for a := 1; a <= 9; a++ {
		<-result
	}
}
