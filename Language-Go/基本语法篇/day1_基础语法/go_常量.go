package main

//调用多个标准包,或者3方包
import (
	"math"
	"fmt"
)

//常量可以作为任何类型来使用
const filename = "abc.txt"

func ConstValue() {
	//注意,如果const变量没有制定类型,那么t如果是数组类型,则其可谓任何数值类型
	const (
		a, b = 3, 4
	)
	var c int
	//注意此处(a*a + b*b)是float64类型,这就是const未指定类型的好处
	c = int(math.Sqrt(a*a + b*b))
	//c此处a又变成了float32类型
	var v float32 = a
	fmt.Println(c, v)
}

func enums() {
	/*
	一般形式的const变量的定义方法
	const (
		cpp    = 0
		java   = 1
		python = 2
		golang = 3
	)*/
	//自增枚举类型iota
	const (
		cpp    = iota // iotal枚举会根据表达式,自动依此变化 0 2 3 4 5
		_
		java
		python
		golang
	)
	//b kb mb gb tb pb
	const (
		b  = 1 << (10 * iota) // 1 << (10 * 0)
		kb					  // 1 << (10 * 1)
		mb					  // 1 << (10 * 2)
		gb					  // 1 << (10 * 3)
		tb					  // 1 << (10 * 4)
		pb					  // 1 << (10 * 5)
	)
	fmt.Println(cpp, java, python, golang)
	//1 1024 1024*1024...
	fmt.Println(b, kb, mb, gb, tb, pb)
}

func main() {
	ConstValue()
	enums()
}
