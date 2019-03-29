package main

import "fmt"

func PrintSlice(s []int) {
	//打印slice的基础信息
	fmt.Printf("%v, len=%d, cap=%d\n", s, len(s), cap(s))
}

func main() {
	// 1 可以使用var value []type = []type{...}定义
	var s0 []int = []int{1, 2, 3, 4}
	fmt.Println(s0)
	fmt.Println("==========Create slice==========")
	// 2 不赋初值的到的s1 is nil
	var s1 []int //Zero value for slice is nil
	PrintSlice(s1)
	//循环向s1中追加元素1
	for i := 0; i < 100; i++ {
		s1 = append(s1, 2*i+1)
		//cap分配内存是*2的方式分配,内存不够  就增加一倍
		PrintSlice(s1)
	}
	fmt.Println(s1)

	//2 自动类型推导定义slice
	//var s2 = []int{2,4,6,8}
	s2 := []int{2, 4, 6, 8}
	PrintSlice(s2)

	//使用make方式创建make(type, len, cap)
	// The make built-in function allocates and initializes an object of type
	// slice, map, or chan (only). Like new
	s3 := make([]int, 10)
	PrintSlice(s3)
	s4 := make([]int, 10, 32)
	PrintSlice(s4)
	fmt.Println("===========================")

	fmt.Println("Copying slice")
	//将s1的元素,拷贝到s3,拷贝长度为s3 或者s1的最小值
	//func copy(dst, src []Type) int
	copy(s3, s1)
	PrintSlice(s3)

	fmt.Println("delete elements from slice")
	//删掉s3的第三个元素
	//slice不支持+ -
	//此处,使用append s3[0:2] 再将s3的[4:]追加
	//注意此处底层cap不变 此处[]type...表示参数展开
	s3 = append(s3[:3], s3[4:]...)
	PrintSlice(s3)

	//去掉slice头,最好先判断len(slice) > 0
	fmt.Println("Popping from front")
	front := s3[0]
	s3 = s3[1:]
	fmt.Println("front=", front)
	PrintSlice(s3)

	//去掉slice尾,最好先判断len(slice) > 0
	fmt.Println("Popping from back")
	back := s3[len(s3)-1]
	fmt.Println("back=", back)
	s3 = s3[:len(s3)-1]
	PrintSlice(s3)
}
