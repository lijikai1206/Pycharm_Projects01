# -*- coding: utf-8 -*-
import wx


class Frame_01(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'here we go', pos=wx.DefaultPosition, size=(300, 100))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Close", pos=(125, 10), size=(50, 50))
        self.Bind(wx.EVT_BUTTON, self.onCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)

    def onCloseMe(self, event):
        self.Close(True)

    def onCloseWindow(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = Frame_01()
    frame.Show()
    app.MainLoop()