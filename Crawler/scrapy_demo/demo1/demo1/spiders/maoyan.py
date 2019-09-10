# -*- coding: utf-8 -*-
import scrapy
from demo1.items import MovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?']

    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        # scores_div =  response.xpath('//div[@class="channel-detail channel-detail-orange"]')
        # scores = []
        # for score in scores_div:
        #     # scores.append(score.xpath('string(.)').extract()[0])
        #     scores.append(score.xpath('string(.)').extract_first())
        # for name, score in zip(names, scores):
        #     print(name, ':', score)
        scores_div = [score.xpath('string(.)').extract_first() for score in
                      response.xpath('//div[@class="channel-detail channel-detail-orange"]')]
        # for name, score in zip(names, scores_div):
        #     # print(name, ':', score)
        #     yield {"name": name, "score": score}

        item = MovieItem()
        for name, score in zip(names, scores_div):
            item['name'] = name
            item['score'] = score
            yield item
