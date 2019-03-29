package main

import (
	"fmt"
	"time"
)

/*
	1 通道是连接打多个goroutine的管道，通道类型为他们需要传递值的类型
	2 你可以在一个Go协程中向通道发送数据，在别的协程中接收
*/

func main() {
	//使用make(chan val-type)创建新的通道
	message := make(chan string)

	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(time.Second)
			//使用chanel <- 发送一个新值到通道中
			message <- "ping"
		}
		close(message)
	}()

	var id int = 0
	for {
		//使用<-chanel语法从通道中取出一个值
		if msg, ok := <-message; ok {
			fmt.Println(id, ":", msg)
			id++
		} else {
			break
		}
	}
}
