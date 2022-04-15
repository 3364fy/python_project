import time
import  json
from selenium import webdriver
#模拟鼠标操作
from  selenium.webdriver import ActionChains
#键盘按键操作
from  selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
driver = webdriver.Chrome(options=option)
driver.get('https://www.taobao.com')
#print(driver)
fr = open('taobbao.txt','r')
coojies = json.load(fr)
fr.close()
for cookie in coojies:
    driver.add_cookie(cookie)
time.sleep(6)
#driver.get('https://www.taobao.com')
 #刷新后，登录态还在
driver.implicitly_wait(2)
driver.refresh()
#关键字
keword = '男装'
#别的网页地址
url = 'https://s.taobao.com/search?q=' + keword
driver.get(url)
#解析网页代码
soup = BeautifulSoup(driver.page_source,'lxml')
#print(soup.text)
data  = soup.select('#mainsrp-itemlist .items .item')
for data_s in data:
    #名称
    name = data_s.find('div',class_='row row-2.csv title').a.text.strip()
    print(name)
    #价格
    price = data_s.find('div',class_='price').text
    if '¥' in price:
        price =price.replace("¥", " ")
        print(price)
    #da = data_s.select_one('div.shop >a').get_text.strip()
    #店名
    da = data_s.find('div',class_='shop').a.text.strip()
    print(da)
    #地区
    da_qu  = data_s.find('div',class_='location').text.strip()
    print(da_qu)
