package main

import "fmt"

type Tester interface {
	Do()
}

type FuncDo func()

func (self FuncDo) Do() {
	self()
}

func main() {
	//var _ fmt.Stringer = (*Data)(nil)
	var t Tester = FuncDo(func() { fmt.Println("Hello world!") })
	t.Do()
}
