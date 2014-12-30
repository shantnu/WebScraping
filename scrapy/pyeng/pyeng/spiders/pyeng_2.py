# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from pyeng.items import PyengItem


class Pyeng2Spider(CrawlSpider):
    name = 'pyeng_2'
    allowed_domains = ['pythonforengineers.com']
    start_urls = ['http://pythonforengineers.com/build-a-reddit-bot-part-1/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print "Title: ", response.xpath('//title').extract(), " ", response.request.url, "  \n"