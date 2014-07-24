#! /usr/bin/python
# -*- coding: utf-8 _*_
#Alpha

######################################################
####    Alfa program to make something in GRB     ####
#### Antonio Galvan, Nissim Fraija, Uriel Luviano ####
####Python 2.7, wxPython (classic) 3.0.0.0, pyRoot####
######################################################


#We make sure that all the modules are correct import for the
#use of the program.
try:
    import wx
    from  ProgramWindow import ProgramWindow
except ImportError:
    errorMessage = "Please, check all the dependences for alpha"
    raise ImportError,errorMessage


#Now we define the main class of the program
class Alfa(wx.Frame):

    CTR = False #A flag to continue to the pyRootSection
    paths = []  #Here we store the paths of the files

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.parent = parent
        self.initialize()

        ###########################################
        # We define the inicialize of the program #
        ###########################################

    def initialize(self):
        '''
        Initialize the main window of Alpha
        '''



        #A grid to make more easier the desing of the template
        grilla = wx.GridBagSizer()

        #Welcome labels
        welcome = '\t Welcome to Alpha\t'
        secondLine = 'Please, select the files .dat of you experiments:  \t'

        #Define, show and propieties of the labels text
        self.etiqueta = wx.StaticText(self, -1, label=welcome)
        self.etiqueta2 = wx.StaticText(self, -1, label=secondLine)
        self.blank = wx.StaticText(self, -1, label='\t \t')
        self.etiqueta.SetForegroundColour(wx.BLACK)
        grilla.Add(self.blank, (8,8),(9,10), wx.EXPAND)
        grilla.Add(self.etiqueta2, (3,3),(4,4), wx.EXPAND)
        grilla.Add(self.etiqueta, (2,2),(3,3), wx.EXPAND)

        #Button of select files, and configure it
        button = wx.Button(self,-1,label = 'Select files')
        grilla.Add(button,(7,3))
        button.Bind(wx.EVT_BUTTON, self.SelectFilesButton)
        
        if Alfa.CTR == True:
            print True


        #The growable column of the grid, show an fit.
        grilla.AddGrowableCol(0)
        self.SetSizerAndFit(grilla)
        self.Show(True)
        
        ############################################################
        # Now we going to define the select button for the program #
        ############################################################

    def SelectFilesButton(self, event):            
         '''
         Create and show the file dialog to select the data files
         of the experiments, and return the paths, in this button
         we will call the new window of the program
         '''

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
             paths = dialog.GetPaths()
             fc = ''
             for x in paths:
                 fc = fc+'\n'+x+'\n'
             dial = wx.MessageDialog(None, fc, 'Are you sure to select this files?', wx.YES_NO
                                     |wx.ICON_QUESTION)
             elec = dial.ShowModal()
             if elec == wx.ID_YES:

                 ##########################################################################
                 ######## Here put the code of the change window to use all the ###########
                 ########                       to work on pyRoot               ###########
                 ##########################################################################
                 
                 windowCalled = ProgramWindow(self)
                 windowCalled.windowFather = self
                 windowCalled.windowFather.Hide()
                 windowCalled.Show()

             if elec == wx.ID_NO:
                 dial2 = wx.MessageDialog(None, "Please, chosse your files again.", "", wx.OK
                                     |wx.ICON_INFORMATION)
                 result = dial2.ShowModal() == wx.OK

         dialog.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = Alfa(None, -1,'Alpha')
    app.MainLoop()
