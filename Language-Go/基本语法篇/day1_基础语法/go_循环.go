package main

import (
	"fmt"
	"strconv"
	"os"
	"bufio"
)
//将某个十进制数转换为二进制
/*
 5: 
 	5/2=2,1 
	2/2 = 1,0 
	1/2=0,1
 10:
	10/2=5,0
	5/2=2,1
	2/2=1,0
	1/2=0,1
	1010

所以只需要每次找到/2的余数,并y逆序余数即可
*/
func convertToBin(n int) string {
	//定义初始值
	result := ""
	for ; n > 0; n /= 2 {
		lsb := n % 2
		//每次将新的余数字符串放到result头部
		result = strconv.Itoa(lsb) + result
	}
	//返回字符串
	return result
}

//省略起始条件,及递增条件
func printFile(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	//可以省略 ;
	/*for ; scanner.Scan();*/
	//当scanner.Scan()的结果不为真时m,表示文件读取完成,则循环退出
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

//死循环
func forEver() {
	//golang中去掉了c/c++的while循环
	/*
	for{

	}表示死循环

	c/c++中
	while(true){

	}
	while(1){

	}
	for(;;){

	}
	*/
	for {
		fmt.Println("abc")
	}
}

func main() {
	//golang中对编码的格式有严格的要求,如下fmt.Println如果要换行,必须严格的在每行结果加上 ','
	fmt.Println(
		convertToBin(5),  //101
		convertToBin(13), //-->1101
	)
	printFile("abc.txt")
	forEver()
}
