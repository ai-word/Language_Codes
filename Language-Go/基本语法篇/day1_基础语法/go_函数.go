package main

import (
	"fmt"
	"reflect"
	"runtime"
	"math"
)

/*
	golang中函数为 一等公民
	函数{
			普通函数
			func show(){

			}
			变参数函数
			func function(args ...int){
				for i := range args{
					fmt.Println(args[i])
				}
			}
			m匿名函数
			func(a, b int) string{
				return strconver.iota(a + b)
			}
		}
	c++中{
			class function{
				public:
					虚函数
					virture void func(){}
					纯续函数
					virture void func2()=0
			}
			函数重载
			void func(int a)
			void func(double a)
			void func(int a, int b)

			函数默认参数
			void func(int a = 0)

			仿函数
			struct op{
				void operator()(int a, int b){
					return a + b;
				}
			}
			op op1;
			op1(1,2);

			limda
			[捕获列表](参数列表){
				centens...
			}

			函数对象
			std::function<void(int, int)> func = [](int a, int b){return;};
			等...........不厌其烦
		}
*/

//通过操作名,操作a b
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

//多值返回
/*
c++中
std::enable_if<sizeof(Args)... == 2>
template<typename... Args>
std::tuple<int, int> GetMessage(Args... args){
	if(sizeof(args)... == 2){
		return std::make_tuple(args);
	}else{
		return std::make_tuple(0 , 0)
	}
}
*/

//多值返回
func div(a, b int) (int, int) {
	return a / b, a % b
}

//如果在多值返回时,可以为每个返回值定义名字,以此提高接口可读性
func pro_div(a, b int) (q, r int) {
	q, r = a/b, a%b
	return a / b, a % b
}
//将函数作为函数的参数,如下,第一个参数为一个函数,其返回值要求为int 参数为 两个int,然后操作后面的两个参数 a, b int
func apply(op func(int, int) int, a, b int) int {
	//函数名反射
	p := reflect.ValueOf(op).Pointer()
	opName := runtime.FuncForPC(p).Name()
	fmt.Printf("Calling function %s with args "+
		"(%d %d)\n", opName, a, b)
	return op(a, b)
}

func pow(a, b int) int {
	return int(math.Pow(float64(a), float64(b)))
}

//可变参数
func sum(numbers ...int) int {
	s := 0
	for i := range numbers {
		s += numbers[i]
	}
	/*
	for _, v:= range numbers {
		s += v
	}
	*/
	return s
}
func main() {
	eval(1, 2, "+")
	fmt.Println(
		div(3, 2),
	)
	fmt.Println(
		pro_div(3, 3),
	)
	//定义函数
	fmt.Println(apply(pow, 10, 1))
	//匿名函数
	fmt.Println(apply(
		func(a int, b int) int {
			return int(math.Pow(float64(a), float64(b)))
		}, 3, 4,
	))
	fmt.Println(sum(1, 2, 3, 4, 5, 6))
}
