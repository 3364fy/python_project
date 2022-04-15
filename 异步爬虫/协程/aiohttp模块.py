import aiohttp
import requests
import asyncio
import time
start=time.time()
header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
urls=[
    'http://www.baidu.com',
    'http://www.sougou.com',
    'http://pic.netbian.com/'
]
async def get_page(url):
    print(f'正在请求的url是{url}')
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url,headers=header) as response:
            page_text=await response.text()
    print(f'请求成功{url}',page_text)
#多任务列表
stasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    stasks.append(task)
loop=asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
end=time.time()
print(end-start)