#分割窗口
import wx
#自定义一个窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="分割窗口",size=(400,300))
        self.Center() #设置窗口居中
        #创建一个splitter
        self.splitter=wx.SplitterWindow(self,-1)
        #创建左侧面板
        self.leftpanel=wx.Panel(self.splitter)
        #创建左侧面板
        self.rightpanel=wx.Panel(self.splitter)
        self.splitter.SplitVertically(self.leftpanel,self.rightpanel,100)
        self.splitter.SetMinimumPaneSize(80)
        list2=['苹果',"橘子","香蕉"]
        lb2=wx.ListBox(self.leftpanel,-1,choices=list2,style=wx.LB_SINGLE)

        self.Bind(wx.EVT_LISTBOX,self.on_listbox,lb2)
        #布局
        vbox1=wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb2,1,flag=wx.ALL | wx.EXPAND,border=5)
        self.leftpanel.SetSizer(vbox1)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        self.content=wx.StaticText(self.rightpanel,label='右侧面板')
        vbox2.Add(self.content,1,flag=wx.ALL|wx.EXPAND,border=5)
        self.rightpanel.SetSizer(vbox2)

    def on_listbox(self,event):
        s='选择{0}'.format(event.GetString())
        self.content.SetLabel(s)

#自定以一个应用程序类
class App(wx.App):
    def OnInit(self):
        #创建窗口对象
        frame=MyFrame()
        frame.Show()
        return True
    def OnExit(self):
        print("应用程序退出")
        return 0

if __name__=='__main__':
    app=App()#创建自定以对象App
    app.MainLoop()#进入事件主循环
