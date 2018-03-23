# -*- coding: UTF-8 -*-
# 爬取静态网站的

import requests
import os
import re
from urllib.request import urlretrieve
from urllib.parse import urljoin
import time
import ssl
import stat
from huepy import *

url = 'http://www.fsjoy.com/main.html'


# 下载进度
def cb(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print(blue('%.2f%%' % per))


def foo(res, *args, **kwargs):
    path = os.path.join('./', 'index.html')
    file = open(path, 'w')
    encoding = res.encoding

    content = ''

    htmlContent = ''
    if res.encoding != 'utf-8':
        format = requests.utils.get_encodings_from_content(res.text)
        if format:
            htmlContent = res.text.encode(encoding).decode(
                requests.utils.get_encodings_from_content(res.text)[0])
        else:
            print(blue('未转换编码'))
    else:
        htmlContent = res.text

    imgs = re.findall('<img\s*?src="(.*?)".*?>', htmlContent)
    if not os.path.exists(os.path.join('./imgs/')):
        print(blue('创建文件夹啊'))
        os.mkdir(os.path.join('./imgs/'))
        os.chmod(os.path.join('./imgs/'), stat.S_IRWXU)
    else:
        os.system('rm -rf ' + os.path.join('./imgs/'))
        os.mkdir(os.path.join('./imgs/'))
        os.chmod(os.path.join('./imgs/'), stat.S_IRWXU)

    print(yellow('==============='))
    print(imgs)
    for img in imgs:
        if img != '':
            htmlContent = img
            if re.match('//', img):
                print(bold(green('开头为: //')))
                htmlContent = re.findall(r'^https?\:', url)[0] + img
            elif re.match('/', img):
                print(bold(green('开头为: /')))
                htmlContent = urljoin(url, img)
            elif re.match(r'^https?\:', img):
                pass

            print(bold(green(htmlContent)))
            content += htmlContent + '\n'

            urlretrieve(htmlContent,
                        os.path.join('./imgs/') + str(time.time()) + '.jpg',
                        cb)
    print(yellow('==============='))

    os.system('cd ./imgs && ls -l | grep "^-" | wc -l')
    file.write(content)


# 这就是一个简单的爬虫了
# 为了https环境下载图片
ssl._create_default_https_context = ssl._create_unverified_context

requests.get(url, hooks={'response': foo})
