import os

from bs4 import BeautifulSoup

htmlPath = os.path.join(os.path.abspath('.'), 'index.html')

with open(htmlPath, 'rt') as f:
    soup = BeautifulSoup(f.read(), 'lxml')
    print(soup.body)
    for ass in soup.find_all('a'):
        print(ass.get('href'))
