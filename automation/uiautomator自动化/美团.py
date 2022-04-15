import uiautomator2 as u2
import time
import random
# d = u2.connect()  # 有线连接，手机需要插电脑上
d = u2.connect("192.168.0.103") #通过无线连接，电脑和手机需要在同一个局域网内，并且需要先用有线的方式做过初始化


# d.app_stop("com.eg.android.AlipayGphone")

print("美团")
d.app_start("com.sankuai.meituan")
time.sleep(2) ## 休眠2s等待支付宝完全启动

print("打开美团，等待5s……")
d(text="水果").click()
time.sleep(5) ## 我手机比较卡，进入蚂蚁森林后还需要几秒钟才能完全加载完
d(text="领水滴").click()


