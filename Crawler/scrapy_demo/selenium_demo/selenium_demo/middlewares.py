# from selenium import webdriver
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):
    # def __init__(self):
    #     self.chrome = webdriver.Chrome()

    def process_request(self, request, spider):
        url = request.url
        # chrome = webdriver.Chrome()
        # chrome.get(url)
        # self.chrome.get(url)
        # html = chrome.page_source
        # html = self.chrome.page_source
        # print(html)
        spider.chrome.get(url)
        html = spider.chrome.page_source
        return HtmlResponse(url=url, body=html, request=request, encoding='utf-8')


