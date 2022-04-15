from selenium import webdriver
import time
from interval import Interval
from selenium.webdriver.common.action_chains import ActionChains
#模拟鼠标操作
from  selenium.webdriver import ActionChains
#键盘按键操作
from  selenium.webdriver.common.keys import Keys
from  steting import  username,password
import json
#window.navigator.webdriver
options = webdriver.ChromeOptions()
user_ag = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
options.add_argument('user-agent=%s' % user_ag)
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
# 定义js代码
script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
def login():
    # 打开淘宝登录页面
    driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.21814703.754894437.1.5af911d9tBuTtn&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    # 执行js代码
    driver.execute_script(script)
    time.sleep(2)
    driver.find_element('name','fm-login-id').send_keys(username)
    time.sleep(2)
    driver.find_element('name','fm-login-password').send_keys(password)
    time.sleep(2)
    try:
        # 找到滑块
        slider = driver.find_element('xpath',"//span[contains(@class, 'btn_slide')]")
        # 判断滑块是否可见
        if slider.is_displayed():
            # 点击并且不松开鼠标
            ActionChains(driver).click_and_hold(on_element=slider).perform()
            # 往右边移动258个位置
            ActionChains(driver).move_by_offset(xoffset=258, yoffset=0).perform()
            # 松开鼠标
            ActionChains(driver).pause(0.5).release().perform()
    except:
        pass
    time.sleep(2)
    driver.find_element('xpath','//*[@id="login-form"]/div[4]/button').click()
    time.sleep(10)
    #获取网站cookie
    dricookie = driver.get_cookies()
    fw = open('taobbao.txt','w')
    json.dump(dricookie,fw)
    fw.close()
def settlement():
    #jump to cart
    driver.get('https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.201864-3.1.5af911d9fHAUqP')
    # 执行js代码
    driver.execute_script(script)
    time.sleep(2)
    shopping_cart=driver.page_source

    #Check the product
    check=driver.find_element('xpath','//*[@id="J_SelectAll1"]/div/label')
    check.click()
    time.sleep(2)

    #settlement
    settlement_key=driver.find_element('id','J_SmallSubmit')
    settlement_key.click()
    time.sleep(2)
def submit():
    while True:
        # 当前时间
        now_localtime = time.strftime("%H:%M:%S", time.localtime())
        # 当前时间（以时间区间的方式表示）
        now_time = Interval(now_localtime, now_localtime)

        time_interval = Interval("13:27:00", "15:00:00")

        # Submit orders
        submit = driver.find_element('xpath', '//*[@id="submitOrderPC_1"]/div[1]/a[2.csv]')
        if now_time in time_interval:
            submit.click()
            break
login()
settlement()

