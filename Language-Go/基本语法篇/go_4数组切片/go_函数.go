package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

//多返回值
func vals() (int, int) {
	return 3, 7
}

func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {
	res := plus(1, 2)
	fmt.Println("1 + 2=", res)

	a, b := vals();
	fmt.Println(a, b)
	//匿名参数
	_, c := vals()
	fmt.Println(c)

	sum(1, 2)
	sum(1, 2, 3)
}
