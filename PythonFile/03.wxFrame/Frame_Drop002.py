import wx,os
class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for name in filenames:
            try:
                f = open(name, 'r')
                text = f.read()
                self.window.WriteText(text)
                f.close()
            except IOError as error:
                dlg = wx.MessageDialog(None, 'Error opening file\n' + str(error))
                dlg.ShowModal()
            except UnicodeDecodeError as error:
                dlg = wx.MessageDialog(None, 'Cannot open non ascii files\n' + str(error))
                dlg.ShowModal()
class DropFile(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="", size = (450, 400))

        self.text = wx.TextCtrl(self, -1, style = wx.TE_MULTILINE|wx.TE_RICH2)
        dt = FileDrop(self.text)
        self.text.SetDropTarget(dt)
        self.Centre()
        self.Show(True)
app = wx.App()
DropFile(None, -1)
app.MainLoop()