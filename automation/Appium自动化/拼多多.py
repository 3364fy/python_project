from appium import webdriver
from time import sleep
from interval import Interval
import time
import random
from appium.webdriver.extensions.android.nativekey import AndroidKey
#adb shell dumpsys activity recents | find "intent={"
desired_caps={
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'ying', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.xunmeng.pinduoduo', # 启动APP Package名称
  'appActivity': '.ui.activity.MainFrameActivity', # 启动Activity名称
  #'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'autoAcceptAlerts':True,
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(1)
def video():
    try:
        while True:
            a = random.randint(600, 800)
            b = random.randint(1200, 1300)
            c = random.randint(10, 200)
            t = random.randint(1, 3)
            driver.swipe(start_x=a, start_y=b, end_x=a, end_y=c, duration=t-1)
            sleep(t)
    except:
        respone = input('确定退出吗？\n')
        if respone == 'v':
            print('继续播放视频')
            video()
        if respone == 'a':
            print('开始看广告')
            advertise()
        else:
            print('开始看小说')
            novel()
def novel():
    try:
        while True:
            driver.swipe(start_x=800, start_y=1200, end_x=0, end_y=1200, duration=2)
            sleep(1)
    except:
        respone = input('确定退出吗？\n')
        if respone == 'v':
            print('继续播放视频')
            video()
        if respone == 'a':
            print('开始看广告')
            advertise()
        else:
            print('开始看小说')
            novel()
def advertise():
    start = time.time()
    try:
        a = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.slidingpanelayout.widget.SlidingPaneLayout/android.widget.FrameLayout[2.csv]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.kuaishou.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[7]/android.view.View[2.csv]'
        while True:
            position = driver.find_element('xpath', a)
            position.click()
            sleep(27)
            driver.find_element('id', 'com.kuaishou.nebula:id/video_countdown_end_icon').click()
            gureward = driver.find_element('id', 'com.kuaishou.nebula:id/award_video_close_dialog_abandon_button')
            if gureward:
                gureward.click()
            sleep(2)
            end=time.time()
            if end-start>=300:
                respone = input('确定退出吗？\n')
                if respone == 'v':
                    print('继续播放视频')
                    video()
                else:
                    print('开始看小说')
                    novel()
    except:
        advertise()
video()