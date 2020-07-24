import wx
import os
class my_frame(wx.Frame):
    """This is a simple text editor"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE,)
        self.Show(True)
        self.CreateStatusBar()#创建窗口底部的状态栏

        filemenu = wx.Menu()
        menu_open = filemenu.Append(wx.ID_OPEN,U"打开文件", " ")
        menu_exit = filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        menu_about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")#设置菜单的内容

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"设置")
        self.SetMenuBar(menuBar)#创建菜单条
        self.Show(True)

        self.Bind(wx.EVT_MENU,self.on_open,menu_open)
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)#把出现的事件，同需要处理的函数连接起来

    def on_about(self,e):#about按钮的处理函数
        dlg = wx.MessageDialog(self,"A samll text editor", "About sample Editor",wx.OK)#创建一个对话框，有一个ok的按钮
        dlg.ShowModal()#显示对话框
        dlg.Destroy()#完成后，销毁它。

    def on_exit(self,e):
        self.Close(True)

    def on_open(self,e):
        """open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self,"Choose a file", self.dirname, "","*.*",wx.OPEN)#调用一个函数打开对话框
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename),"r")
        dlg.Destroy()


app = wx.App(False)
frame = my_frame(None, 'Small edior')
app.MainLoop()