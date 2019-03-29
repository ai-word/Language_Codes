package main

import (
	"fmt"
	"unsafe"
	"reflect"
)

type User struct {
	id   int
	name string
}

/*
	struct Iface{
		Itab* tab;
		//此处为数据域，void*指针指向的内容是不可修改的，但是如果void*指向的指针指向的内容是可以修改的
		void* data;
	}

	struct Itab{
		InterfaceType* inter;
		Type* type;
		void (*func[])(void);
	}

 */

//数据指针持有的是目标对象的只读复制品，复制完整的对象或者指针

type iface struct {
	itab, data uintptr
}

func main() {
	var u User = User{1, "Tom"}
	//此处是拷贝
	var i interface{} = u
	var j interface{} = &u
	//只修改u，不修改i
	//i.(User).id = 3 //只读拷贝，不能修改
	u.id = 2
	u.name = "Jack"

	//接口转换返回临时的对象，只有使用指针才能够修改其状态
	//修改j中数据域指针指向的对象
	j.(*User).id = 3
	j.(*User).name = "cat"

	fmt.Printf("%v\n", u)
	fmt.Printf("%v\n", i.(User))
	fmt.Printf("%v\n", j.(*User))
	fmt.Println(i, j)

	//只有tab 和 data都为nil,接口才等于nil
	var a interface{} = nil         //tab = nil data = nil
	var b interface{} = (*int)(nil) //tab包含(*int)类型信息，data=nil
	ia := *(*iface)(unsafe.Pointer(&a))
	ib := *(*iface)(unsafe.Pointer(&b))
	fmt.Println(a == nil, ia)
	fmt.Println(b == nil, ib, reflect.ValueOf(b).IsNil())
}
