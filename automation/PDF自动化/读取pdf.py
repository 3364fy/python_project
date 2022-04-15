from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
pdf_file=open('E:\office\pdf\安全评价.pdf','rb')
rsrcmgr=PDFResourceManager()
retstr=StringIO()
laparams=LAParams()

device=TextConverter(rsrcmgr=rsrcmgr,outfp=retstr,laparams=laparams)
process_pdf(rsrcmgr=rsrcmgr,device=device,fp=pdf_file)
device.close()
content=retstr.getvalue()
retstr.close()
pdf_file.close()
print(content)