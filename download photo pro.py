import requests
import re
import json
page=input("输入类别:")#小写拼音
num=int(input("x:"))
if num==1:
    url1=f"https://www.4kdesk.com/4K{page}/"
else:
    url1=f"https://www.4kdesk.com/4K{page}/index_{num}.html"
response1=requests.get(url=url1)
response1.encoding='utf-8'
obj=re.compile(r'<a href=(?P<url>.*?) target="_blank" title=(?P<name>.*?)\d.*?>')#取url
result1=obj.finditer(response1.text)
for item1 in result1:
    desk1=item1.group("url")
    desker1=json.loads(desk1)
#----------------------------------------------------------------------------------
    url2=desker1
    response2=requests.get(url=url2)
    response2.encoding='utf-8'
    obj=re.compile(r'<div class="auto mt30 pic-main">.*?<img src=(?P<scr>.*?)alt',re.S)#取imgsrc
    result2=obj.finditer(response2.text) 
    for item2 in result2:
        desk2=item2.group("scr")

        desker2=json.loads(desk2)#字符串变字典
        name=desker2.split("/")[-1]#照片的src最后一个/后的内容截取，作为照片的名字
        rese_img=requests.get(desker2)
        with open(f"f:\photo/{name}","wb")as fp:
            fp.write(rese_img.content)#rese_img.content拿到文件的字节
