#!/usr/bin/python

from win32com.client import Dispatch

def SaveExcel():
    xlApp = Dispatch('Excel.Application')

    xlApp.Visible = True

    xlApp.Workbooks.Open(r"C:\Users\lijik\PycharmProjects\PythonFile\01.ExcelofR&W\win32_learning\\公式计算结果验证.xlsx")
    xlApp.Quit()
    Sheet=None
    Doc=None
    app=None
    while not app==None:
        pythoncom.PumpWaitingMessages()

    xlApp.Save
    print("保存成功！")

SaveExcel()





