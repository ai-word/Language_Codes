package main

import (
	"time"
	"fmt"
)

func main(){
	timer := time.NewTimer(time.Second * 2)
	//等待timer 2秒
	<-timer.C
	fmt.Println("timer 1 expired")

	//新建一个 1 秒定时器
	timer2 := time.NewTimer(time.Second)
	go func() {
		//协程中等待超时
		<- timer2.C
		fmt.Println("timer 2 expired")
	}()
	//主线程退出定时
	stop2 := timer2.Stop()
	if stop2{
		fmt.Println("timer 2 stopped")
	}
}
