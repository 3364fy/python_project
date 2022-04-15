import time
from multiprocessing.dummy import Pool
start_time=time.time()
def fy(str):
    print(f'正在下载:{str}')
    time.sleep(2)
    print(f'下载成功:{str}')

lst=['xiaozi','aa','bb','cc']

pool=Pool(4)
pool.map(fy,lst)

end_time=time.time()
print(end_time-start_time)