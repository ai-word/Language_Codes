package main

import (
	"fmt"
	"time"
)

func sync() {
	data := make(chan int)
	exit := make(chan bool)

	go func() {
		for d := range data {
			fmt.Println(d)
		}
		fmt.Println("recv over.")
		exit <- true
	}()

	data <- 1
	time.Sleep(time.Second)
	data <- 2
	time.Sleep(time.Second)
	data <- 3
	time.Sleep(time.Second)
	close(data)
	fmt.Println("send over.")

	//等待子携程退出
	<-exit
}

func async() {
	data := make(chan int, 3)
	exit := make(chan bool)

	//上面设置的data的缓冲区有3个 int，当缓冲区满了之后才会阻塞等待
	data <- 1
	data <- 2
	data <- 3
	go func() {
		for d := range data {
			fmt.Println("thread 1", d)
		}
		fmt.Println("recv over.")
		exit <- true
	}()

	go func() {
		for {
			if d, ok := <-data; ok {
				fmt.Println("thread 2", d)
			} else {
				break
			}
		}
	}()

	for i := 4; i < 1000 /*100000*/; i++{
		data <- i
	}
	close(data)
	<-exit
}

func main() {
	//同步阻塞版本
	//sync()

	async()
}
