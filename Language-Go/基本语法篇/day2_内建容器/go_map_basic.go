package main

import "fmt"

func main() {
	/*
		c++
		std::map<std::string, std::string> m{
			{"name","ccmouse"},
			{"course:","golang"},
			{"site","imooc"},
			{"quality","notbad"}
		};

		slice map function不能作为key
		struct 类型中不包含上3中类型,也可以作为key值
	*/

	/*
	1 var m map[string]string = map[string]string{
		"name":    "ccmouse",
		"course":  "golang",
		"site":    "imooc",
		"quality": "notbad",
	}
	*/
	m := map[string]string{
		"name":    "ccmouse",
		"course":  "golang",
		"site":    "imooc",
		"quality": "notbad",
	}
	fmt.Println(m)
	//2 使用map创建,对于map来说不用指定len cap
	//  因为map底层是由hash_map构成,所以预先分配内存是无效的key不允重复
	m2 := make(map[string]int)
	var m3 map[string]int
	fmt.Println(m2, m3)

	//每次出现的顺序可能不一样hashmap
	fmt.Println("Traversing map")
	/*
	//只取值
	for _, v := range m {
		fmt.Println(v)
	}
	//只取key
	for k, _ := range m {
		fmt.Println(k)
	}
	*/
	for k, v := range m {
		fmt.Println(k, v)
	}

	//如果key值不存在,则返回一个空
	fmt.Println("Getting values")
	//这种方式获取map的值,如果key不存在返回一个初始值
	/*
		c++中 map 重载了value& operator[](key index)所以,当index不存在时,将改变map本身,q增加一条key,value value为初始值
		golang中 map[key]将返回value,bool 判断bool是否为真即可得到结果,注意此处返回的值与c++不同
		在c++中map的返回值为value本身的引用,而golang中的返回值应为其value的拷贝
	*/

	courseName := m["course"]
	fmt.Println(courseName)

	if courseName, ok := m["course:"]; ok {
		fmt.Println(courseName)
	} else {
		fmt.Println("key does not exist")
	}

	//删除map中的值func delete(m map[Type]Type1, key Type)
	fmt.Println("Deleting")
	name, ok := m["name"]
	if ok {
		fmt.Println(name, ok)
		delete(m, "name")
		fmt.Println(m)
	}
}
