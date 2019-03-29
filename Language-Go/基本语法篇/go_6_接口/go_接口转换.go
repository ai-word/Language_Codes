package main

import (
	"fmt"
)
//利用类型推断，可判断接口对象是否是某个具体的接口或者类型
type User struct {
	id int
	name string
}

func (self *User) String() string {
	return fmt.Sprintf("%d, %s", self.id, self.name)
}

type Stringer interface {
	String() string
}

type Printer interface {
	String() string
	Print()
}

//User独有的函数
func (self *User) PrivateFunc() {
	self.Print()
}

//实现接口Printer
func (self *User) Print() {
	fmt.Println(self.String())
}

func main() {
	var o interface{} = &User{1, "Tom"}

	if i, ok := o.(fmt.Stringer); ok {
		fmt.Println(i)
	}

	u := o.(*User)
	//u := o.(User)
	fmt.Println(u)

	switch v := o.(type) {
	case nil:
		fmt.Println("nil")
	case fmt.Stringer:
		fmt.Println(v)
	case func() string:
		fmt.Println(v)
	case *User:
		fmt.Printf("%d, %v\n", v.id, v.name)
	default:
		fmt.Println("unknown")
	}
	//超级接口可以转换为子集接口，反之出错
	var o1 Printer = &User{2, "Jack"}
	var s Stringer = o1
	fmt.Println(s.String())
}
