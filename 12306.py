#查找火车票，出发地和目的地均用字母，北京:BJP,上海SHH
import requests
import json
from selenium.webdriver.common.by import By
import prettytable as pt
from selenium import webdriver
from password import Password
#查票
startcity=input('输入出发城市')
endcity=input('输入到达城市')
date=input('出发日期')
trainurl='https://www.12306.cn/index/'
trainlogin='https://kyfw.12306.cn/otn/resources/login.html'
url=f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={startcity}&leftTicketDTO.to_station={endcity}&purpose_codes=ADULT'
head={'cookie':'_uab_collina=169969749451258070608832; JSESSIONID=F1C7596486B644348694A517AF9643B9; tk=rAFy5Yjp_Jow0d8p9iPflCus4JJTHLiE2B5dqQ1pr1r0; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=2011693322.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=786956554.50215.0000; fo=y14ysu5knmtnnnjxxRAQzA6U5fsHbRH7XHlkybdGaRqNtCyNiq4spHj3vdrfxokOvEjfI5d1pXCEG8NLS8IRuKmTHC0QM-x_j7Y7gbZs64MvYxQTZuzwgmSncQc6DrFKO-p4RgmcvnVt5BT7eXUop-8CXp0dgk4YN5_LwlU35YQDjRJwGIIvU4WGyT0; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2023-11-15; _jc_save_toDate=2023-11-11; _jc_save_wfdc_flag=dc; uKey=beb57bbf2b1ccdff95082af5078d1ced510a11606c26ed2dd68b5e77104548cd','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'}
response=requests.get(url=url,headers=head)
response.encoding='utf-8'
tb=pt.PrettyTable()
#添加表
tb.field_names=[
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等座',
    '二等座',
    '无座',
]
page=0

for item in response.json()['data']['result']:
    info_list=item.split('|')#将爬取的数据用'|'分开，进行索引
    trainnum=info_list[3]
    starttime=info_list[8]
    endtime=info_list[9]
    usetime=info_list[10]
    special=info_list[25]
    nochair=info_list[26]
    if special:
        pass
    else:
        special=info_list[32]
        first=info_list[31]
        second=info_list[30]
    dit={
        '车次':trainnum,
        '出发时间':starttime,
        '到达时间':endtime,
        '耗时':usetime,
        '特等座':special,
        '一等座':first,
        '二等座':second,
        '无座':nochair
    }
    #给表中加数据
    tb.add_row([
        page,
        trainnum,
        starttime,
        endtime,
        usetime,
        special,
        first,
        second,
        nochair,
    ])

    page+=1
print(tb)