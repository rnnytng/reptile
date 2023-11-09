import requests
import re
page=input("输入类别:")#小写拼音
url=f"https://www.4kdesk.com/4K{page}/"
response=requests.get(url)
response.encoding='utf-8'
obj=re.compile(r'<a href=(?P<urll>.*?)target="_blank" title=(?P<name>.*?)\d.*?>')
result=obj.finditer(response.text)
for item in result:
    dict=item.groupdict()
    print(dict)
#也可将正则中的内容换成自己想要得到的数据
