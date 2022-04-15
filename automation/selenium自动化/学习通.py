from selenium import webdriver
import time
import re
from lxml import etree
from selenium.webdriver import ActionChains
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import json
#Implement evasion detection
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
bro=webdriver.Edge(executable_path='msedgedriver.exe')
bro.get('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')
# 定义js代码
script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
# 执行js代码
bro.execute_script(script)
time.sleep(2)
#Label positioning
search_input=bro.find_element('id','phone')
#Tab interaction
search_input.send_keys('19831958283')
pwd=bro.find_element('id','pwd')
pwd.send_keys('FYYSJCHJ...')
#Click the search button
sut=bro.find_element('id','loginBtn')
sut.click()
#Wait for the webpage to respond, otherwise the webpage source code may not be returned
time.sleep(2)
bro.execute_script(script)

#Jump to the sub-iframe of the page and get the corresponding webpage source code
bro.switch_to.frame('frame_content')
time.sleep(2)

#Get the source information of the webpage
text = bro.page_source
tree_one = etree.HTML(text)
#find link
href = tree_one.xpath('//*[@id="course_203020391_52290183"]/div[1]/a/@href')[0]
#Jump to web page
bro.get(href)
time.sleep(2)
bro.execute_script(script)

text = bro.page_source
time.sleep(2)
task=bro.find_element('class','zy')
task.click()
time.sleep(2)