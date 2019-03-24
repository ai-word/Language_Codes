#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import MySQLdb
import json

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", port = 6379, db = 0)

    # 创建mysql数据库连接
    mysqlcli = MySQLdb.connect(host = "127.0.0.1", port = 3306, \
        user = "power", passwd = "60055969", db = "youyuan")

    offset = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("yy:items")
        item = json.loads(data)
        try:
            # 创建mysql 操作游标对象，可以执行mysql语句
            cursor = mysqlcli.cursor()

            cursor.execute("insert into beijing_18_25_mm (username, age, header_url, images_url, content, place_from, education, hobby, source_url, source, time, spidername) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [item['username'], item['age'], item['header_url'], item['images_url'], item['content'], item['place_from'], item['education'], item['hobby'], item['source_url'], item['sourec'], item['time'], item['spidername']])
            # 提交事务
            mysqlcli.commit()
            # 关闭游标
            cursor.close()
            offset += 1
            print offset
        except:
            pass

if __name__ == "__main__":
    process_item()
