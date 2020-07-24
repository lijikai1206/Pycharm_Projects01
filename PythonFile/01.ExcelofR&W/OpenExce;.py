#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com
from win32com.client import Dispatch, constants

def excel_open(file_path,results,sheet_name):
    time.sleep(3)
    xlApp = win32com.client.DispatchEx("Excel.Application")  #打开excel操作环境
    xlApp.Visible = True    #进程可见，False是它暗自进行
    xlApp.DisplayAlerts = 0   #不跳出来。
    xlBook = xlApp.Workbooks.Open(file_path,False)  #打开文件，有时候会有警告框说由外部链接什么的（与里面公式有关），要点是则True，否则False
    sht = xlBook.Worksheets(sheet_name)  #找到要操作的sheet
    for i in range(len(results)):  # sheet数据,日期列格式为date
        for j in range(len(results[0])):
            sht.Cells(i + 2, j + 1).Value =results[i][j]   #从第二行第二列开始填入数据。
    print("WRITE FINISHED")
    xlBook.Close(True)    #关闭该文件，并保存。不保存就是False
    xlApp.quit()   #关闭excel操作环境。


def useVBA(VBA):
    xlApp = win32com.client.DispatchEx("Excel.Application")
    xlApp.Visible = True
    xlApp.DisplayAlerts = 0
    xlBook = xlApp.Workbooks.Open(file_path,False)
    xlBook.Application.Run(VBA) #宏
    xlBook.Close(True)
    xlApp.quit()

results=((5,2,1),(7,2,7),(4,0,3))    #这是要填入的数据，一个3*3元组
file_path="D:\hel.xlsm" #文件
sheet_name="我还在想"
VBA="每日操作"
excel_open(file_path,results,sheet_name)
#useVBA(VBA)
