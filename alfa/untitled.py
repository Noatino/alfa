#######################################################################################
        ### Definition of the elements of the Inverse Compton screen
        #######################################################################################
        self.buttonInvc = wx.Button(Lpanel,11,"Inverse Compton fit Root" ,(10,100))
        StringTextSycn = "Make fit of the Inverse Compton \n scattering"
        wx.StaticText(Lpanel, -1, StringTextSycn, pos = (10,130))
        self.Bind(wx.EVT_BUTTON, self.InvcRoot, id = 11)
        #A0 box parameters
        A0Label_Inv = "A0 parameter"
        self.A0val_InvTextInvc = wx.StaticText(Rpanel, -1, A0Label_Inv, pos=(20,30)) #pos = (x,y)
        self.A0val_InvTextInvc.Show(False)
        self.A0val_Inv = wx.TextCtrl(Rpanel, -1, "AInvc value", pos=(180,30), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixA0_Inv = wx.CheckBox(Rpanel, -1, "Fix A0", pos = (310, 30))        
        A0Label_Inv = "A0 parameter range"
        self.A0val_InvTextInvc = wx.StaticText(Rpanel, -1, A0Label_Inv, pos=(20,60)) #pos = (x,y)
        self.A0val_InvXmin = wx.TextCtrl(Rpanel, -1, "A0 min value", pos=(180,60), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.A0val_InvXmax = wx.TextCtrl(Rpanel, -1, "A0 max value", pos=(310,60), size=(100,25), style=wx.TE_PROCESS_ENTER)
        #alfa box parameters
        alfaLabel_Inv = "Alfa parameter"
        self.alfaval_InvTextInvc = wx.StaticText(Rpanel, -1, alfaLabel_Inv, pos=(20,90)) #pos = (x,y)
        self.alfaval_InvTextInvc.Show(False)
        self.alfaval_Inv = wx.TextCtrl(Rpanel, -1, "Alfa value", pos=(180,90), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixalfa_Inv = wx.CheckBox(Rpanel, -1, "Fix Alfa", pos = (310, 90))
        alfaLabel_Inv = "Alfa parameter range"
        self.alfaval_InvTextInvc = wx.StaticText(Rpanel, -1, alfaLabel_Inv, pos=(20,120)) #pos = (x,y)
        self.alfaval_InvXmin = wx.TextCtrl(Rpanel, -1, "Alfa min value", pos=(180,120), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.alfaval_InvXmax = wx.TextCtrl(Rpanel, -1, "Alfa max value", pos=(310,120), size=(100,25), style=wx.TE_PROCESS_ENTER)
        #Emin box parameters
        EminLabel = "Emin parameter"
        self.Eminval_InvTextInvc = wx.StaticText(Rpanel, -1, EminLabel, pos=(20,150)) #pos = (x,y)
        self.Eminval_InvTextInvc.Show(False)
        self.Eminval_Inv = wx.TextCtrl(Rpanel, -1, "Emin value", pos=(180,150), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixEmin_Inv = wx.CheckBox(Rpanel, -1, "Fix Emin", pos = (310, 150))
        EminLabel = "Emin parameter range"
        self.Eminval_InvTextInvc = wx.StaticText(Rpanel, -1, EminLabel, pos=(20,180)) #pos = (x,y)
        self.Eminval_InvXmin_Inv = wx.TextCtrl(Rpanel, -1, "Emin min value", pos=(180,180), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.Eminval_InvXmax_Inv = wx.TextCtrl(Rpanel, -1, "Emin max value", pos=(310,180), size=(100,25), style=wx.TE_PROCESS_ENTER)
        #Ecut box parameters
        EcutLabel_Inv = "Ecut parameter"
        self.Ecutval_InvTextInvc = wx.StaticText(Rpanel, -1, EcutLabel_Inv, pos=(20,210)) #pos = (x,y)
        self.Ecutval_InvTextInvc.Show(False)
        self.Ecutval_Inv = wx.TextCtrl(Rpanel, -1, "Ecut value", pos=(180,210), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.fixEcut_Inv = wx.CheckBox(Rpanel, -1, "Fix Ecut", pos = (310, 210))
        EcutLabel_Inv = "Ecut parameter range"
        self.Ecutval_InvTextInvc = wx.StaticText(Rpanel, -1, EcutLabel_Inv, pos=(20,240)) #pos = (x,y)
        self.Ecutval_InvXmin = wx.TextCtrl(Rpanel, -1, "Ecut min value", pos=(180,240), size=(100,25), style=wx.TE_PROCESS_ENTER)
        self.Ecutval_InvXmax = wx.TextCtrl(Rpanel, -1, "Ecut max value", pos=(310,240), size=(100,25), style=wx.TE_PROCESS_ENTER)
        #Fit button
        self.buttonChargeSVal_Inv = wx.Button(Rpanel,16, "Fit", (600,390))
        self.Bind(wx.EVT_BUTTON, self.getValues_fit_Invc, id = 17)
        ########################################################################################
        ### Now I will disapear all the elements of this screen
        ########################################################################################
        self.A0val_InvTextInvc.Show(False)
        self.alfaval_InvTextInvc.Show(False)
        self.Eminval_InvTextInvc.Show(False)
        self.Ecutval_InvTextInvc.Show(False)
        #---
        self.A0val_InvTextInvc.Show(False)
        self.A0val_Inv.Show(False)
        self.fixA0_Inv.Show(False)
        self.A0val_InvTextInvc.Show(False)
        self.A0val_InvXmin.Show(False)
        self.A0val_InvXmax.Show(False)
        self.alfaval_InvTextInvc.Show(False)
        self.alfaval_Inv.Show(False)
        self.fixalfa_Inv.Show(False)
        self.alfaval_InvTextInvc.Show(False)
        self.alfaval_InvXmin.Show(False)
        self.alfaval_InvXmax.Show(False)
        self.Eminval_InvTextInvc.Show(False)
        self.Eminval_Inv.Show(False)
        self.fixEmin_Inv.Show(False)
        self.Eminval_InvTextInvc.Show(False)
        self.Eminval_InvXmin_Inv.Show(False)
        self.Eminval_InvXmax_Inv.Show(False)
        self.Ecutval_InvTextInvc.Show(False)
        self.Ecutval_Inv.Show(False)
        self.fixEcut_Inv.Show(False)
        self.Ecutval_InvTextInvc.Show(False)
        self.Ecutval_InvXmin.Show(False)
        self.Ecutval_InvXmax.Show(False)
        self.buttonChargeSVal_Inv.Show(False)
        #--