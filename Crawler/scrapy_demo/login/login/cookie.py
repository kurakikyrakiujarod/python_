cookie_str = 'zg_did=%7B%22did%22%3A%20%2216b283fd77d13c-0ba706d8de83cd-e353165-e1000-16b283fd77eef%22%7D;' \
               ' UM_distinctid=16b2840227f1c9-088802c8d98782-e353165-e1000-16b28402280619;' \
               ' 53revisit=1559748420594; CNZZDATA1261969808=560922699-1559745896-%7C1561526800; ' \
               'zg_c1e08f0fa5e3446d854919ffa754d07f=%7B%22sid%22%3A%201561530913291%2C%22updated%22%3A%201' \
               '561530966777%2C%22info%22%3A%201561530913302%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA' \
               '%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%AF%B8%E8%91%9Bio%5C%22%7D%22%2C%22plat' \
               'form%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%2' \
               '2%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.sxt.cn%2Findex%2Fuser.html%22%2C%22zs%22%3A%2' \
               '00%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201561530913291%7D; user=a%3A2%3A%7Bs%3A2%3A%2' \
               '2id%22%3Bi%3A29969%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2217756444528%22%3B%7D'

cookies = {}
for cookie in cookie_str.split(';'):
    key, value = cookie.split('=', 1)
    cookies[key.strip()] = value.strip()
print(cookies)