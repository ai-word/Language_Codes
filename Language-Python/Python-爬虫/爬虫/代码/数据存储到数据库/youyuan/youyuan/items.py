# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class YouyuanItem(Item):
    # 用户名
    username = Field()
    # 年龄
    age = Field()
    # 头像图片的链接
    header_url = Field()
    # 相册图片的链接
    images_url = Field()
    # 内心独白
    content = Field()
    # 籍贯
    place_from = Field()
    # 学历
    education = Field()
    #　兴趣爱好
    hobby = Field()
    # 个人主页
    source_url = Field()
    # 数据来源网站
    sourec = Field()
    # utc 时间
    time = Field()
    # 爬虫名
    spidername = Field()