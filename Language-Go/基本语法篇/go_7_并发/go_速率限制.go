package main

import (
	"time"
	"fmt"
)

func main() {
	request := make(chan int, 5)

	for i := 1; i <= 5; i++ {
		request <- i
	}

	close(request)

	//利用打点器，限制每次接收数据的间隔为200ms
	limiter := time.NewTicker(time.Second)
	for req := range request {
		<-limiter.C
		fmt.Println("request", req, time.Now())
	}

	//利用通道缓冲，前三次不会延时接收
	burstyLimiter := make(chan time.Time, 3)
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	go func() {
		//程序会阻塞，因为通道已经满了
		for t := range time.Tick(time.Second) {
			burstyLimiter <- t
		}
	}()

	burstyRequest := make(chan int, 5)
	for i := 0; i < 5; i++ {
		burstyRequest <- i
	}
	close(burstyRequest)

	//后两次接收有1s的延时
	for req := range burstyRequest {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
	close(burstyLimiter)
}
