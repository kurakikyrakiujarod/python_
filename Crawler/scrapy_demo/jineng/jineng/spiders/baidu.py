# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']

    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        while True:
            yield scrapy.Request('http://www.baidu.com/', callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.url)
