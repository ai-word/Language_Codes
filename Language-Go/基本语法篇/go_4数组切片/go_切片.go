package main

import "fmt"

func PrintLenCap(s []string) {
	fmt.Printf("len:%d, cap:%d value:%v\n", len(s), cap(s), s)
}
func main() {
	//不像数组，slice的类型且有它所以包含元素决定（
	//不像数组还需要元素的个数）。要创建一个非空的
	//slice，需要使用内建的方法make,这里我们创建一个
	//长度为3的string类型slice（初始化为0值）
	s := make([]string, 3)
	fmt.Println("emp:", s)

	s1 := []string{};
	fmt.Println("emp:", s1)

	var s2 []string;
	fmt.Println("emp:", s2)

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])
	PrintLenCap(s)

	//内置操作append
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)
	PrintLenCap(s)

	//slice
	l := s[2:5]
	//此处cap[l] = 4, len[l]=3，因为底层的数组还有最后一个元素
	//所以再次切片是可以 l1 := l[:4]
	PrintLenCap(l)
	l = l[0:4]
	PrintLenCap(l)

	l = s[:5]
	PrintLenCap(l)

	l = s[2:]
	PrintLenCap(l)

	//copy
	c := make([]string, len(s))
	copy(c, s)
	fmt.Print("cpy:")
	PrintLenCap(c)

	//声明并初始化
	t := []string{"g", "h ", "i"}
	PrintLenCap(t)

	//slice可以组合成多维数组，且内部slice长度可以不同
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d:", twoD)
}
