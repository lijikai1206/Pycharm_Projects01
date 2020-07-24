# coding=utf=8
# 说明：多个按钮使用同一个回调函数
# Python版本：2.7.11

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'多个按钮使用同一个回调函数')

        panel = wx.Panel(self)

        btn_1 = wx.Button(panel, 1, u"按钮1")  # 按钮1的id为1
        btn_2 = wx.Button(panel, 2, u"按钮2")
        btn_3 = wx.Button(panel, 3, u"按钮3")

        self.tc = wx.StaticText(panel, -1, u"按钮测试")

        # 关键点：使用lambda
        self.Bind(wx.EVT_BUTTON, lambda evt, i=btn_1.GetId(): self.OnClick(evt, i), btn_1)
        self.Bind(wx.EVT_BUTTON, lambda evt, i=btn_2.GetId(): self.OnClick(evt, i), btn_2)
        self.Bind(wx.EVT_BUTTON, lambda evt, i=btn_3.GetId(): self.OnClick(evt, i), btn_3)

        buttonLayout = wx.BoxSizer(wx.HORIZONTAL)
        buttonLayout.Add(btn_1, 0, wx.ALL, 15)
        buttonLayout.Add(btn_2, 0, wx.ALL, 15)
        buttonLayout.Add(btn_3, 0, wx.ALL, 15)

        mainLayout = wx.BoxSizer(wx.VERTICAL)
        mainLayout.Add(buttonLayout, 0, wx.ALL, 5)
        mainLayout.Add(self.tc, 1, wx.ALIGN_CENTER_HORIZONTAL)
        panel.SetSizer(mainLayout)

    def OnClick(self, event, index):
        msg = u"按钮" + str(index) + u"被按下"
        print
        msg
        self.tc.SetLabel(msg)


if __name__ == '__main__':
    app = wx.App(0)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
