import wx

import model
import view
import controller

app = wx.App()

model = model.CalcModel()
view = view.CalcForm(None, "Calc")
controller = controller.CalcController(model, view)

view.controller = controller

view.Show(True)
app.MainLoop()
