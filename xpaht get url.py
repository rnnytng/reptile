import requests
from lxml import etree
url="https://www.4kdesk.com/"
response=requests.get(url)
response.encoding='utf-8'
et=etree.HTML(response.text)
result=et.xpath("//div[@class='clearfix pic-auto pic-list']/a/@href")
for item in result:
    print(item)

