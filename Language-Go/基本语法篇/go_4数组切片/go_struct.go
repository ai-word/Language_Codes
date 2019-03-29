package main

import (
	"fmt"
)

type Sayer interface {
	Stringer() string
}

type persion struct {
	name string
	age  int
}

func (p *persion) Stringer() string {
	return "I,m a persion!"
}

func SayHello(stringer Sayer){
	fmt.Println(stringer.Stringer())
}

func main() {
	//传见一个新的person元素
	fmt.Println(persion{"Bob", 20})

	//初始化时，指定字段
	fmt.Println(persion{name: "Alice", age: 30})

	//省略字段，将初始化为0值
	fmt.Println(persion{name: "Fred"})

	//& 生成一个结构提指针
	fmt.Println(&persion{"Ann", 50})

	//指针 和 值均使用 . 操作访问成员
	s := persion{"Sean", 50}
	fmt.Println(s.name)
	sp := &s
	fmt.Println(sp.age)

	//指针修改，影响本身
	sp.age = 51
	fmt.Println(s.age)

	var p Sayer = sp
	fmt.Println(p.Stringer())
	SayHello(p)
}
