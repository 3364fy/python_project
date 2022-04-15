import xlrd
import xlwt
from xlutils.copy import copy
tem_excel=xlrd.open_workbook('E:/office/Excel/fy.xls',formatting_info=True)
tem_sheet=tem_excel.sheet_by_index(0)

new_excel=copy(tem_excel)
new_sheet=new_excel.get_sheet(0)

style=xlwt.XFStyle()

font=xlwt.Font()
font.name='楷体'
font.bold=True
font.height=360#*20
style.font=font

borders=xlwt.Borders()
borders.top=xlwt.Borders.THIN
borders.bottom=xlwt.Borders.THIN
borders.right=xlwt.Borders.THIN
borders.left=xlwt.Borders.THIN
style.borders=borders

alignment=xlwt.Alignment()
alignment.horz=xlwt.Alignment.HORZ_CENTER
alignment.vert=xlwt.Alignment.VERT_CENTER
style.alignment=alignment

new_sheet.write(2,2,12,style)
new_excel.save('E:/office/Excel/fy1.xls')

