package main

import (
	"math"
	"fmt"
)

type geometry interface {
	area() float64
	perid() float64
}

type square struct {
	width, height float64
}

type circle struct {
	radius float64
}

//要在go中实现一个接口，我们只需要实现接口中的所有方法
func (s square) area() float64 {
	return s.width * s.height
}

func (s square) perid() float64 {
	return 2 * (s.width + s.height)
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perid() float64 {
	return 2 * math.Pi * c.radius
}

//如果一个变量是接口类型，那么我们可以调用这个被命名的接口中的所有的方法
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perid())
}

func main() {
	s := square{width: 3, height: 4}
	c := circle{radius: 5}

	measure(s)
	measure(c)
}
