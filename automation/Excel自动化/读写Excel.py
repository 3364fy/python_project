import xlwt
import xlrd
new_workbook=xlwt.Workbook()
worksheet=new_workbook.add_sheet('new_test')
worksheet.write(0,0,'test')
new_workbook.save('E:/office/Excel/test.xls')
print('===============================================================')
xlsx=xlrd.open_workbook('E:/office/Excel/test.xls')
table=xlsx.sheet_by_index(0)
#table=xlsx.sheet_by_name('test')
print(table.cell_value(0,0))
print(table.cell(0,0).value)
print(table.row(0)[0].value)
