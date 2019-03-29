package main

import "fmt"

func main() {
	// 这里我们创建了一个数组a用于存放5个int
	// 元素的类型和长度都是数组的一部分。数组默认是零值的
	// 对于int数组也是0
	var a [5]int
	fmt.Println("emp:", a)

	//我们可以使用array[index]=value的语法数组来设置数组
	//指定位置的值可以通过array[index]来获取值
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	//使用内置函数 len 返回数组的长度
	fmt.Println("len:", len(a))

	// 使用这一语法初始化一个数组
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	//数组存放类型是单一的，但是你可以组合这些数据
	//来构造更多的维度
	var two [2][3] int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			two[i][j] = i + j
		}
	}
	fmt.Println("2d:", two)
}
