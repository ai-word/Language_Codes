package main

import "fmt"

//当使用通道作为函数参数的时候，你可以指定这个通道是不是只用来发送或者接收值，
//这个特性使得程序更加安全

func ping(pings chan<- string /*只发送*/ , msg string) {
	pings <- msg
}

func pong(pings <-chan string /*只接收*/ , pongs chan<- string /*只发送*/) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	//发送消息
	ping(pings, "passed message")
	//取出pings中的消息，并将其发送到pongs通道中
	pong(pings, pongs)
	//取出pongs中的消息
	fmt.Println(<-pongs)

	var send chan<- string = pings
	var recv <-chan string = pings

	send <- "Hello world!"
	//<- send 只发送通道，如果调用 <- chan操作将会发生编译错误
	fmt.Println(<-recv)
}
