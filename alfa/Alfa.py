######################################################
####    Alfa program to make something in GRB     ####
#### Antonio Galvan, Nissim Fraija, Uriel Luviano ####
####Python 2.7, wxPython (classic) 3.0.0.0, pyRoot####
######################################################

import wx

class Frame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Alpha',
            pos=(300,150), size = (320,250))
        self.SetBackgroundColour("gray")

        self.button1 = wx.Button(self, id=-1, label='Button1',
            pos=(8, 8), size=(10, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.button1Click)
        # optional tooltip
        self.button1.SetToolTip(wx.ToolTip("click to hide"))
        
        # show the frame
        self.Show(True)
    def button1Click(self,event):
        self.button1.Hide()
        self.SetTitle("Button1 clicked")


application = wx.PySimpleApp()
# call class Frame
window = Frame()
# start the event loop
application.MainLoop()

