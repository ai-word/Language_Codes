package queue

//using NewType = []int,这点和c++中不同
//在c++中此处using NewType = []int 或者 typedef []int NewType
//且在c++别名与Type本身应该为同一种类型
//在golang中的NewType []int时不同的类型
type Queue []int
//为Queue定义指针传递接口方法

//插入元素
func (q *Queue) Push(v int) {
	if q == nil {
		return
	}
	*q = append(*q, v)
}

//pop删除元素
func (q *Queue) Pop() int {
	if q == nil {
		return -1
	}
	head := (*q)[0]
	*q = (*q)[1:]
	return head
}

//判断是否为空
func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}
