# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from pyeng.items import PyengItem


class Pyeng2Spider(CrawlSpider):
    name = 'pyeng_3'
    allowed_domains = ['pythonforengineers.com']
    start_urls = ['http://pythonforengineers.com/build-a-reddit-bot-part-1/']

    rules = (
        Rule(LinkExtractor(allow="build-a-reddit"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        code= response.xpath("//pre/text()").extract()
        with  open("code.txt", "a") as f:
            f.write("".join(code))