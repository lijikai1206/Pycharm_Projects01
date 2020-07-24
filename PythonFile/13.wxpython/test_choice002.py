import wx


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Routing Policy Selector', size=(300, 500))
        self.Center()
        self.panel = wx.Panel(self, -1)
        SenderOption = ['connector_proc', 'echo_plugin']
        wx.StaticText(self.panel, -1, "Sender: ", (20, 20))
        self.SenderList = wx.Choice(self.panel, -1, (90, 18), choices=SenderOption)
        # 第二个Choice初始选项为空
        self.test = wx.Choice(self.panel, -1, (90, 58), choices=[])
        ConfirmButton = wx.Button(self.panel, label='Confirm', pos=(60, 400), size=(60, 30))
        CancelButton = wx.Button(self.panel, label='Cancel', pos=(160, 400), size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.OnConfirm, ConfirmButton)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, CancelButton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # 检测第一个选择绑定函数
        self.Bind(wx.EVT_CHOICE, self.OnTest, self.SenderList)

    # 第一个框体选择操作触发的函数 第二个框体选项为123
    def OnTest(self, event):
        Sender = self.SenderList.GetStringSelection()
        if Sender == 'connector_proc':
            print('half')
            # self.test = wx.Choice(self.panel, -1, (90, 58), choices=['1', '2', '3'])
            newItems = ['1', '2', '3']
            self.test.SetItems(newItems)
        self.Refresh()
        print("刷新完成！")

    def OnConfirm(self, event):
        Sender = self.SenderList.GetStringSelection()
        print(Sender)
        # self.Close(False)

    def OnCancel(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()

