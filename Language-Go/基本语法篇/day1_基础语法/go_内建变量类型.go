package main

import (
	"math/cmplx"
	"fmt"
	"math"
)

/*
	基础类型
	bool string
	//整型
	(u)int (u)int8 (u)int16 (u)int32 (u)int64 uintptr
	//两种字节类型
	byte(1字节) rune(4字节)
	//浮点数3 + 4i
	float32 float64 complex64 complex128
 */

func euler() {
	c := cmplx.Pow(math.E, 1i*math.Pi)
	fmt.Println(cmplx.Abs(c))
}

func triangle() {
	var a, b int = 3, 4
	var c int
	c = int(math.Sqrt(float64(a*a + b*b)))
	fmt.Println(c)
}

func main() {
	euler()
	triangle()
}
