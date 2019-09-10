from scrapy.cmdline import execute

name = "maoyan"
# execute("scrapy crawl baidu".split())
execute(["scrapy", "crawl", name])
