import requests
import re
url="https://www.4kdesk.com/"
response=requests.get(url)
response.encoding='utf-8'
obj=re.compile(r'<a href=(?P<urll>.*?)target="_blank" title=(?P<name>.*?)\d.*?>')
result=obj.finditer(response.text)
for item in result:
    dict=item.groupdict()
    print(dict)
