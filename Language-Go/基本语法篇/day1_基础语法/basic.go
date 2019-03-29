package main //每个文件必须有个自己的包名,原则上同一个目录的文件包名一样

import "fmt" //导入打印的标准库

//包内全局变量,不可用 :=,注意,golang中的全局变量只是在包内元素共享
var (
	aa = 3
	ss = "kkk"
	bb = true
)
//bb := true error

//不赋初值,默认为0 ""
func variableZeroValue() {
	var a int
	var s string
	//fmt.Println(a,s)
	//%q能够打印空值
	fmt.Printf("%d %q\n", a, s)
}

//基础变量定义,使用关键字var valueName = value的方式推导
func variableInitIalValue() {
	var a, b int = 3, 4
	var s string = "abc"
	fmt.Println(a, b, s)
}

//var自动类型推导,更简单的自动类型推导
func variableTypeDeduction() {
	//同时可以定义不同类型的值
	/*
	//一行定义
	var(
		a, b, c, s = 3, 4, true, "def"
	)
	//多行定义
	var(
		a = 3 
		b = 4
		c = true
		s = "def"
	)
	*/
	var a, b, c, s = 3, 4, true, "def"
	b = 5
	//Println可变参数,并在打印结束自动换行
	fmt.Println(a, b, c, s)
}

// := 函数体内推导
func variableShorter() {
	a, b, c, s := 3, 4, true, "def"
	fmt.Println(a, b, c, s)
}

func main() {
	fmt.Println("Hello world")
	variableZeroValue()
	variableInitIalValue()
	variableTypeDeduction()
	variableTypeDeduction()
	fmt.Println(aa, ss, bb)
}
