import requests

#登录后才能访问的网页
url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=238b5b6f95dffe9ba172d2043f2b8cd3&upsId=238b5b6f95dffe9ba172d2043f2b8cd3'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookies={'cookies':'_m_h5_tk=ba2cce361440f281dc9106bfced01bdb_1642222805503; _m_h5_tk_enc=ba13a9236e1c508707b0d16d2daecfbc; xlly_s=1; t=9fccf378f8ef86b11a5d629ac7bae404; enc=B%2FUcpm4EJ6Kg1ENpB60zQ%2BkRDMSkF1zv%2B9YzH2royRtvcTumyF8SFUSMOYhkYe10ijjruIs%2FzeLpcCvS4dbt%2FbiAnbsfiFBLi3j7eesboAk%3D; _tb_token_=3beb98e5e8666; thw=cn; cookie2=102c2a734a4c1aa0a552c005bfadb6b5; _samesite_flag_=true; cna=JAVXGilS/BwCAbfGNjkGn20z; sgcookie=E100CyVWTeeyE6LLeLZcTX%2FKx1v3EHC8ZUgRCowF3ycEQmPQ2VFPkmha4onCvloa7hapfaruxNYzXUsYV4erFgsVMT5jqzXwb%2BB95zetidwiffoKJ3qHxlQPWlHS0RfSyM6f; unb=2206590947290; uc3=nk2=F5RDLA0hEORJH6s%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCvUzDwY%2B1IID0qJQ%3D&id2=UUphzOfXI0TKhTo7YQ%3D%3D; csg=27b3b0ae; lgc=tb608495071; cancelledSubSites=empty; cookie17=UUphzOfXI0TKhTo7YQ%3D%3D; dnk=tb608495071; skt=5252ec4471e5e8da; existShop=MTY0MjIxNTU1Ng%3D%3D; uc4=nk4=0%40FY4I708GfoZZ4E7%2BGWrbTJyvsbQicw%3D%3D&id4=0%40U2grF8waOUTTT8uis2WIvBDPmS4upEaX; tracknick=tb608495071; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=10b; _nk_=tb608495071; cookie1=UoCAwg29qe6IC%2Bz4Qq8GyC53%2B21ZAY1Gacg%2BQ%2BBBixw%3D; mt=ci=39_1; uc1=existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&pas=0&cookie15=URm48syIIVrSKA%3D%3D&cookie14=UoewAjxA8h%2F03g%3D%3D; isg=BC0t_d2BMG4ZjtSC64zj0iSpPMmnimFc3LmNzW8zTEQz5k-YN9t7LGr00LoA5nkU; tfstk=cZQVBIGROrUVau8_vETafrpJeIgAaEKMY4R9mi9tNhLKLxKkLsYtBQYrfQRd_Vxc.; l=eBL8VRIVg5n7YOUtBO5Churza779PIObzsPzaNbMiInca1yO6FWWpNCp0iEBJdtjgtCY1etz_WZiLRUW-U4dgJdQP8huBKWT7xJO.'}
header={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
            }
#在发送get请求时带上请求头和cookies
resp = requests.get(url=url, headers = header,cookies=cookies)

print(resp.content.decode('utf-8'))
