package main

import (
	"time"
	"fmt"
)

func main() {
	queue := make(chan string, 2)
	done := make(chan bool)
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(time.Microsecond)
			queue <- "ping"
		}
		done <- true
	}()

	/*for i := 0; i < 2; i++ {
		select {
		case msg := <-queue:
			fmt.Println(msg)
		default:
			fmt.Println("exit")
		}
	}*/

	/*for elem := range queue {
		fmt.Println(elem)
	}*/

	for {
		if data, ok := <-queue; ok {
			fmt.Println(data)
		} else {
			fmt.Println("exit")
			break
		}
	}
	<-done

	close(queue)
	close(done)
}
