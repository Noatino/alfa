#! /usr/bin/python
# -*- coding: utf-8 _*_
#Alpha

######################################################
####    Alfa program to make something in GRB's   ####
#### Antonio Galvan, Nissim Fraija, Uriel Luviano ####
####Python 2.7, wxPython (classic) 3.0.0.0, pyRoot####
####                  matplotlib                  ####
######################################################


#We make sure that all the modules are correct import for the
#use of the program.
try:
    import wx

except ImportError:
    errorMessage = "Please, check all the dependences for alpha"
    raise ImportError,errorMessage


#Now we define the main class of the program

class Alpha(wx.Frame):
    
    def __init__(self, parent, id, title):
        '''
        __init__
        '''
        wx.Frame.__init__(self, parent, id, title,
        pos=(50,100), size=(950, 550))
        self.parent = parent
        self.inicialize()



    def inicialize(self):
        '''
        inicializer method
        '''


        #We define all the sizer to use in the program
        Top = wx.BoxSizer(wx.VERTICAL)
        title = wx.BoxSizer(wx.HORIZONTAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)

        global vbox2
        vbox2 = wx.BoxSizer(wx.VERTICAL)

        #Now the panels
        Tpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        Lpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)


        #We use global panels to the right side of the window
        global Rpanel
        Rpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        
        #In this list, we gonna store the file's paths
        global paths
        paths = []
        global display
        display = []

        #This is the box of the control list of the rigth panel
        global lBox
        
        title.Add(Tpanel, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(Lpanel, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(Rpanel, 1, wx.EXPAND | wx.ALL, 3)

        #######################################################################################
        #Welcome message
        wx.StaticText(Tpanel, -1, "Hello, the finally of this program is ... ", pos = (10,10))
        #######################################################################################

        #######################################################################################
        #First panel
        #######################################################################################


        #######################################################################################
        #Button to charge files 
        #######################################################################################
        #######################################################################################
        #**Open files
        #######################################################################################
        self.buttonCharge = wx.Button(Lpanel,10,"Charge files" ,(10,30))
        wx.StaticText(Lpanel, -1, "Click to charge your \n experiment files", pos = (10,60))
        self.Bind(wx.EVT_BUTTON, self.chargeFiles, id = 10)

        #######################################################################################
        #** Rigth Panel
        #######################################################################################
        StringTextWelcome = "Welcome, thanks to use Alpha for you research"
        self.messageWelcome = wx.StaticText(Rpanel,-1,StringTextWelcome , pos=(20,10))
        
        StringTextFiles = "Would you like make a change of basis of your files?"
        self.messageCharge = wx.StaticText(Rpanel,-1,StringTextFiles , pos=(20,10))
        self.messageCharge.Show(False)



        #######################################################################################
        #**Sincrotron radation
        #######################################################################################
        self.buttonSinc = wx.Button(Lpanel,11,"Sincrotron fit Root" ,(10,100))
        StringTextSycn = "Make fit of the Synchrotron \n scattering"
        wx.StaticText(Lpanel, -1, StringTextSycn, pos = (10,130))
        self.Bind(wx.EVT_BUTTON, self.SincRoot, id = 11)

        #######################################################################################
        #** Rigth Panel
        #######################################################################################
        StringTextSync = "Please, selec the files with I do the fit of the emission of Synchrotron"
        self.TextoSync = wx.StaticText(Rpanel,-1, StringTextSync , pos=(20,10))
        self.TextoSync.Show(False)
        

        ########################################################################################
        #**Inverse Compton scattering
        ########################################################################################
        self.buttonComp = wx.Button(Lpanel,12,"Inverse Compton \n fit Root" ,(10,185))
        wx.StaticText(Lpanel, -1, "Make fit of the Inverse \n Compton scattering" , pos = (10,250))
        self.Bind(wx.EVT_BUTTON, self.InvCom, id = 12)

        ########################################################################################
        #** Smoothing the graph
        ########################################################################################
        self.buttonSG = wx.Button(Lpanel,13,"Smooth Graph" ,(10,290))
        wx.StaticText(Lpanel, -1, "Make the smoothing of the graph" , pos = (10,330))
        self.Bind(wx.EVT_BUTTON, self.SGraph, id = 13)

        ########################################################################################
        #** Exit button
        ########################################################################################
        self.buttonEX = wx.Button(Lpanel,14,"Exit" ,(10,350))
        wx.StaticText(Lpanel, -1, "Close the program" , pos = (10,390))
        self.Bind(wx.EVT_BUTTON, self.Evtexit, id = 14)
        

        #########################################################################
        ### Put a flag to disable the buttons on the main window ################
        #########################################################################
        self.buttonSinc.Disable()                  ##############################
        self.buttonComp.Disable()                  ##############################
        self.buttonSG.Disable()                    ##############################
                                                   ##############################
        hbox.Add(vbox1, 1, wx.EXPAND)              ##############################
        hbox.Add(vbox2, 3, wx.EXPAND)              ##############################
        Top.Add(title, 1,wx.EXPAND)                ##############################
        Top.Add(hbox, 5, wx.EXPAND)                ##############################
        #########################################################################
        
        self.SetSizer(Top)
        self.Show(True)

        ############ End of initialize ########################################################### 


    def chargeFiles(self, event):
        '''
        Invoque the window to charge the files to the program.

        Create and show the file dialog to select the data files
        of the experiments, and return the paths, in this button
        we will call the new window of the program
        '''

        self.TextoSync.Show(False)
        self.messageCharge.Show(True)
        
        wildCard = "Data files (*.dat)|*.dat;" #Here we define that we can only read
        #.dat files for Alpha
        #Now we going to make the file dialog window
        dialog = wx.FileDialog(
            self, message = "Select the data files",
            defaultFile = "",
            wildcard = wildCard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        election = dialog.ShowModal() #We store the election of the user here
        if election == wx.ID_OK:
            #######################################################################
            # Store all the paths of the files with the data experiments in a list#
            #######################################################################
            #### I need to do something that I don't repeat elements in the    ####
            #### list and                                                   ####
            tmp_p = dialog.GetPaths()

            for path in tmp_p:
                tmp = path.split('/')
                path1 = '/'+tmp[len(tmp)-1]
                display.extend([path1])
            paths.extend(tmp_p)                                                ####
                                                                               ####
            #######################################################################
            lBox =  wx.CheckListBox(Rpanel, id = 15, pos = (20,40),choices = display,
                                    size = (400,350))
            vbox2.Add(lBox)
            
        else:
            return

        ###########################################################################
        ########## Now I will enable and show all elements with I can't see  ######
        ###########################################################################
        self.buttonSinc.Enable()    # Now we gonna go to enable the buttons  ######
        self.buttonComp.Enable()    # and then we can work with the other    ######
        self.buttonSG.Enable()      # modules of the program.                ######
        self.messageCharge.Show(True)                                        ######
        ###########################################################################
        ########## Now I disable all the elements of the principal frame     ######
        ###########################################################################
        self.messageWelcome.Show(False)                                      ######
        ###########################################################################


    def SincRoot(self, event):
        '''
        Invoque the frame to make the fit on the Synchrotron radiation
        '''
        ###########################################################################
        ########## I will now appear all the panel of synchrotron radation   ######
        ###########################################################################
        self.messageWelcome.Show(False)
        self.messageCharge.Show(False)
        self.TextoSync.Show(True)                                            ######
        ###########################################################################
        


        pass

    def InvCom(self, event):
        ''' 
        Invoque the window to make the fit on the Inverse Compton Scattering
        '''
        
        pass

    def SGraph(self, event):
        '''
        Invoque the window to make the Smooth of the final graph
        '''
        
        pass



    def Evtexit(self, event):
        '''
        Close the program
        '''
        mess1 = 'Remember'
        mess2 = 'Thanks to use Alpha, please if you used by you research please cite as @'
        mess3 = '\n Do you want close the program?'
        dial = wx.MessageDialog(None, mess2+mess3, mess1,
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            
        ret = dial.ShowModal()
        
        if ret == wx.ID_YES:
            self.Destroy()
            quit()

        
if __name__ == "__main__":
    app = wx.App()
    frame = Alpha(None, -1, 'Alpha')
    app.MainLoop()
