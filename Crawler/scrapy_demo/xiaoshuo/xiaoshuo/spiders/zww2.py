# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/1215']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//dl/dd[1]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[3]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ', '\n')
        yield {
            'title': title,
            'content': content
        }
        # item = {}
        # next_url = response.xpath('//div[@class="bottem2"]/a[3]/@href').extract_first()
        # # base_url = 'https://www.81zw.us/book/606/{}'
        # if next_url.find('.html') != -1:
        #     # base_url = base_url.format(next_url)
        #     yield scrapy.Request(response.urljoin(next_url), callback=self.parse_item)
        # return item
