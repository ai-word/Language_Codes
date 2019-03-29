package main

import "fmt"

//数组指针,可修改传入数据本身,由此可看出,golang中数组s是一种数据类型
//当数组的长度不一样时是不能够编译通过的
/*
c 语言的方式
void printArray(int* arr, int arrLen){
	assert(arrLen>=0);
	for(int i = 0; i < arrLen; ++i){
		printf("%d,", arr[i]);
	}
}

c++方式
void printArray(std::vector<int> arr){
	for(auto& item : arr){
		std::cout << item << ",";
	}
	std::cout << std::endl;
}
*/
func printArray1(arr *[5]int){
	arr[0]=100
	for _, v := range arr {
		fmt.Println(v)
	}
}
//默认值传递;修改数组里面的值不影响传入值本身
func printArray2(arr [5]int){
	arr[0]=100
	for _, v := range arr {
		fmt.Println(v)
	}
}

func main() {
	//定义数组arr1值全为初始值0
	var arr1 [5]int
	//数组类型自动u推导
	arr2 := [3]int{1, 3, 5}
	//大小,数组的大小由后面的元素个数决定
	arr3 := [...]int{2, 4, 6, 8, 10}
	//二维数组4行5列的bool类型的二位数组
	var grid [4][5]bool
	//打印
	fmt.Println(arr1, arr2, arr3)
	fmt.Println(grid)
	//循环打印,访问二维数组的每个元素
	for i := 0; i < 4; i++ {
		for j := 0; j < 5; j++ {
			fmt.Println(grid[i][j])
		}
	}
	fmt.Println(len(grid))
	//将数组作为指针传递;函数体内修改元素有效
	printArray1(&arr3)
	printArray1(&arr1)
	//arr2的数组长度为3 与 [5]int不能搭配
	//printArray(arr2)
	fmt.Println(arr1, arr3)
}
