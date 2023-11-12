from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#chrome_driver_path = r'c:\py\chromedriver.exe'
driver=webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.implicitly_wait(15)
#driver.find_element('id','J-userName').send_keys('17602555256')
#driver.find_element('id','J-password').send_keys('nIsHENGrI1125')
#driver.find_element(By.XPATH,'//*[@id="J-login"]').click()
driver.find_element(By.XPATH,'//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="link_for_ticket"]').click()
#出发城市
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').click()
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').send_keys('汉中')
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').send_keys(Keys.ENTER)
#目的地
driver.find_element(By.XPATH,'//*[@id="toStationText"]').click()
driver.find_element(By.XPATH,'//*[@id="toStationText"]').send_keys('西安北')
driver.find_element(By.XPATH,'//*[@id="toStationText"]').send_keys(Keys.ENTER)
#时间
driver.find_element(By.XPATH,'//*[@id="train_date"]').click()
driver.find_element(By.XPATH,'//*[@id="train_date"]').clear()
driver.find_element(By.XPATH,'//*[@id="train_date"]').send_keys("2023-11-13")
driver.find_element(By.XPATH,'//*[@id="train_date"]').send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="query_ticket"]').click()#查询
driver.find_element(By.XPATH,'//*[@id="ticket_76000G12820F_06_07"]/td[13]/a').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="normalPassenger_0"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="submitOrder_id"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="qr_submit_id"]').click()
input('结束:按任意键退出')