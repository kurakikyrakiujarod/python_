from urllib.request import Request, urlopen

base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20"
i = 0
while True:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/75.0.3770.80 Safari/537.36"
    }
    url = base_url.format(i * 20)
    request = Request(url, headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    if info == "" or info is None:
        break
    i += 1
