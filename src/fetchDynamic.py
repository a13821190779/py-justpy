# -*- coding: UTF-8 -*-

# %E7%AF%AE%E7%90%83")) # url解码
# print(urllib.parse.quote("街头篮球")) # url编码

import requests
import sys
import ssl
import urllib.parse
import os


# 用类来写，目前获取到基本的请求信息了，需要递归获取内部详细数据
def foo(res, *args, **kwargs):
    content = res.json()
    print(content)
    path = os.path.join('./', 'index.html')
    file = open(path, 'w')

    file.write(str(content))


keyword = '街头篮球'
url = r'https://www.toutiao.com/search_content/?offset=0&format=json&keyword=' + urllib.parse.quote(keyword) + '&autoload=true&count=20&cur_tab=3&from=gallery'

ssl._create_default_https_context = ssl._create_unverified_context

payload = {
    'offset': 0,
    'format': 'json',
    'keyword': keyword,
    'autoload': 'true',
    'count': 20,
    'cur_tab': 1,
    'from': 'search_tab'
}

print(urllib.parse.quote(keyword))
requests.get(url, hooks={'response': foo}, verify=False)

