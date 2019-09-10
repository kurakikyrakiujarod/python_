from scrapy.cmdline import execute

name = "zww2"
# execute("scrapy crawl baidu".split())
execute(["scrapy", "crawl", name])
