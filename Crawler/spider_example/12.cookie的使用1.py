from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "http://www.sxt.cn/index/user.html"
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": "PHPSESSID=loriolh7fbt1su8h4rbtlhffm3; 17756444528=321447; "
              "UM_distinctid=16b5f46f75266c-092f60ed16b187-37c153e-e1000-16b5f46f7538c3;"
              " CNZZDATA1261969808=789503722-1560666382-http%253A%252F%252Fwww.sxt.cn%252F%7C1560666382"
}
request = Request(url, headers=headers)
response = urlopen(request)

print(response.read().decode())
