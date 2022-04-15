from selenium import webdriver
import time
import json
options = webdriver.ChromeOptions()
user_ag = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
options.add_argument('user-agent=%s' % user_ag)
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
# 打开教务系统登录页面
driver.get("http://xjw1.ncst.edu.cn/login")
# 定义js代码
script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
# 执行js代码
driver.execute_script(script)
time.sleep(1)
driver.find_element_by_id('input_username').send_keys('201914400313')
driver.find_element_by_id('input_password').send_keys('FYYSJCHJ3364@fy')
verification_code=input('请输入验证码:\n')
driver.find_element_by_id('input_checkcode').send_keys(verification_code)
driver.find_element_by_id('loginButton').click()
time.sleep(1)

driver.find_element_by_id('12580300').click()
time.sleep(1)
driver.find_element_by_id('12580302').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="myTab"]/li[2.csv]').click()
time.sleep(2)

#Assessment Catalog
for i in range(3,13):
    driver.execute_script(script)
    driver.find_element_by_xpath(f'//*[@id="codetbody"]/tr[{i}]/td[2.csv]/button').click()
    driver.execute_script(script)
    for index in range(2,20,2):
        try:
            driver.find_element_by_xpath(f'//*[@id="saveEvaluation"]/table/tbody/tr[{index}]/td/div[1]/label/span[1]').click()
        except:
            driver.find_element_by_xpath('//*[@id="saveEvaluation"]/table/tbody/tr[12]/td/div/textarea').send_keys('好')
            time.sleep(120)
            save=driver.find_element_by_xpath('//*[@id="savebutton"]')
            driver.execute_script("arguments[0].click();",save)
            time.sleep(5)


# #jump to cart
# driver.get('https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.201864-3.1.5af911d9fHAUqP')
# # 执行js代码
# driver.execute_script(script)
# time.sleep(2.csv)
# shopping_cart=driver.page_source
#
# #Check the product
# check=driver.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label')
# check.click()
# time.sleep(2.csv)
#
# #settlement
# settlement_key=driver.find_element_by_class_name('btn-area')
# settlement_key.click()
# time.sleep(2.csv)
#
# try:
#     #Submit orders
#     submit=driver.find_element_by_class_name('go-btn')
# except:
#     # jump to cart
#     driver.get('https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.201864-3.1.5af911d9fHAUqP')
#     driver.execute_script(script)
#     time.sleep(2.csv)
#     shopping_cart = driver.page_source
#
#     # Check the product
#     check = driver.find_element_by_xpath('//*[@id="J_Order_s_2928278102_1"]/div[1]/div/div/label')
#     check.click()
#     time.sleep(2.csv)
#
#     # settlement
#     settlement_key = driver.find_element_by_class_name('btn-area')
#     settlement_key.click()
#     time.sleep(2.csv)
#
#     # Submit orders
#     submit = driver.find_element_by_class_name('go-btn')
# while True:
#     # 当前时间
#     now_localtime = time.strftime("%H:%M:%S", time.localtime())
#     # 当前时间（以时间区间的方式表示）
#     now_time = Interval(now_localtime, now_localtime)
#
#
#     time_interval = Interval("13:27:00", "15:00:00")
#
#
#     if now_time in time_interval:
#         submit.click()
#         break
