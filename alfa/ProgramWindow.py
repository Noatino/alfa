#! /usr/bin/python
# -*- coding: utf-8 _*_
#ProgramWindow.py

######################################################
#### Second frame from the program, in this frame ####
####   we will use all the properties from Alpha  ####
######################################################


#We make sure that all the modules are correct import for the
#use of the program.
try:
    import wx
except ImportError:
    errorMessage = "Please, check all the dependences for alpha"
    raise ImportError,errorMessage


class ProgramWindow(wx.Frame):
    
    def __init__(self, parent):
        '''
        __init__ from the second frame from Alpha
        '''
        wx.Frame.__init__(self, parent, wx.NewId(), "Alpha",
                          pos=(130,130), size=(400,300))

        self.panel = wx.Panel(self,-1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel,1,wx.EXPAND,0)

        self.SetSizer(sizer)
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.CloseWindow)

    def CloseWindow(self, event):
        self.windowFather.Show()
        self.Destroy()


if __name__ == "__main__":
    app = wx.App(0)
    Window = ProgramWindow(None)
    Window.Show(True)
    app.MainLoop()
