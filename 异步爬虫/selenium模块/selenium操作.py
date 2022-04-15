#window.navigator.webdriver
# # 定义js代码
# script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
# # 执行js代码
# driver.execute_script(script)
# time.sleep(2.csv)
from selenium import webdriver
import time
bro=webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('https://uland.taobao.com/sem/tbsearch')
page_text=bro.page_source
#标签定位
search_input=bro.find_element_by_id('J_search_key')
#标签交互
search_input.send_keys('蓝牙耳机')
#点击搜索按钮
sut=bro.find_element_by_class_name('submit')
sut.click()
#滚轮
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
#回退
bro.back()
#前进
bro.forward()
time.sleep(5)
bro.quit()