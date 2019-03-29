package main

import (
	"fmt"
)

/*
接口是一个或者多个方法的签名的集合，任何类型的方法集中，
只要拥有与之对应的全部方法，就表示它实现了该接口
无需显示的指明添加接口声明：

1 接口的命名习惯以er结尾
2 接口只有方法的声明没有实现
3 接口没有数据类型字段
4 可在接口中嵌入其他的接口
5 一个类型可以实现多个接口
class Stringer{
public:
    virtual std::string String() = 0;
};

class Printer:public Stringer{
public:
    virtual void Print(){
        std::cout << String() << std::endl;
    }
};

class User:public Printer{
public:
    User(){}
    User(int id, std::string name):m_id(id),m_name(std::move(name)){}
    std::string String() override {
        std::stringstream ss;
        ss << "User: Id" <<m_id << " Name:" << m_name;
        return ss.str();
    }

private:
    int m_id;
    std::string m_name;
};

int main(){
 	User user{1,"tom"};
	user.Print();
	return 0;
}
*/

//接口 Stringer
type Stringer interface {
	Stringer() string
}

//接口Printer包含接口Stringer
type Printer interface {
	Stringer //接口嵌入
	Print()
}

//实现接口的类型
type User struct {
	id   int
	name string
}

//User独有的函数
func (self *User) PrivateFunc() {
	self.Print()
}

//实现接口Stringer
func (self *User) Stringer() string {
	return fmt.Sprintf("User %d, %s", self.id, self.name)
}

//实现接口Printer
func (self *User) Print() {
	fmt.Println(self.Stringer())
}

//空接口，interface{}没有任何的签名方法，也就意味着任何的类型都实现了空接口，其作用类似于void* 或者object
func Print(v interface{}) {
	fmt.Printf("%T:%v\n", v, v)
}

func main() {
	var user *User = &User{id: 1, name: "tom"}
	user.PrivateFunc()
	user.Print()
	fmt.Println(user.Stringer())

	//User 实现了接口 Stringer
	//*User包含方法Stringer  *Stringer （User只包含方法Stringer)
	var stringer Stringer = &User{id: 2, name: "tim"}
	fmt.Println(stringer.Stringer())

	var t Printer = &User{id: 3, name: "cut"}
	t.Print()
	fmt.Printf("%s\n", t.Stringer())

	Print(1)
	Print("Hello world")
}
