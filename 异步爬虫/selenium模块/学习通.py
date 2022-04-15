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
bro=webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')
# 定义js代码
script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
# 执行js代码
bro.execute_script(script)
time.sleep(2)
#Label positioning
search_input=bro.find_element('id','phone')
#Tab interaction
search_input.send_keys('17531972858')#9831958283 17772623695
pwd=bro.find_element('id','pwd')
pwd.send_keys('liu20001203')#FYYSJCHJ... Kongbaige.
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
href = tree_one.xpath('//*[@id="course_224225202_54361151"]/div[1]/a/@href')[0]

#Jump to web page
bro.get(href)
bro.execute_script(script)
time.sleep(2)

text = bro.page_source
ad=bro.find_element('xpath','/html/body/div[2]/div/div[3]/div[3]/div').click()

# chapter=bro.find_element_by_class_name('zj')
# chapter.click()
# time.sleep(3)

#Obtain schedule
text1=bro.page_source
bro.switch_to.frame('frame_content-zj')
frame=bro.page_source
ex='(?<=已完成任务点: ).*?(?=/90)'
'已完成任务点: 0/90'
#<span style="color:#00B368">0</span>
schedule=int(re.findall(ex,frame,re.S)[0])
print(schedule)


chapter1=bro.find_element('xpath','//*[@id="fanyaChapter"]/div/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div/div/div[2]')
chapter1.click()
time.sleep(2)
bro.execute_script(script)


text2 = bro.page_source
tree_two = etree.HTML(text2)
li_list=tree_two.xpath('//*[@id="coursetree"]/ul/li')
#Section 1 id
a=int(str(tree_two.xpath('//*[@id="cur551626664"]/@id')[0])[-3:])
b=tree_two.xpath('//*[@id="cur551626664"]/@id')[0][0:-3]
'print(a,b)'
for li in li_list:
    title=li.xpath('./div[2]/ul/li/div/span[1]/text()')
    #/html/body/div[5]/div[3]/div[2]/div[1]/div/ul/li[1]/div[2]/ul/li[1]/div/span[1]
    for data_name in title:
        print(data_name)
        try:
            # select chapter
            title_key = bro.find_element('id',f'{b}{a+schedule}')
            bro.execute_script("arguments[0].scrollIntoView();", title_key)  # 拖动到可见的元素去
            title_key.click()
            time.sleep(1)
        except:
            title_key = bro.find_element('id',f'{b}{a+9+schedule}')
            bro.execute_script("arguments[0].scrollIntoView();",title_key)  # 拖动到可见的元素去
            title_key.click()

        #play video
        bro.switch_to.frame(bro.find_element('xpath','//*[@id="qqqq"]/iframe'))
        bro.switch_to.frame(bro.find_element('xpath', '//*[@id="ext-gen1044"]/iframe'))
        frame2 = bro.page_source
        chapter2 = bro.find_element('xpath', '//*[@id="video"]/button')
        chapter2.click()
        while (1):
            frame2=bro.page_source
            ex2 = '(?<=<span class="vjs-duration-display" aria-live="off">).*?(?=</span>)'
            time_ = re.findall(ex2, frame2, re.S)[0]
            if time_ != '0:00':
                time_1 = (int(str(time_).split(':')[0])+1)*60
                print(time_1)
                break
        time.sleep(time_1)
        bro.switch_to.default_content()
        a+=1
bro.quit()