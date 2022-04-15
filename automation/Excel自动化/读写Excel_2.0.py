#不能带格式
import xlsxwriter as xw
workbook=xw.Workbook('E:\\office\\Excel\\1.xlsx')
sheet0=workbook.add_worksheet('sheet0')
for i in range(0,300):
    sheet0.write(i,0,i)
workbook.close()
print('===============================================================')
#性能不稳定
import openpyxl
workbook=openpyxl.load_workbook('E:\\office\\Excel\\1.xlsx')
sheet0=workbook['sheet0']
sheet0['A1']=5464
sheet0['A2']=31531
sheet0['A3']=646
sheet0['A4']=546
sheet0['A5']=789
workbook.save('E:\\office\\Excel\\2.csv.xlsx')