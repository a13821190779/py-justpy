import requests
import os
import re
import json
from urllib.request import urlretrieve
import time
import ssl
import stat

url = 'http://dnf.qq.com/'


def foo(res, *args, **kwargs):
    path = os.path.join('./', 'index.html')
    file = open(path, 'w')
    encoding = res.encoding

    content = ''

    temp = ''
    if res.encoding != 'utf-8':
        temp = res.text.encode(encoding).decode(
            requests.utils.get_encodings_from_content(res.text)[0])
    else:
        temp = res.text

    imgs = re.findall('<img\s*?src="(.*?)".*?>', temp)
    if not os.path.exists(os.path.join('./imgs/')):
        print('创建文件夹啊')
        os.mkdir(os.path.join('./imgs/'))
        os.chmod(os.path.join('./imgs/'), stat.S_IRWXU)
        
    
    
    print('===============')
    for img in imgs:
        if img != '':
            temp = re.findall(r'^https?\:', url)[0] + img
            content += temp + '\n'
            # 下载图片
            urlretrieve(temp, os.path.join('./imgs/') + str(time.time()) + '.jpg')
    print('===============')
    file.write(res.text)


# 这就是一个简单的爬虫了
# 为了https环境下载图片
ssl._create_default_https_context = ssl._create_unverified_context
requests.get(url, hooks = {'response': foo})

