
# -*- coding: utf-8 _*_
#Alpha

######################################################
####    Alfa program to make something in GRB's   ####
#### Antonio Galvan  agalvan@astro.unam.mx        ####
#### Nissim Fraija   nifraija@astro.unam.mx       ####
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
        StringTextHeader = "Hello, this program will help you to make the SED of your favorite AGN"

        #This is the box of the control list of the rigth panel
        global lBox
        
        title.Add(Tpanel, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(Lpanel, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(Rpanel, 1, wx.EXPAND | wx.ALL, 3)

        #######################################################################################
        #Welcome message
        wx.StaticText(Tpanel, -1, StringTextHeader, pos = (10,10))
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
        self.Bind(wx.EVT_BUTTON, self.charge_button, id = 10)

        #######################################################################################
        #** Rigth Panel
        #######################################################################################
        StringTextWelcome = "Welcome, please select the files that you will use."
        self.messageWelcome = wx.StaticText(Rpanel,-1,StringTextWelcome , pos=(20,10))
        
        StringTextFiles = "Please, select the files in their respective emission radiation process"
        self.messageCharge = wx.StaticText(Rpanel,-1,StringTextFiles , pos=(20,10))
        self.messageCharge.Show(False)

        
        #######################################################################################
        #** Rigth Panel
        #######################################################################################


        #######################################################################################
        ### Elements to use on the syncrotron scattering panel
        #######################################################################################

        StringTextSync = "Please, give me the parameters to do the fit of the Syncrotron Scattering"
        self.TextoSync = wx.StaticText(Rpanel,-1, StringTextSync , pos=(20,10))
        self.TextoSync.Show(False)


        #######################################################################################
        ### Definition of the elements of the syncrotron screen
        #######################################################################################


        self.buttonSync = wx.Button(Lpanel,11,"Syncrotron fit Root" ,(10,100))
        StringTextSycn = "Make fit of the Synchrotron \n scattering"
        wx.StaticText(Lpanel, -1, StringTextSycn, pos = (10,130))
        self.Bind(wx.EVT_BUTTON, self.SyncRoot, id = 11)

        

        #A0 box parameters
        A0Label = "A0 parameter"
        self.A0ValTextSync = wx.StaticText(Rpanel, -1, A0Label, pos=(20,30)) #pos = (x,y)
        self.A0ValTextSync.Show(False)
        self.A0val = wx.TextCtrl(Rpanel, -1, "ASync value", pos=(180,30), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixA0 = wx.CheckBox(Rpanel, -1, "Fix A0", pos = (310, 30))
        
        A0Label = "A0 parameter range"
        self.A0ValTextSync = wx.StaticText(Rpanel, -1, A0Label, pos=(20,60)) #pos = (x,y)
        self.A0valXmin = wx.TextCtrl(Rpanel, -1, "A0 min value", pos=(180,60), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.A0valXmax = wx.TextCtrl(Rpanel, -1, "A0 max value", pos=(310,60), size=(100,25), style=wx.TE_PROCESS_ENTER)


        #alfa box parameters
        alfaLabel = "Alfa parameter"
        self.alfaValTextSync = wx.StaticText(Rpanel, -1, alfaLabel, pos=(20,90)) #pos = (x,y)
        self.alfaValTextSync.Show(False)
        self.alfaval = wx.TextCtrl(Rpanel, -1, "Alfa value", pos=(180,90), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixalfa = wx.CheckBox(Rpanel, -1, "Fix Alfa", pos = (310, 90))
        alfaLabel = "Alfa parameter range"
        self.alfaValTextSync = wx.StaticText(Rpanel, -1, alfaLabel, pos=(20,120)) #pos = (x,y)
        self.alfavalXmin = wx.TextCtrl(Rpanel, -1, "Alfa min value", pos=(180,120), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.alfavalXmax = wx.TextCtrl(Rpanel, -1, "Alfa max value", pos=(310,120), size=(100,25), style=wx.TE_PROCESS_ENTER)
        


        #Emin box parameters
        EminLabel = "Emin parameter"
        self.EminValTextSync = wx.StaticText(Rpanel, -1, EminLabel, pos=(20,150)) #pos = (x,y)
        self.EminValTextSync.Show(False)
        self.Eminval = wx.TextCtrl(Rpanel, -1, "Emin value", pos=(180,150), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixEmin = wx.CheckBox(Rpanel, -1, "Fix Emin", pos = (310, 150))
        EminLabel = "Emin parameter range"
        self.EminValTextSync = wx.StaticText(Rpanel, -1, EminLabel, pos=(20,180)) #pos = (x,y)
        self.EminvalXmin = wx.TextCtrl(Rpanel, -1, "Emin min value", pos=(180,180), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.EminvalXmax = wx.TextCtrl(Rpanel, -1, "Emin max value", pos=(310,180), size=(100,25), style=wx.TE_PROCESS_ENTER)


        #Ecut box parameters
        EcutLabel = "Ecut parameter"
        self.EcutValTextSync = wx.StaticText(Rpanel, -1, EcutLabel, pos=(20,210)) #pos = (x,y)
        self.EcutValTextSync.Show(False)
        self.Ecutval = wx.TextCtrl(Rpanel, -1, "Ecut value", pos=(180,210), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixEcut = wx.CheckBox(Rpanel, -1, "Fix Ecut", pos = (310, 210))
        EcutLabel = "Ecut parameter range"
        self.EcutValTextSync = wx.StaticText(Rpanel, -1, EcutLabel, pos=(20,240)) #pos = (x,y)
        self.EcutvalXmin = wx.TextCtrl(Rpanel, -1, "Ecut min value", pos=(180,240), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.EcutvalXmax = wx.TextCtrl(Rpanel, -1, "Ecut max value", pos=(310,240), size=(100,25), style=wx.TE_PROCESS_ENTER)
        

        #Fit button
        self.buttonChargeSVal = wx.Button(Rpanel,16, "Fit", (600,390))
        self.Bind(wx.EVT_BUTTON, self.getValues_fit_sync, id = 16)


        ########################################################################################
        ### Now I will disapear all the elements of this screen
        ########################################################################################
        self.A0ValTextSync.Show(False)
        self.alfaValTextSync.Show(False)
        self.EminValTextSync.Show(False)
        self.EcutValTextSync.Show(False)
        #---
        self.A0ValTextSync.Show(False)
        self.A0val.Show(False)
        self.fixA0.Show(False)
        self.A0ValTextSync.Show(False)
        self.A0valXmin.Show(False)
        self.A0valXmax.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfaval.Show(False)
        self.fixalfa.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfavalXmin.Show(False)
        self.alfavalXmax.Show(False)
        self.EminValTextSync.Show(False)
        self.Eminval.Show(False)
        self.fixEmin.Show(False)
        self.EminValTextSync.Show(False)
        self.EminvalXmin.Show(False)
        self.EminvalXmax.Show(False)
        self.EcutValTextSync.Show(False)
        self.Ecutval.Show(False)
        self.fixEcut.Show(False)
        self.EcutValTextSync.Show(False)
        self.EcutvalXmin.Show(False)
        self.EcutvalXmax.Show(False)
        self.buttonChargeSVal.Show(False)
        #--
        

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
        self.buttonSync.Disable()                  ##############################
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


        
        ########################################################################################
        self.messageCharge.Show(False)
        ########################################################################################
        ### Now I will disapear all the elements of Syncrotron
        ########################################################################################
        self.TextoSync.Show(False)
        self.A0ValTextSync.Show(False)
        self.alfaValTextSync.Show(False)
        self.EminValTextSync.Show(False)
        self.EcutValTextSync.Show(False)
        #---
        self.A0ValTextSync.Show(False)
        self.A0val.Show(False)
        self.fixA0.Show(False)
        self.A0ValTextSync.Show(False)
        self.A0valXmin.Show(False)
        self.A0valXmax.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfaval.Show(False)
        self.fixalfa.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfavalXmin.Show(False)
        self.alfavalXmax.Show(False)
        self.EminValTextSync.Show(False)
        self.Eminval.Show(False)
        self.fixEmin.Show(False)
        self.EminValTextSync.Show(False)
        self.EminvalXmin.Show(False)
        self.EminvalXmax.Show(False)
        self.EcutValTextSync.Show(False)
        self.Ecutval.Show(False)
        self.fixEcut.Show(False)
        self.EcutValTextSync.Show(False)
        self.EcutvalXmin.Show(False)
        self.EcutvalXmax.Show(False)
        self.buttonChargeSVal.Show(False)
        #--
        ########################################################################################
        
        
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
                path1 = tmp[len(tmp)-1]
                display.extend([path1])
            paths.extend(tmp_p)                                                ####
                                                                               ####
            #######################################################################
            self.lBox =  wx.CheckListBox(Rpanel, id = 15, pos = (20,40),choices = display,
                                    size = (400,350))
            
            
            vbox2.Add(self.lBox)

            ###########################################################
            
            if paths != []:
                ###########################################################################
                ########## Now I will enable and show all elements with I can't see  ######
                ###########################################################################
                self.buttonSync.Enable()    # Now we gonna go to enable the buttons  ######
                self.buttonComp.Enable()    # and then we can work with the other    ######
                self.buttonSG.Enable()      # modules of the program.                ######
                self.messageCharge.Show(True)                                        ######
                ###########################################################################
                ########## Now I disable all the elements of the principal frame     ######
                ###########################################################################
                self.messageWelcome.Show(False)                                      ######
                ###########################################################################


    def SyncRoot(self, event):
        '''
        Invoque the frame to make the fit on the Synchrotron radiation
        '''
        ###########################################################################
        ########## I will now disappear all the not sync elements of the panel ####
        ###########################################################################
        self.messageWelcome.Show(False)
        self.messageCharge.Show(False)
        self.lBox.Show(False)
        self.buttonCharge.Show(False)
        
        ###########################################################################
        #Now I will define the elements that could be on the fit parameters    ####
        ###########################################################################
        self.TextoSync.Show(True)
        self.A0ValTextSync.Show(True)
        self.alfaValTextSync.Show(True)
        self.EminValTextSync.Show(True)
        self.EcutValTextSync.Show(True)
        #---
        self.A0ValTextSync.Show(True)
        self.alfaValTextSync.Show(True)
        self.EminValTextSync.Show(True)
        self.EcutValTextSync.Show(True)
        #---
        self.A0ValTextSync.Show(True)
        self.A0val.Show(True)
        self.fixA0.Show(True)
        self.A0ValTextSync.Show(True)
        self.A0valXmin.Show(True)
        self.A0valXmax.Show(True)
        self.alfaValTextSync.Show(True)
        self.alfaval.Show(True)
        self.fixalfa.Show(True)
        self.alfaValTextSync.Show(True)
        self.alfavalXmin.Show(True)
        self.alfavalXmax.Show(True)
        self.EminValTextSync.Show(True)
        self.Eminval.Show(True)
        self.fixEmin.Show(True)
        self.EminValTextSync.Show(True)
        self.EminvalXmin.Show(True)
        self.EminvalXmax.Show(True)
        self.EcutValTextSync.Show(True)
        self.Ecutval.Show(True)
        self.fixEcut.Show(True)
        self.EcutValTextSync.Show(True)
        self.EcutvalXmin.Show(True)
        self.EcutvalXmax.Show(True)
        ###########################################################################

        #Button to load the fit parameters of syncrotron radiation
        self.buttonChargeSVal.Show(True)
        
        return

    def InvCom(self, event):
        ''' 
        Invoque the window to make the fit on the Inverse Compton Scattering
        '''

        ########################################################################################
        ### Now I will disapear all the elements of this screen
        ########################################################################################
        self.A0ValTextSync.Show(False)
        self.alfaValTextSync.Show(False)
        self.EminValTextSync.Show(False)
        self.EcutValTextSync.Show(False)
        #---
        self.A0ValTextSync.Show(False)
        self.A0val.Show(False)
        self.fixA0.Show(False)
        self.A0ValTextSync.Show(False)
        self.A0valXmin.Show(False)
        self.A0valXmax.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfaval.Show(False)
        self.fixalfa.Show(False)
        self.alfaValTextSync.Show(False)
        self.alfavalXmin.Show(False)
        self.alfavalXmax.Show(False)
        self.EminValTextSync.Show(False)
        self.Eminval.Show(False)
        self.fixEmin.Show(False)
        self.EminValTextSync.Show(False)
        self.EminvalXmin.Show(False)
        self.EminvalXmax.Show(False)
        self.EcutValTextSync.Show(False)
        self.Ecutval.Show(False)
        self.fixEcut.Show(False)
        self.EcutValTextSync.Show(False)
        self.EcutvalXmin.Show(False)
        self.EcutvalXmax.Show(False)
        self.buttonChargeSVal.Show(False)
        #--
        
        pass

    def SGraph(self, event):
        '''
        Invoque the window to make the Smooth of the final graph
        '''
        
        pass

    def charge_button(self, event):
        '''
        Generate the configuration to see the screen of charge files
        '''

        ###################################################################
        #  Desable the elems from the Syncrotron Scattering panel    ######
        #                                                            ######
        try:
            self.A0ValTextSync.Show(False)
            self.buttonChargeSVal.Show(False)
            self.A0val.Show(False)
        except AttributeError as e:
            #Really I dont wanna do nothing in this exception because can be generate
            #the firts time that I click the button
            print "Err"
            pass
        ###################################################################

        self.messageCharge.Show(True)
        self.messageWelcome.Show(False)
        self.TextoSync.Show(False)
        self.buttonCharge = wx.Button(Rpanel,15, "Load Files", (600,390))
        self.Bind(wx.EVT_BUTTON, self.chargeFiles, id = 15)
        try:
            self.lBox.Show(True)
            self.fixA0.Show(False)
        except AttributeError as e:
            #Really I dont wanna do nothing in this exceptio because can be generate
            #the firts time that I click the button
            print "Err"
            pass


    def getValues_fit_sync(self, event):
        stringValue10 = self.A0val.GetValue()
        print stringValue10, "Ann"
        return



    def Evtexit(self, event):
        '''
        Close the program
        '''
        mess1 = 'Remember'
        mess2 = 'Thanks to use Alpha, please if you used by you research please cite as @'
        mess3 = '\n Do you want close the program?'
        dial = wx.MessageDialog(None, mess2+mess3, mess1,
            wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
            
        ret = dial.ShowModal()
        
        if ret == wx.ID_YES:
            self.Destroy()
            quit()

        
if __name__ == "__main__":
    app = wx.App()
    frame = Alpha(None, -1, 'Alpha')
    app.MainLoop()
