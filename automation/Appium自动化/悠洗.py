from appium import webdriver
from time import sleep
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
from playsound import playsound
#adb shell dumpsys activity recents | find "intent={"
def music():
  playsound('吹梦到西洲.mp3')
desired_caps={
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'ying', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.zhishan.washer', # 启动APP Package名称
  'appActivity': '.ui.splash.SplashAy', # 启动Activity名称
  #'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'autoAcceptAlerts':True,
  #'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 600,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(50)

sleep(20)
# driver.tap([(968,187)],1000)
# sleep(2.csv)
# driver.tap([(980,596)],1000)
# laundry = driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup')
# laundry.click()
# code=driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2.csv]/android.widget.ImageView')
# code.click()
enter=driver.find_element('id','com.zhishan.washer:id/etCode')
machine= {'082':7, '043':6,'142':4, '160':3, '123':1,'097':5, '245':2,'0151':'一楼','0127':'一楼'}#
while True:
  for i in machine:
    try:
      enter.send_keys(f'GTYX2112210{i}')
      a=driver.find_element('id', 'com.zhishan.washer:id/bind_washer_submit')
      a.click()
      b=driver.find_element('id', 'com.zhishan.washer:id/bind_washer_submit')
      if b:
          print(f'{machine[i]}号洗衣机正在使用')
    except:
        print(f'\033[0;36m{machine[i]}号洗衣机空闲\033[m')
        music()

