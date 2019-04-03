# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import codecs
url = "1.html"
# 创建一个列表，来装我们的a标签的所有内容
alists = []
# 第一步：（以只读模式）打开文件
f = open(url, 'r', encoding='utf-8')
html_str = f.read()
f.close()
soup = BeautifulSoup(html_str, 'html.parser')
#find_all 通过这个方法寻找a标签
all_a = soup.find_all('a')
print(all_a)
with codecs.open("test.txt", "w", 'utf-8') as f:
    f.truncate()
index = 0
for item in all_a:
    obj = item.string
    if obj != None:
        index += 1
        with codecs.open("test.txt", "a",'utf-8') as f:
            print(obj)
            f.write(str(index) + " "+ obj + "" + "\n")
