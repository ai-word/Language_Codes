package main

import "fmt"

//这个intSeq函数返回另外一个匿名函数
//这个函数绑定了一个变量i
func intSeq() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}


func main() {
	nextInt := intSeq()
	fmt.Println("firstInts")
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	//新的一个闭包中绑定的变量i是不同的
	fmt.Println("newInts()")
	newInts := intSeq()
	fmt.Println(newInts())
	fmt.Println(newInts())
	fmt.Println(newInts())
}
