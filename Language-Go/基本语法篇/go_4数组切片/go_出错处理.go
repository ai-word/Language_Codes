package main

import (
	"errors"
	"fmt"
)
//错误通常是内建接口error
func f1(arg int) (int, error) {
	if arg == 42 {
		return -1, errors.New("can't work with 42")
	}
	return arg + 3, nil
}

//通过实现 Error方法来实现自定义的error
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {
		//在此处，我们使用 &argError语法来创建一个新的
		//结构提
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {
	//go一般处理方式
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 work:", r)
		}
	}
	//自定义错误使用
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 work:", r)
		}
	}

	//自定义错误，类型断言
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
