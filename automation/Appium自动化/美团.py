from appium import webdriver
from time import sleep
from appium.webdriver.extensions.android.nativekey import AndroidKey
#adb shell dumpsys activity recents | find "intent={"
desired_caps={
    'platformName': 'Android', # 被测手机是安卓
    'platformVersion': '10', # 手机安卓版本
    'deviceName': 'ying', # 设备名，安卓手机可以随意填写
    'appPackage': 'com.sankuai.meituan', # 启动APP Package名称
    'appActivity': 'com.meituan.android.pt.homepage.activity.MainActivity', # 启动Activity名称
    'autoAcceptAlerts':True,
    'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
    'resetKeyboard': True, # 执行完程序恢复原来输入法
    'noReset': True,       # 不要重置App
    'newCommandTimeout': 6000,
    'automationName' : 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 根据id定位搜索免费领水果，点击
driver.find_element('accessibility id',"免费领水果").click()
sleep(10)
a=driver.contexts
driver.switch_to.context(a[2])
# driver.switch_to.context(a[2.csv])
# print(driver.contexts)
print (driver.page_source)

# while True:
#   # 点击绝对坐标时的代码，测试机屏幕宽1080，高2340
#   driver.tap([(955,1954)],1000)


