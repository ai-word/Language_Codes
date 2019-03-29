package main

import "fmt"

/*
	结构体定义方法
	type Type struct{
		Value int
		left, rigth *Type
	}
	注意,如果希望其他包能够访问,则将字段首字母大写
*/
type treeNode struct {
	value       int
	left, right *treeNode
}

//定义方法 (node treeNode)为接收者
//值接收者,某人值传递
func (node treeNode) print() {
	fmt.Println(node.value)
}

//指针接收者
func (node *treeNode) print2() {
	//应该判断指针是否为nil
	if node == nil{
		return 
	}
	//打印节点本身的值
	fmt.Println(node.value)
}

//值传递
func (node treeNode) setValue(value int) {
	//设置vlaue不会影响传入值本身
	node.value = value
}

//传指针修改本身
func (node *treeNode) setValue2(value int) {
	if node == nil {
		fmt.Println("Setting value to nil" +
			" node. Ignore.")
		return
	}
	node.value = value
}

//中序遍历方法
func (node *treeNode) traverse() {
	if node == nil {
		return
	}
	//先遍历左边
	node.left.traverse()
	//再中间
	node.print()
	//h右边
	node.right.traverse()
}

//可以返回局部变量地址
/*
c++
treeNode* CreateNode(int value){
	return new treeNode{value, nullptr, nullptr}
}
*/
func createNode(value int) *treeNode {
	//工厂函数,返回局部变量地址,由于golang的gc机制,是可以的
	return &treeNode{value: value}
}

func main() {
	// 1 定义方法 var value Type
	var root treeNode
	fmt.Println(root.value)
	//不初始化所有值,或者顺序和内容不一致,初始化需要指定字段名
	root = treeNode{value: 3}
	root.left = &treeNode{}
	//初始化所有字段,且字段顺序正确
	test := treeNode{left:nil, value:1, right:nil}
	fmt.Println(test)
	root.right = &treeNode{5, nil, nil}
	//func new(Type) *Type
	root.right.left = new(treeNode)
	root.left.right = createNode(1)

	//定义slice可以不指定treeNode
	nodes := []treeNode{
		//只初始化一个字段
		{value: 3},
		//不初始化
		{},
		//全指定
		{6, nil, nil},
	}
	fmt.Println(nodes)

	//定义map key [int]  value *treeNode
	nodeMap := map[int]*treeNode{
		1: createNode(1),
		2: createNode(2),
		3: createNode(3),
	}

	for k, v := range nodeMap {
		fmt.Println(k, *v)
	}

	//拷贝很影响性能
	root.print()
	root.setValue(5)
	root.print()
	//传递地址,优化性能
	root.setValue2(5)
	root.print2()

	var rootP treeNode
	rootP.left.setValue2(100)

	root.traverse()
}
