# -*- coding: utf-8 -*-
import scrapy

# 正统模拟登录方法：
# 首先发送登录页面的get请求，获取到页面里的登录必须的参数，比如说zhihu的 _xsrf
# 然后和账户密码一起post到服务器，登录成功

class Renren2Spider(scrapy.Spider):
    name = "renren2"
    allowed_domains = ["renren.com"]
    start_urls = (
        "http://www.renren.com/PLogin.do",
    )

    def parse(self, response):
        #_xsrf = response.xpath("//_xsrf").extract()[0]
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {"email" : "mr_mao_hacker@163.com", "password" : "alarmchime"},#, "_xsrf" = _xsrf},
                callback = self.parse_page
            )

    def parse_page(self, response):
        print "=========1===" + response.url
        #with open("mao.html", "w") as filename:
        #    filename.write(response.body)
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    def parse_newpage(self, response):
        print "===========2====" + response.url
        with open("xiao.html", "w") as filename:
            filename.write(response.body)


