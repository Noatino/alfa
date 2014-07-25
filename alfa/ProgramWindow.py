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
    import convertPoints as cp
except ImportError:
    errorMessage = "Please, check all the dependences for alpha"
    raise ImportError,errorMessage




class ProgramWindow(wx.Frame):

    global flag #Flag for the check box
    flag = True

    def setPaths(self, filePaths):
        paths = filePaths
    
    def __init__(self, parent):
      
        '''
        __init__ from the second frame from Alpha
        '''

        wx.Frame.__init__(self, parent, wx.NewId(), "Alpha",
                          pos=(130,130), size=(400,300))

        self.panel = wx.Panel(self,-1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel,1,wx.EXPAND,0)        

        ##########################################################
        ####              Below is the code for               ####
        #### Convert the basis of the .dat files to log scale ####
        ##########################################################

        self.cb = wx.CheckBox(self.panel, -1, 'Check the graph of points', (130,35))
        self.cb.SetValue(True)
        wx.EVT_CHECKBOX(self, self.cb.GetId(),self.ShowGraph)

        self.buttonChange = wx.Button(self.panel,-1,"Change basis" ,(30,30))
        self.buttonChange.Bind(wx.EVT_BUTTON,self.ChangeBasis)


        #self.buttonChange = wx.Button(self,wx.NewId(),"Change basis")
        #sizer.Add(self.buttonChange)
        #self.Bind(wx.EVT_BUTTON, self.ChangeBasis)


        ###########################################################
        
        self.SetSizer(sizer)
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.CloseWindow)
        self.Centre()

    def CloseWindow(self, event):
        '''
        Instructions for close this window
        '''
        
        self.windowFather.Show()
        self.Destroy()



    def ShowGraph(self, event):
        '''
        Instructions for the check box, just change
        the boolean value to set visible the graph or not
        '''
        if self.cb.GetValue():
            flag = True

        else:
            flag = False

    def ChangeBasis(self,event):
        changeStatus = event.GetEventObject()

        #####################################
        ### Here make the change of scale ###
        #####################################

        if flag == True:
            #print "Chage basis with graph in ",flag
            
        changeStatus.Disable()
        self.cb.Disable()

if __name__ == "__main__":
    app = wx.App(0)
    Window = ProgramWindow(None)
    Window.Show(True)
    app.MainLoop()
