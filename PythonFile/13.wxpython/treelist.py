# coding=utf-8
import wx
import wx.lib.agw.customtreectrl as CT


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "CustomTreeCtrl")
        self.custom_tree = CT.CustomTreeCtrl(self, agwStyle=wx.TR_DEFAULT_STYLE)
        root = self.custom_tree.AddRoot(u"根选项")

        for y in range(5):
            item = self.custom_tree.AppendItem(root, u"选项%d" % y, ct_type=1)


app = wx.PySimpleApp()
frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()
app.MainLoop()