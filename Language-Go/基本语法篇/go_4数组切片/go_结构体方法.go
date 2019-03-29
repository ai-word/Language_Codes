package main

import "fmt"

type rect struct {
	width, heigth int
}

func (r *rect) area() int {
	return r.width * r.heigth
}

func (r rect) perim() int {
	return 2*r.width + 2*r.heigth
}

func main() {
	r := rect{width: 10, heigth: 5}

	//执行指针传递
	fmt.Println("area:", r.area())
	//拷贝r
	fmt.Println("perim:", r.perim())

	rp := &r
	//执行指针传递
	fmt.Println("area:", rp.area())
	//拷贝r
	fmt.Println("perim:", rp.perim())
}
