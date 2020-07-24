#! /usr/bin/env python
# coding:UTF-8
#
# wx静态文本使用范例

__author__ = "zyl508@gamil.com"
__date__ = "$2010-5-14 9:10:52$"

import wx


# 窗口类
class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Example For StaticText", size=(400, 300))
        panel = wx.Panel(self, -1)

        # 基本静态文本
        wx.StaticText(panel, -1, "This is a basic StaticText Example", (100, 10))

        # 指定前景色和背景色
        stext = wx.StaticText(panel, -1, "StaticText with Fg and Bg Colour", (100, 30))
        stext.SetForegroundColour("White")
        stext.SetBackgroundColour("Black")

        # 指定居中对齐
        centerText = wx.StaticText(panel, -1, "Align Center", (100, 50), (160, -1),
                                   wx.ALIGN_CENTER)
        centerText.SetForegroundColour("White")
        centerText.SetBackgroundColour("Black")

        # 指定右对齐
        rightText = wx.StaticText(panel, -1, "Align Right", (100, 70), (160, -1),
                                  wx.ALIGN_RIGHT)
        rightText.SetForegroundColour("White")
        rightText.SetBackgroundColour("Black")

        # 指定字体的静态文本
        str = "You can change the font"
        fontText = wx.StaticText(panel, -1, str, (20, 100))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        fontText.SetFont(font)

        # 设置多行文本
        mutiStr = "Here we go\nYou can see\nThe ending!"
        wx.StaticText(panel, -1, mutiStr, (20, 150))

        # 设置多行文本右对齐
        mutiRightStr = "Example again\n But this time\nWe Align Right!"
        wx.StaticText(panel, -1, mutiRightStr, (220, 150),
                      style=wx.ALIGN_RIGHT)


def main():
    app = wx.PySimpleApp()
    frame = StaticTextFrame()
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
