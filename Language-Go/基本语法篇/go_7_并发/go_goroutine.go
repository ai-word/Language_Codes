package main

import (
	"fmt"
	"time"
)

func main() {
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Println(i, " Say hello world!")
		}(i)
	}

	time.Sleep(time.Second * 5)

	fmt.Println("Main goroutine over!")
}
