import wx
import wx.grid

class FileDrop( wx.FileDropTarget ):
    def __init__(self):
        wx.FileDropTarget.__init__(self)

    def OnDropFiles(self, x, y, filePath):
        path = filePath[0]

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Tools', size=(600, 800))
        panel = wx.Panel(self, -1)

        #文件拖放
        fileDrop = FileDrop()
        panel.SetDropTarget(fileDrop)

        self.button = wx.Button(panel, -1, "选择Xml", pos=(10, 10), size=(80, 25))
        self.text = wx.TextCtrl(panel, -1, "Xml", pos=(100, 10), size=(470, 25))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        self.button1 = wx.Button(panel, -1, "选择Excel", pos=(10, 45), size=(80, 25))
        self.text1 = wx.TextCtrl(panel, -1, "", pos=(100, 45), size=(470, 25))
        self.button2 = wx.Button(panel, -1, "选择Log", pos=(10, 80), size=(80, 25))
        self.text2 = wx.TextCtrl(panel, -1, "", pos=(100, 80), size=(470, 25))
        #增加下拉选择框
        sampleList = ['Phone1','Phone2', 'Phone3','Demo']
        self.type = wx.StaticText(panel, -1, "Type:", pos=(10, 165),size=(40,25))
        self.type2 = wx.Choice(panel, -1, pos=(55, 160),size=(77,25),choices=sampleList)
        self.button3 = wx.Button(panel, -1, "导入xml系数", pos=(150, 160), size=(80, 25))
        self.button4 = wx.Button(panel, -1, "导入Log数据", pos=(255, 160), size=(80, 25))
        self.button5 = wx.Button(panel, -1, "读取Excel结果", pos=(350, 160), size=(90, 25))
        self.button5 = wx.Button(panel, -1, "计算和照度计差值", pos=(455, 160), size=(115, 25))
        #静态文本显示
        self.CL500_x = wx.StaticText(panel, -1, "CL500_x:", pos=(10,125), size=(50,25))
        self.text_x = wx.TextCtrl(panel, -1, "", pos=(63, 120), size=(70, 25))
        self.Bind(wx.EVT_TEXT, self.Get_ValueX, self.text_x)
        self.CL500_y = wx.StaticText(panel, -1, "CL500_x:", pos=(140, 125), size=(50, 25))
        self.text_y = wx.TextCtrl(panel, -1, "", pos=(198, 120), size=(70, 25))
        self.Bind(wx.EVT_TEXT, self.Get_ValueY, self.text_y)
        self.CL500_CCT = wx.StaticText(panel, -1, "CL500_CCT:", pos=(275, 125), size=(65, 25))
        self.text_CCT = wx.TextCtrl(panel, -1, "", pos=(343, 120), size=(75, 25))
        self.Bind(wx.EVT_TEXT, self.Get_ValueCCT, self.text_CCT)
        self.CL500_LUX = wx.StaticText(panel, -1, "CL500_LUX:", pos=(425, 125), size=(65, 25))
        self.text_LUX = wx.TextCtrl(panel, -1, "", pos=(493, 120), size=(75, 25))
        self.Bind(wx.EVT_TEXT, self.Get_ValueLUX, self.text_LUX)
        self.CL500_LUX = wx.StaticText(panel, -1, "操作记录", pos=(10, 210), size=(80, 25))
        self.text_LUX = wx.TextCtrl(panel, -1, "", pos=(10, 235), size=(560, 150))
        #创建网格
        #grid = wx.grid.Grid(parent, -1, pos=(10, 400), size=(560, 280))

    def OnClick(self, event):
        self.button.SetLabel("Clicked")
    def Get_ValueX(self, event):
        X = self.text_x.GetValue()
        print(X)
        return X
    def Get_ValueY(self, event):
        Y = self.text_y.GetValue()
        print(Y)
        return Y
    def Get_ValueCCT(self, event):
        CCT = self.text_CCT.GetValue()
        print(CCT)
        return CCT
    def Get_ValueLUX(self, event):
        LUX = self.text_LUX.GetValue()
        print(LUX)
        return LUX


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()