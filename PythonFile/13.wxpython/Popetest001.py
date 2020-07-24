#!/usr/bin/python
# coding=utf-8
#  combobox.py
import wx


class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title,
                           size=(250, 270))

        panel = wx.Panel(self, -1, (75, 20), (100, 127),
                         style=wx.SUNKEN_BORDER)
        wx.Button(self, 1, ' 发送 ', (80, 160))

        # self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)

class MyApp(wx.App):
    def OnInit(self):
        dlg = MyDialog(None, -1, 'Popetest001.py')
        dlg.ShowModal()
        dlg.Destroy()
        return True


app = MyApp(0)
app.MainLoop()
