package main

import "fmt"

//go 指针不能运算
func SwapByValue(a, b int) {
	b, a = a, b
}

//与c语言类型,但是golang中的指针不能够参与运算,如a++ a+1这些都不行
func SwapByPtr(a, b *int) {
	*b, *a = *a, *b
}

func main() {
	a, b := 3, 4
	//使用时记得&
	SwapByPtr(&a, &b)
	fmt.Println(a, b)
}
