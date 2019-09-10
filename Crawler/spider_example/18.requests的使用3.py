from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
proxies = {
    "http": "http://127.0.0.1:25378"
}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)