package main

import "fmt"

func main() {
	//要创建一个空的map
	m := make(map[string]int)

	//使用map[key] = value语法来设置键值对
	m["k1"] = 1
	m["k2"] = 2
	fmt.Println(m)

	//使用map[key]来获取一个键的值
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	//len(map)返回监制对数目
	fmt.Println("len:", len(m))
	//fmt.Println("cap:", cap(m))

	//内建的delete可以从map中移除键值对
	delete(m, "k1")
	fmt.Println(m)

	//可选第二参数，表示是否此key在map存在
	val, prs := m["k2"]
	fmt.Println("val:", val, "prs:", prs)

	//直接初始化
	n := map[string]int{"foo":1, "bar":2}
	fmt.Println("n:", n)
}
