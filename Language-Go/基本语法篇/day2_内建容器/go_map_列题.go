package main

import (
	"fmt"
	"unicode/utf8"
)

//abcabcbb --> abc==> 3
//bbbbbbbb -->  b ==> 1

/*
	寻找某个字符串中的最长不重复的字串
	定义start = 0 maxLength = 0
	lastOccurrend记录某个字符串上一次出现的位置,
	如果上一次出现的位置在start之前,
	或者lastOccurrend不存在当前遍历的字符串
	则表示,不是重复的字串
*/

func lengthOfNonRepeatingSubstr(s string) int {
	lastOccurrend := make(map[rune]int)
	//var lastOccurrend map[byte]int
	start := 0
	maxLength := 0
	//此处将string转换为[]rune(s),为了能够识别中文字符
	for i, ch := range []rune(s) {
		//map存在,且出现的位置大于计数开始start,则start重新赋值为lastOccurrend[ch] + 1
		if lastI, ok := lastOccurrend[ch]; ok && lastI >= start {
			start = lastOccurrend[ch] + 1
		}
		//判断当前的长度是否大于maxLength
		if i-start+1 > maxLength {
			maxLength = i - start + 1
		}
		//记录字符位置信息
		lastOccurrend[ch] = i
	}
	return maxLength
}
func main() {
	fmt.Println(
		lengthOfNonRepeatingSubstr("abcabccc"),
		lengthOfNonRepeatingSubstr("bbbb"),
		lengthOfNonRepeatingSubstr(""),
		lengthOfNonRepeatingSubstr("abcdef"),
		lengthOfNonRepeatingSubstr("abcdef"),
		lengthOfNonRepeatingSubstr("这里是慕课网"), //中文有问题
	)

	s := "Yes 我爱慕课网"
	//打印字节数
	fmt.Println(len(s))
	//打印字符串
	fmt.Printf("%s\n", []byte(s))
	//十六进制显示
	fmt.Printf("%X\n", []byte(s))
	//转化为字节流
	for _, b := range []byte(s) {
		fmt.Printf("%X ", b)
	}
	fmt.Println()

	//ch is rune and i 不是连续的
	for i, ch := range s {
		fmt.Printf("(%d %X) ", i, ch)
	}
	fmt.Println()
	//获取字符个数
	fmt.Println("Rune count:",
		utf8.RuneCountInString(s), //字符数
	)
	//不断将[]byte decode为utf8 rune字符
	bytes := []byte(s)
	for len(bytes) > 0 {
		ch, size := utf8.DecodeRune(bytes)
		bytes = bytes[size:]
		fmt.Printf("%c ", ch)
	}
	fmt.Println()

	//不用关心底层细节,直接将字符转换为utf8字节流,且i连续
	for i, ch := range []rune(s) {
		fmt.Printf("(%d %c) ", i, ch)
	}
}
