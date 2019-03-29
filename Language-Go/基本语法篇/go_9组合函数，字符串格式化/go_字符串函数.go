package main

import (
	"fmt"
	"strings"
)

var p = fmt.Println

func main() {
	p("Contains: 			", strings.Contains("test", "es"))
	p("Count: 			", strings.Count("test", "t"))
	p("HasPrefix:			", strings.HasPrefix("test", "te"))
	p("HasSuffix:			", strings.HasSuffix("test,", "st"))
	p("Index:				", strings.Index("test", "e"))
	p("Join:				", strings.Join([]string{"a", "b"}, "-"))
	p("Repeat:			", strings.Repeat("a", 5))
	p("Replace:			", strings.Replace("foo", "o", "0", -1))
	p("Replace:			", strings.Replace("foo", "o", "0", 1))
	p("Split:				", strings.Split("a-b-c-d", "-"))
	p("ToLower:			", strings.ToLower("TEST"))
	p("ToUpper:			", strings.ToUpper("test"))
}
