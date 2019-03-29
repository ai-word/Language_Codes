package main

import "fmt"

func main() {
	nums := []int{2, 3, 4}
	sum := 0
	//省略参数
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	//range arr slice
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	//range map
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	//range string,第一返回值为rune的起始字节位置，第二返回值为本身字符
	for i, c := range "go" {
		fmt.Printf("%d -> %c\n", i, c)
	}
}
