# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class JinengPipeline(object):
    def process_item(self, item, spider):
        if item == '动作':
            print('正常的Item')
        else:
            raise DropItem
        return item
