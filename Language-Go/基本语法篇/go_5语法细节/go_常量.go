package main

import (
	"fmt"
	"math"
)

//包内全局常量
const s string = "constant"

func main() {
	fmt.Println(s)
	//数值类型常量，可以根据使用环境，自动转为需要的类型
	const n = 500000
	fmt.Println(n)

	const d = 3e20 / n
	fmt.Println(d)

	fmt.Println(int64(d))
	fmt.Println(math.Sin(n))
}
