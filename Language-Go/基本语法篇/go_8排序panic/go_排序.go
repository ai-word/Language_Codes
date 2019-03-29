package main

import (
	"sort"
	"fmt"
)

//go sort 包实现了内置和用户自定义的类型排序
//功能 我们首先关注内置类型排序
func main() {
	//排序方法是正对内置类型的;这里是一个字符串的列子
	//注意排序是原地更新的，所以它会改变字符串序列并且不返回
	//一个新值
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println(strs)

	//int 排序
	ints := []int{1, 3, 2}
	sort.Ints(ints)
	fmt.Println(ints)

	//检查是否有序
	s := sort.IntsAreSorted(ints)
	fmt.Println("sorted:", s)

	s = sort.StringsAreSorted(strs)
	fmt.Println("sorted:", s)
}
