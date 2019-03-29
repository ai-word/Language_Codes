package main

import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			if j, more := <-jobs; more {
				fmt.Println("received job ", j)
			} else {
				fmt.Println("received all jobs")
				//发送同步退出信号
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		//向通道发送消息
		jobs <- j
		fmt.Println("sent job ", j)
	}
	close(jobs)

	fmt.Println("sent all jobs")
	//等待子协程同步退出信号
	<-done
}
