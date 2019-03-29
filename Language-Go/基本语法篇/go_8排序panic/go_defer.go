package main

import (
	"os"
	"fmt"
)

func main(){
	f := createFile("/tmp/defer.txt")
	//函数结束的时候自动关闭文件
	defer closeFile(f)
	//写入文件先执行
	writeFile(f)
}

func createFile(filename string) *os.File{
	fmt.Println("creating")
	f, err := os.Create(filename)
	if err != nil{
		panic(err)
	}
	return f
}

func writeFile(f *os.File){
	fmt.Println("Writting")
	fmt.Fprintln(f, "data")
	//此处os.File实现了os.Write()
}

func closeFile(f *os.File){
	fmt.Println("Closing")
	f.Close()
}
