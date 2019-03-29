package main

import (
	"io/ioutil"
	"fmt"
)
/*
在golang中,switch有两种用法(相比c/c++省略掉了break,golang中是满足条件自动推出switch)
	op的选项为condition 如op为 string 1,2,3
	1. switch op{
		case "condtion1":
		case "condtion2":
		case "condtion3":
		case "condtion4":
		case "condtion5":
		default:
	}
	//condtion为某个条件如 a > 100
	2. switch{
		case condtion1:
		case condtion2:
		case condtion3:
		default:
	}
*/
func eval(a, b int, op string) int {
	//条件
	var result int
	switch op {
	case "+":
		result = a + b
	case "-":
		result = a - b
	case "*":
		result = a * b
	case "/":
		result = a / b
	default:
		panic("unsupported operaor:" + op)
	}
	return result
}

func grade(score int) string {
	//跟判断
	g := ""
	switch {
	case score < 0 || score > 100:
		//panic报错,并终止程序
		panic(fmt.Sprintf(
			"Wrong socre: %d", score,
		))
	case score < 60:
		g = "F"
	case score < 80:
		g = "C"
	case score < 90:
		g = "B"
	case score <= 90:
		g = "A"
	}
	return g
}

func main() {
	fmt.Println(
		grade(0),
		grade(60),
		grade(70),
		grade(80),
		grade(90),
		grade(100),
		//grade(-3),
		eval(100, 90, "-"),
	)

	//if 后面可跟初始化语句
	const filename = "abc.txt"
	//读取文件,直接将文件filename读取完毕contents []byte
	if contents, err := ioutil.ReadFile(filename); err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("%s\n", contents)
	}
}
