import urllib.request
import urllib.parse
import urllib.error
import bs4
from bs4 import BeautifulSoup

url =' http://py4e-data.dr-chuck.net/comments_1547251.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    sum = sum+int(tag.contents[0])
print(sum)