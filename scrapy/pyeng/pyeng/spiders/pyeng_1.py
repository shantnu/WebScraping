# -*- coding: utf-8 -*-
import scrapy
from pyeng.items import PyengItem

class Pyeng1Spider(scrapy.Spider):
    name = "pyeng_1"
    allowed_domains = ["pythonforengineers.com"]
    start_urls = (
        'http://pythonforengineers.com/pythonforengineersbook/',
    )

    def parse(self, response):
        #print "\n Page title: ", response.xpath('//title').extract(), "\n"
        
        for sel in response.xpath("//p"):
            item = PyengItem()
            item['text'] =  sel.xpath('text()').extract()
            #print item['text']
            yield item        