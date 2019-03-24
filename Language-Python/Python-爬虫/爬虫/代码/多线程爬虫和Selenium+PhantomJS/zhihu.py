#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time

def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)
    text = raw_input("请输入验证码：")
    # 返回用户输入的验证码
    return text

def zhihuLogin():
    # 构建一个Session对象，可以保存页面Cookie
    sess = requests.Session()

    # 请求报头
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 首先获取登录页面，找到需要POST的数据（_xsrf)，同时会记录当前网页的Cookie值
    html = sess.get("https://www.zhihu.com/#signin", headers = headers).text
    # 调用lxml解析库
    bs = BeautifulSoup(html, "lxml")

    # _xsrf 作用是防止CSRF攻击（跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任机制来做坏事
    # 跨域攻击通常通过伪装成网站信任的用户的请求(利用Cookie)，盗取用户信息、欺骗web服务器
    # 所以网站会通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户Cookie和服务器Session的一种方式

    # 找到name属性值为 _xsrf 的input标签，再取出value 的值
    _xsrf = bs.find("input", attrs={"name":"_xsrf"}).get("value")

    # 根据UNIX时间戳，匹配出验证码的URL地址
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    # 发送图片的请求，获取图片数据流，
    captcha_data = sess.get(captcha_url, headers = headers).content
    # 获取验证码里的文字，需要手动输入
    text = captcha(captcha_data)

    data = {
        "_xsrf" : _xsrf,
        "email" : "123636274@qq.com",
        "password" : "ALARMCHIME",
        "captcha" : text
    }

    # 发送登录需要的POST数据，获取登录后的Cookie(保存在sess里)
    response = sess.post("https://www.zhihu.com/login/email", data = data, headers = headers)
    #print response.text

    # 用已有登录状态的Cookie发送请求，获取目标页面源码
    response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers = headers)
    with open("my.html", "w") as f:
        f.write(response.text.encode("utf-8"))

if __name__ == "__main__":
    zhihuLogin()
