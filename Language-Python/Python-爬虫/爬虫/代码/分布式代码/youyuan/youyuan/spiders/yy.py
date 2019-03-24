# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from youyuan.items import YouyuanItem

import re

#class YySpider(CrawlSpider):
class YySpider(RedisCrawlSpider):
    name = 'yy'
    #allowed_domains = ['youyuan.com']
    #start_urls = ['http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/']
    redis_key = "yyspider:start_urls"

    # 动态域范围获取
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(YySpider, self).__init__(*args, **kwargs)

    # 第一级匹配规则：北京市18~25岁女性的每一页链接匹配规则
    page_links = LinkExtractor(allow = (r"youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p\d+/"))
    # 第二级匹配规则：每个女性个人主页的匹配规则
    profile_links = LinkExtractor(allow = (r"youyuan.com/\d+-profile/"))

    rules = (
        Rule(page_links),
        Rule(profile_links, callback = "parse_item"),
    )

    def parse_item(self, response):
        item = YouyuanItem()

        item['username'] = self.get_username(response)
        # 年龄
        item['age'] = self.get_age(response)
        # 头像图片的链接
        item['header_url'] = self.get_header_url(response)
        # 相册图片的链接
        item['images_url'] = self.get_images_url(response)
        # 内心独白
        item['content'] = self.get_content(response)
        # 籍贯
        item['place_from'] = self.get_place_from(response)
        # 学历
        item['education'] = self.get_education(response)
        # 　兴趣爱好
        item['hobby'] = self.get_hobby(response)
        # 个人主页
        item['source_url'] = response.url
        # 数据来源网站
        item['sourec'] = "youyuan"

        yield item


    def get_username(self, response):
        username = response.xpath("//dl[@class='personal_cen']//div[@class='main']/strong/text()").extract()
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()


    def get_age(self, response):
        age = response.xpath("//dl[@class='personal_cen']//dd/p/text()").extract()
        if len(age):
            age = re.findall(u"\d+岁", age[0])[0]
        else:
            age = "NULL"
        return age.strip()

    def get_header_url(self, response):
        header_url = response.xpath("//dl[@class='personal_cen']/dt/img/@src").extract()
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = "NULL"
        return header_url.strip()


    def get_images_url(self, response):
        images_url = response.xpath("//div[@class='ph_show']/ul/li/a/img/@src").extract()
        if len(images_url):
            images_url = images_url
        else:
            images_url = "NULL"
        return images_url

    def get_content(self, response):
        content = response.xpath("//div[@class='pre_data']/ul/li/p/text()").extract()
        if len(content):
            content = content[0]
        else:
            content = "NULL"
        return content.strip()

    def get_place_from(self, response):
        place_from = response.xpath("//div[@class='pre_data']/ul/li[2]//ol[1]/li[1]/span/text()").extract()
        if len(place_from):
            place_from = place_from[0]
        else:
            place_from = "NULL"
        return place_from.strip()

    def get_education(self, response):
        education = response.xpath("//div[@class='pre_data']/ul/li[3]//ol[2]/li[2]/span/text()").extract()
        if len(education):
            education = education[0]
        else:
            education = "NULL"
        return education.strip()


    def get_hobby(self, response):
        hobby = response.xpath("//dl[@class='personal_cen']//ol/li/text()").extract()
        if len(hobby):
            hobby = ",".join(hobby).replace(" ","")
        else:
            hobby = "NULL"
        return hobby.strip()