package main

import "fmt"

//默认通道是无缓冲的，这意味着只有在对应的接收<-chan,收发必须一致才行
//效率不高
func main(){
	//设置通道的缓冲大小为2
	message := make(chan string, 2)

	message <- "buffered"
	message <- "chanel"

	fmt.Println(<-message)
	fmt.Println(<-message)
	//len函数返回未读元素个数，cap（）返回缓冲区长度
	fmt.Println("len(message):", len(message), "cap(message):", cap(message))
}
