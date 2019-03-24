# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import json

class YouyuanPipeline(object):
    def process_item(self, item, spider):
        # 格林威治时间，距离中国 +8 时区
        item['time'] = datetime.utcnow()
        # 爬虫名
        item['spidername'] = spider.name
        return item
