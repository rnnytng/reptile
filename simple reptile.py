import requests
a='https://cn.bing.com/search'
#伪装成浏览器
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"}
kw=input("enter")
para={"q":kw}#利用字典爬取想要搜索关键词的网页
re=requests.get(url=a,params=para,headers=head)
page=re.text
with open("ppp","w",encoding="utf-8")as fp:
    fp.write(page)