# coding: utf-8
print(u"起動")
import wx
title = u"たのしいゲーム"
print(title)

class SampleApp(wx.App):
    def OnInit(self):
        self.init_frame()
        return True

    def init_frame(self):
        self.frm_main = wx.Frame(None)
        self.frm_main.SetTitle(title)
        self.frm_main.SetSize((400, 200))
        self.frm_main.Show()

if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()