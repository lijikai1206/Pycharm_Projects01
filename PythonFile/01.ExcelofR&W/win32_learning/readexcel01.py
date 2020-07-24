import win32com.client
import win32com.client

def ReadExcel(filename):
    xlApp = win32com.client.Dispatch('Excel.Application')
    xlApp.Visible = True
    xlApp.DisplayAlerts = True
    xlBook = xlApp.Workbooks.Open(filename)
    sht = xlBook.Worksheets()
    value = sht.Cells(2, 6).Value
    print(value)

ReadExcel("公式计算结果验证.xlsx")
