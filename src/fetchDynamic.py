# -*- coding: UTF-8 -*-

# urllib.parse.unquote(%E7%AF%AE%E7%90%83")) # url解码
# urllib.parse.quote("街头篮球") # url编码

import requests
from urllib.request import urlretrieve
import ssl
import urllib.parse
import os
import json
from bs4 import BeautifulSoup
import re
import stat
import time
from huepy import *
from urllib import parse


class fetchTouTiao(object):
    def __init__(self):
        self.storeText = ''
        self.count = 0
        self.url = r'https://www.toutiao.com/search_content/'

    def process(self, a, b, c):
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
            print(green('ok✅'))
            return
        print(blue('%.2f%%' % per))

    def writeFile(self, res, *args, **kwargs):
        if res.status_code == 200:
            script = BeautifulSoup(res.text, 'lxml').select('script')[6]
            scriptInnerText = re.findall('"{.*}"', script.prettify())[0]
            # 多次使用 json.loads 就可以了...
            imgs = json.loads(json.loads(scriptInnerText))['sub_images']
            for img in imgs:
                self.count = self.count + 1
                imgUrl = img['url']
                self.storeText += imgUrl + '\n'
                urlretrieve(
                    imgUrl,
                    os.path.join('./imgs/') + str(time.time()) + '.jpg',
                    self.process)

        path = os.path.join('./', 'index.js')
        file = open(path, 'w')
        file.write(self.storeText)

    def mainResFn(self, res, *args, **kwargs):
        content = res.json()
        if not os.path.exists(os.path.join('./imgs/')):
            print(blue('创建文件夹啊'))
            os.mkdir(os.path.join('./imgs/'))
            os.chmod(os.path.join('./imgs/'), stat.S_IRWXU)
        else:
            os.system('rm -rf ' + os.path.join('./imgs/'))
            os.mkdir(os.path.join('./imgs/'))
            os.chmod(os.path.join('./imgs/'), stat.S_IRWXU)
        print(content, '======')
        for item in content['data']:
            print(item, '===')
            tempUrl = 'https://www.toutiao.com/a'
            # tagetUrl = urllib.parse.urlparse(
            #     urllib.parse.unquote(item['open_url']))
            # targetId = json.loads(
            #     tagetUrl.query.split('&')[2].split('=')[1])['search_result_id']
            targetId = item['id']

            # 为了防止头条的 ua 检查， 也就是防反扒
            headers = {
                'scheme':
                'https',
                'user-agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
            }
            requests.get(
                tempUrl + str(targetId) + '/',
                headers=headers,
                hooks={'response': self.writeFile},
                verify=False)
        print(green('一共%s张图片' % self.count))

    def start(self, *, keyword, count=5):

        params = parse.urlencode({
            'offset': 0,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': count,
            'cur_tab': 3,
            'from': 'gallery'
        })

        requests.get(
            self.url,
            params=params,
            hooks={'response': self.mainResFn},
            verify=False)


ssl._create_default_https_context = ssl._create_unverified_context
obj = fetchTouTiao()
obj.start(keyword='火影忍者')
