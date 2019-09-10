# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/606/14365245.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ', '\n')
        yield {
            'title': title,
            'content': content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[3]/@href').extract_first()
        # base_url = 'https://www.81zw.us/book/606/{}'
        if next_url.find('.html') != -1:
            # base_url = base_url.format(next_url)
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

