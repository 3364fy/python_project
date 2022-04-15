from appium import webdriver
from time import sleep
from appium.webdriver.extensions.android.nativekey import AndroidKey
#adb shell dumpsys activity recents | find "intent={"
desired_caps={
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'ying', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.ss.android.ugc.aweme.lite', # 启动APP Package名称
  'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity', # 启动Activity名称
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
def video():
    try:
        while True:
            driver.swipe(start_x=500, start_y=1200, end_x=500, end_y=100, duration=2)
            sleep(3)
    except :
        respone = input('确定退出吗？\n')
        if respone == 'v':
            print('继续播放视频')
            video()
        else:
            print('开始看小说')
            novel()
def novel():
    try:
        while True:
            driver.swipe(start_x=500, start_y=1200, end_x=0, end_y=1200, duration=2)
            sleep(1)
    except:
        respone = input('确定退出吗？\n')
        if respone == 'v':
            print('继续播放视频')
            video()
        else:
            print('开始看小说')
            novel()
video()


