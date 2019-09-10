import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome
}
login_url = "http://www.sxt.cn/index/login/login"
data = {
    "user": "17703181473",
    "password": "123456"
}
response = requests.post(login_url, headers=headers, data=data)
print(response.text)
