import requests
from lxml import etree
import xlwt
if __name__ == '__main__':
    new_workbook = xlwt.Workbook()
    worksheet = new_workbook.add_sheet('58.xls')
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://bj.58.com/ershoufang/'
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    div_list=tree.xpath('//section[@class="list"]/div')
    a=0
    for div in div_list:
        title=div.xpath('./a/div[@class="property-content"]/div/div/h3/text()')[0]
        worksheet.write(a,0,title)
        a+=1
    new_workbook.save('E:/office/Excel/58.xls')
