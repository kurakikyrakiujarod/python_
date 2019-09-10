import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    sleep(randint(3, 5))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.select('.channel-detail.movie-item-title > a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrs['href'])
    return ['http://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.select('h3.name')[0].text
    types = soup.select('li.ellipsis')[0].text
    actors = soup.select('li.celebrity.actor > div.info > a')

    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }


def format_actors(actors_a):
    actor_set = set()
    for a in actors_a:
        actor_set.add(a.text.strip())
    return actor_set


def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)


if __name__ == '__main__':
    main()
