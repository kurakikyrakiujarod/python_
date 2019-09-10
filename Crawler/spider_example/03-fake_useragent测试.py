from fake_useragent import FakeUserAgentError
from fake_useragent import UserAgent

try:
    ua = UserAgent()
except FakeUserAgentError:
    pass

print(ua.chrome)
print(ua.firefox)
print(ua.ie)
