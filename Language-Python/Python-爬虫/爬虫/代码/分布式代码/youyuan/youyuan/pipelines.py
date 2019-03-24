# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class YouyuanPipeline(object):
    def __init__(self):
        #self.lists = []
        self.filename = open("youyuan.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content.encode("utf-8"))
        #self.lists.append(content.encode("utf-8"))
        return item

    def close_spider(self, spider):

        self.filename.close()