# pip3 install -U wxPython
import wx

class CalcForm(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (200, 400), style = wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.MAXIMIZE_BOX)
        
        self.controller = None
        
        # ui
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        
        self._disp = wx.TextCtrl(self, value = "ddd", style = wx.TE_RIGHT | wx.TE_READONLY)
        self._sizer.Add(self._disp, flag = wx.EXPAND | wx.ALL, border = 5)

        sizer = wx.GridSizer(5, 4, 5, 5)
        self._sizer.Add(sizer, flag = wx.EXPAND | wx.ALL, border = 5)

        # 1 line
        sizer.Add(self.BindButton(self.CreateButton('AC'), 'ALL_CLEAR'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('C'), 'CLEAR'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('sqrt'), 'SQRT'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('/'), 'DIVISION'), flag = wx.EXPAND)
        # 2 line
        sizer.Add(self.BindButton(self.CreateButton('7'), '7'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('8'), '8'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('9'), '9'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('*'), 'MULTIPLICATION'), flag = wx.EXPAND)
        # 3 line
        sizer.Add(self.BindButton(self.CreateButton('4'), '4'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('5'), '5'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('6'), '6'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('-'), 'SUBSTRACTION'), flag = wx.EXPAND)
        # 4 line
        sizer.Add(self.BindButton(self.CreateButton('1'), '1'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('2'), '2'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('3'), '3'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('+'), 'ADDITION'), flag = wx.EXPAND)
        # 4 line
        sizer.Add(self.BindButton(self.CreateButton('0'), '0'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('.'), 'DOT'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('+/-'), 'SIGN'), flag = wx.EXPAND)
        sizer.Add(self.BindButton(self.CreateButton('='), 'CALCULATE'), flag = wx.EXPAND)

    def CreateButton(self, label):
        return wx.Button(self, label = label, style = wx.BU_EXACTFIT)

    def BindButton(self, button, tag):
        button.UserData = tag
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)
        return button

    def OnSize(self, event):
        self.Size = (min(event.Size[0], 320), self._sizer.ComputeFittingWindowSize(self)[1])
        self.Layout()
    
    def OnClick(self, event):
        # call controller.command
        self.controller.command(event.EventObject.UserData)

    # interface for controller
    def ShowResult(self, result):
        self._disp.Value = result