#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

"""登录用户获取文章链接"""
class csdnSpider(object):
    def __init__(self):
        # 创建session对象，可以保存Cookie值
        self.session = requests.session()
        # 处理 headers
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

        # 判重列表
        self.repeUrl = []

    # 获取登录后页面
    def getPages(self,pageNum=5):
        # 清空用于保存的文件
        self.clearFile()
        # 循环指定页面提取url
        for i in range(pageNum):
            html = self.session.get("https://blog.csdn.net/BaiHuaXiu123/article/list/"+str(i+1),headers=self.headers).text # 修改为自己的博客地址
            print(html)
            #使用bs解析页面
            formats = 'h4 a'
            values = "href"
            # 解析页面
            self.analysisHTML(html,formats,values)

    #保存获取到的url到文件中
    def downloadUrl(self,url):
        # 将url地址写入页面
        with open("download/url.txt", "a") as f:
            f.write(url+"/" + "\n")
            print("\r %s OK" % url)

    #解析页面，提取符合格式内容的数据
    def analysisHTML(self,html,formats,values):
        # 使用lxml解析页面
        bs = BeautifulSoup(html, "lxml")
        # 按照formats格式查找数据返回集合
        analysisList = bs.select(formats)
        if len(analysisList):
            for i in analysisList:
                # 下载页面文章url地址
                self.downloadUrl(i.get(values))

    #从文件中读取地址用于判重
    def clearFile(self):
        with open("download/url.txt", "w") as f:
            f.write("")
            print("\r Clear OK...")

def Main():
    # 初始化对象
    cs = csdnSpider()
    # 获取页面，并下载文章url,输入下载页面数（默认为5）
    try:
        cs.getPages(10)
    except:
        print("出错了")

if __name__ == "__main__":
    num = 0
    while True:
       # 每一个小时获取一次数据
       if num % 3600 == 0:
           Main()
       num += 1
       print("\r剩余等待时间：%d"%(3600 - num))
       time.sleep(1)