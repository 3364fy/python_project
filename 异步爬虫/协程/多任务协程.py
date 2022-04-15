import asyncio
import time
async def request(url):
    print(f'正在请求的url是{url}')
    #time.sleep(2.csv)
    #当在asyncio中遇到阻塞操作必须手动挂起
    await asyncio.sleep(2)
    print(f'请求成功{url}')
start=time.time()
urls=[
    'www.baidu.com',
    'www.sougou.com',
    'www.goubanjia.com'
]
#多任务列表
stasks=[]
for url in urls:
    c=request(url)
    task=asyncio.ensure_future(c)
    stasks.append(task)
loop=asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
end=time.time()
print(end-start)