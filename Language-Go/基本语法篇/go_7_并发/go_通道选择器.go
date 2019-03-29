package main

import (
	"time"
	"fmt"
)

//通道选择器让你可以同时等待几个通道的操作。
//Go协程和通道选择器是的程序更加灵活
func main() {
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		time.Sleep(time.Second * 1)
		c1 <- "one"
	}()

	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()
	//类型与c语言中的select轮寻方式，不断的去询问其中哪个case准备好了
	//就读取哪个通道的结果
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println(msg1)
		case msg2 := <-c2:
			fmt.Println(msg2)
		}
	}
}
