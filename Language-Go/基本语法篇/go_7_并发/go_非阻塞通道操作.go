package main

import (
	"fmt"
)

func main() {
	messages := make(chan string, 1)
	signals := make(chan bool)
	select {
	case msg := <-messages:
		fmt.Println("recived message ", msg)
	default:
		fmt.Println("no message received")
	}
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("send message ", msg)
	default:
		fmt.Println("no message send")
	}
	//messages <- "hello" err 不能在缓冲区为1的chan中未接收的情况下连续发送消息
	select {
	case msg := <-messages:
		fmt.Println("recived message ", msg)
	case sig := <-signals:
		fmt.Println("received signal ", sig)
	default:
		fmt.Println("no activity")
	}
}
