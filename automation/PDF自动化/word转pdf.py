from win32com.client import constants, gencache
import time

def createPdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    time.sleep(0.5)
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)
createPdf(r"E:\office\word\安全评价.docx","E:\office\pdf\安全评价.pdf")