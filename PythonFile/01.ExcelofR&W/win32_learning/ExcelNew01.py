#!/usr/bin/python
from win32com.client import Dispatch
import os

def SaveExcel(filename):
    pwd = os.getcwd()
    xlApp = Dispatch('Excel.Application')
    xlApp.Visible = True
    xlBook = xlApp.Workbooks.Open(pwd + '\\' + filename)
    sht = xlBook.Worksheets(1)
    print(sht)
    xlBook.Save()
    xlBook.Close()
    xlApp.Quit()
SaveExcel('公式计算结果验证.xlsx')

