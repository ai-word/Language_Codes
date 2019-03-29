package main

import (
	"Learn/day3_面向对象/queue"
	"fmt"
)

/*	
	包的管理:
	每个目录只能有同一个包,包内的方法可以定义在包内的不同文件之中
	其他包内使用,只能使用GOPATH环境变量下面的包

	project:
			src:
				Learn:
					 TreeNode
*/

func main() {
	q := queue.Queue{1}

	q.Push(2)
	q.Push(3)

	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())
}
