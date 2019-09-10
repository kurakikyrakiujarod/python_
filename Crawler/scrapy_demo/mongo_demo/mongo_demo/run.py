from scrapy.cmdline import execute

name = 'douban'
execute(['scrapy', 'crawl', name])
