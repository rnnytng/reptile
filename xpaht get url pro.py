import requests
from lxml import etree
page=input("输入类别:")
url=f"https://www.4kdesk.com/4K{page}/"
response=requests.get(url)
response.encoding='utf-8'
et=etree.HTML(response.text)
result=et.xpath("//div[@class='mt15 clearfix pic-auto pic-list']/a/@href")
#类别的网页源码比首页源码同位置多mt15
for item in result:
    print(item)

