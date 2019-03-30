# -*- coding: utf-8 -*-
# __author__ = 'Carina'

import re  # 导入正则表达式
import urllib.request


def getlink(csdnurl):
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0")
    opener = urllib.request.build_opener()  # 修改表头信息
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(csdnurl)
    data = str(file.read())
    # print(data)
    # 根据需求构建好链接表达式
    pat = '(https?:// [^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    print(link)
    # 去除重复数据
    link = list(set(link))
    return link


# 要爬取的网页链接
csdnurl = "https://blog.csdn.net/BaiHuaXiu123/article/list/2"
# 获取对应网页中包含的链接地址
linklist = getlink(csdnurl)
print(linklist)
# 通过for 循环分别遍历输出获取到的链接地址到屏幕上
for link in linklist:
    print(link[0])