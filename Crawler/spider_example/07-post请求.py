from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "http://www.sxt.cn/index/login/login.html"
form_data = {
    "user": "17703181473",
    "password": "123456"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.80 Safari/537.36"
}
f_data = urlencode(form_data)
request = Request(url, data=f_data.encode(), headers=headers)
response = urlopen(request)
print(response.read().decode())
