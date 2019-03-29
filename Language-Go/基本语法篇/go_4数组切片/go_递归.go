package main

import "fmt"

//face在n > 1时，一直调用自身
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	// 5
	fmt.Println(fact(5))
}
