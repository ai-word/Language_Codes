package main

import "fmt"

//匿名接口可以作为变量类型，或者结构体成员
type Tester struct {
	s interface {
		String() string
	}
}

type User struct {
	id   int
	name string
}

func (self *User) String() string {
	return fmt.Sprintf("User %d, %s", self.id, self.name)
}

func main() {
	t := Tester{&User{1, "Tom"}}
	fmt.Println(t.s.String())
}
