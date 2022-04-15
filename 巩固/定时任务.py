import time
from interval import Interval

while True:
    # 当前时间
    now_localtime = time.strftime("%H:%M:%S", time.localtime())
    # 当前时间（以时间区间的方式表示）
    now_time = Interval(now_localtime, now_localtime)


    time_interval = Interval("12:00:00", "15:50:00")


    if now_time in time_interval:
        print("是在这个时间区间内")
        print("要执行的代码部分")
        break