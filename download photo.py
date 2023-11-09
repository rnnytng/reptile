import requests
import re
import json
url='https://www.4kdesk.com/4kqitq/27822.html'
response=requests.get(url)
response.encoding='utf-8'
#print(response.text)
obj=re.compile(r'<div class="auto mt30 pic-main">.*?<img src=(?P<scr>.*?)alt',re.S)
result=obj.finditer(response.text) 

for item in result:
    name=item.group("scr")
desk=json.loads(name)
res=requests.get(desk)
with open("dd.jpg","wb")as fp:
    fp.write(res.content)



