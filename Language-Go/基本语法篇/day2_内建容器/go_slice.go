package main

import "fmt"

//传入slice可以直接修改底层数组的值
func updateSlice(s []int) {
	s[0] = 100
}

/*
	slice 为数组的一个视图,修改视图可以修改arr本身
	[]int视图
*/
func main() {
	//申请一个大小为8的数组
	arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}
	//切片此操作获取slice [2:6] [arr[2], arr[6])
	fmt.Println("arr[2:6]=", arr[2:6])
	fmt.Println("arr[ :6]=", arr[:6])
	s1 := arr[2:]
	fmt.Println("arr[2: ]=", arr[2:])
	s2 := arr[:]
	fmt.Println("arr[ : ]=", arr[:])

	fmt.Println("After updateSlice(s1)")
	updateSlice(s1)
	fmt.Println("After updateSlice(s2)")
	updateSlice(s2)
	fmt.Println(arr)

	//slice可以继续relisce
	fmt.Println(s2)
	fmt.Println("Relisce")
	s2 = s2[:5]
	fmt.Println(s2)
	s2 = s2[2:]
	fmt.Println(s2)

	//slice ptr(首地址) len(slice长度) cap(底层数组容量)
	//所以slice可以向后扩展,可以超越s1 不能超越底层数组的长度
	fmt.Println("Extending slice")
	//{0,1,2,3,4,5,6,7}
	arr[0], arr[2] = 0, 2
	//{2,3,4,5}
	s1 = arr[2:6]
	//{5,6},注意此处s1的底层数组为arr 而arr[5]是存在的,所以此处能够得到s1的底层的arr[5]这个元素
	s2 = s1[3:5]
	//每个slice 有 首指针 len cap组成
	fmt.Println("arr=", arr)
	fmt.Printf("s1=%v, len(s1)=%d, cap(s1)=%d\n",
		s1, len(s1), cap(s1))
	fmt.Println("s1=", s1)

	fmt.Printf("s2=%v, len(s2)=%d, cap(s2)=%d\n",
		s2, len(s2), cap(s2))
	fmt.Println("s2=", s2)

	//当slice超越arr本身的长度,系统会分配更大的底层数组
	fmt.Println("append to slice")
	//s3修改了arr的最后一个元素 []type append([]type,...)
	s3 := append(s2, 10)
	s4 := append(s3, 11)
	s5 := append(s4, 12)
	fmt.Println("s3, s4, s5=", s3, s4, s5)
	//s4 and s5 no longer view arr.
	fmt.Println("arr=", arr)
	/*
		1. 添加元素超越cap,系统分配更大的底层数组
		2. 由于值传递的关系,必须接受append的返回值
		3. s=append(s,value)
	*/

}
