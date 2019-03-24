# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback = 'parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
# 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
# 内容
        item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
# 链接
        item['url'] = response.url

        yield item
