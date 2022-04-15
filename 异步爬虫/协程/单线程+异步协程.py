import asyncio
async def request(url):
    print(f'正在请求的url是{url}')
    print(f'请求成功{url}')
    return url
c=request('www.baidu.com')
# #创建一个循环对象
# loop=asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# #task的使用
# loop=asyncio.get_event_loop()
# #基于loop创建一个task对象
# task=loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# #future的使用
# loop=asyncio.get_event_loop()
# future=asyncio.ensure_future(c)
# print(future)
# loop.run_until_complete(future)
# print(future)
def callback_func(future):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(future.result())
#绑定回调
loop=asyncio.get_event_loop()
future=asyncio.ensure_future(c)
future.add_done_callback(callback_func)
loop.run_until_complete(future)