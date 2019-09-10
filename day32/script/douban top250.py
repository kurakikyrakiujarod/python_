import re
import requests
import json


def get_page(url):
    return requests.get(url).text


def parse_html(html):
    regex = re.compile(
        r'<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>.*?'
        '<span class="rating_num".*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>.*?', re.S)

    result = regex.finditer(html)  # 返回的迭代器
    for info in result:  # 从迭代器中取值 组装成字典
        yield {
            'id': info['id'],
            'title': info['title'],
            'rating_num': info['rating_num'],
            'comment_num': info['comment_num']
        }


def show_write(info):
    for data in info:
        # print(type(data))
        # print(data)
        with open('top250_info', encoding='utf-8', mode='a+') as f:
            data = json.dumps(data, ensure_ascii=False)
            print(data)
            f.write(data + "\n")


def main():
    count = 0
    for i in range(10):
        url = "https://movie.douban.com/top250?start=%d&filter=" % count
        html = get_page(url)
        info = parse_html(html)
        show_write(info)
        count += 25


if __name__ == '__main__':
    main()