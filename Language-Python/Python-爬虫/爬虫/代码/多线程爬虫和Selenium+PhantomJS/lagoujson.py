#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
# json解析库，对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)
#  取出json文件里的内容，返回的格式是字符串
html =  response.read()

# 把json形式的字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)

# Python形式的列表
city_list = jsonpath.jsonpath(unicodestr, "$..name")

#for item in city_list:
#    print item

# dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
# 禁用ascii编码格式，返回的Unicode字符串，方便使用
array = json.dumps(city_list, ensure_ascii=False)
#json.dumps(city_list)
#array = json.dumps(city_list)

with open("lagoucity.json", "w") as f:
    f.write(array.encode("utf-8"))




