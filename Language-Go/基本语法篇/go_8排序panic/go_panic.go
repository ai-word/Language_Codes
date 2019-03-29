package main

import (
	"os"
)

//panic表示出现未知的错误

func main(){
	//func panic(v interface{})接受任何类型，使得程序种植
	panic("a problem")

	_, err := os.Create("/tmp/orbit-fengqy")
	if err != nil{
		panic(err)
	}
}
