
from PySide6.QtCore import (Qt,QCoreApplication, QRect, QMetaObject)
from PySide6.QtGui import (QAction,QKeySequence, QFont)
from PySide6.QtWidgets import ( QStatusBar, QMenuBar,  QMenu, QToolBar)  # type: ignore

def menu_cascade(my_self1):
    
    if my_self1.login_flag == False:
        login_menu(my_self1)
    else:    
        menu_analysis_sections(my_self1)
    #analysis_section_menu
        #if my_self1.document_type == 1:
        #    menu_analysis_sections(my_self1)
        #    pass
        #elif my_self1.document_type == 2:
        #    menu_VCRH(my_self1)
        #    pass
     
def login_menu(my_self):
        # Action to quit the application.
    font = QFont()
    font.setPointSize(12)  
    my_self.actionLogin = QAction()
    my_self.actionLogin.setFont(font)
    my_self.actionLogin.setObjectName(u"actionLogin")
    my_self.actionExit = QAction()
    my_self.actionExit.setFont(font) 
    my_self.actionExit.setObjectName(u"actionExit")
    my_self.actionContents = QAction()
    my_self.actionContents.setFont(font)
    my_self.actionContents.setObjectName(u"actionContents")
    my_self.actionAbout = QAction()
    my_self.actionAbout.setFont(font)
    my_self.actionAbout.setObjectName(u"actionAbout")       

    my_self.menubar = QMenuBar()
    my_self.menubar.setObjectName(u"menubar")
    my_self.menubar.setGeometry(QRect(0, 0, 1200, 22))
    my_self.menuFile = QMenu(my_self.menubar)
    my_self.menuFile.setObjectName(u"menuFile")
    my_self.menuHelp = QMenu(my_self.menubar)
    my_self.menuHelp.setObjectName(u"menuHelp")
       
    my_self.setMenuBar(my_self.menubar)

 
    my_self.menubar.setFont(font)

    my_self.menubar.addAction(my_self.menuFile.menuAction())
    my_self.menubar.addAction(my_self.menuHelp.menuAction())
    my_self.menuFile.addAction(my_self.actionLogin)
    my_self.menuFile.addSeparator()
    my_self.menuFile.addAction(my_self.actionExit)
    my_self.menuHelp.addAction(my_self.actionContents)
    my_self.menuHelp.addSeparator()
    my_self.menuHelp.addAction(my_self.actionAbout)

    my_self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
    my_self.actionLogin.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
    my_self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
    my_self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
    my_self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
    my_self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
    my_self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    my_self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))


    my_self.actionLogin.triggered.connect(my_self.onLogin)
    my_self.actionExit.triggered.connect(my_self.onExit)
    my_self.actionContents.triggered.connect(my_self.onContents)
    my_self.actionAbout.triggered.connect(my_self.onAbout)

   
    #"""Create status bar and content."""
    my_self.statusBar = QStatusBar()
    my_self.statusBar.setObjectName(u"statusBar")
    my_self.setStatusBar(my_self.statusBar)
   

#def menu_analysis_sections2(self):

#    self.actionExit = QAction(self)
#    self.actionExit.setObjectName(u"actionExit")
#    self.actionLogout = QAction(self)
#    self.actionLogout.setObjectName(u"actionLogout")
#    self.actionAnalysis_Sections = QAction(self)
#    self.actionAnalysis_Sections.setObjectName(u"actionAnalysis_Sections")
#    self.actionConstruction_Rehab_History = QAction(self)
#    self.actionConstruction_Rehab_History.setObjectName(u"actionConstruction_Rehab_History")
#    self.actionConst_Rehab_Layer_Detail = QAction(self)
#    self.actionConst_Rehab_Layer_Detail.setObjectName(u"actionConst_Rehab_Layer_Detail")
#    self.actionProject = QAction(self)
#    self.actionProject.setObjectName(u"actionProject")
#    self.actionAbout = QAction(self)
#    self.actionAbout.setObjectName(u"actionAbout")
#    self.actionsplit = QAction(self)
#    self.actionsplit.setObjectName(u"actionsplit")
#    self.actionContents = QAction(self)
#    self.actionContents.setObjectName(u"actionContents")
#    self.actionVCRH_VCRLD_VPROJ = QAction(self)
#    self.actionVCRH_VCRLD_VPROJ.setObjectName(u"actionVCRH_VCRLD_VPROJ")
#    self.actionEdit_Layers = QAction(self)
#    self.actionEdit_Layers.setObjectName(u"actionEdit_Layers")

#    font = QFont()
#    font.setPointSize(12) 

#    self.menubar = QMenuBar()
#    self.menubar.setObjectName(u"menubar")
#    self.menubar.setFont(font)

#    self.menubar.setGeometry(QRect(0, 0, 1253, 22))
#    self.menuFile = QMenu(self.menubar)
#    self.menuFile.setObjectName(u"menuFile")
#    self.menuView = QMenu(self.menubar)
#    self.menuView.setObjectName(u"menuView")
#    self.menuHelp = QMenu(self.menubar)
#    self.menuHelp.setObjectName(u"menuHelp")
#    self.setMenuBar(self.menubar)

#    self.menubar.addAction(self.menuFile.menuAction())
#    self.menubar.addAction(self.menuView.menuAction())
#    self.menubar.addAction(self.menuHelp.menuAction())
#    self.menuFile.addAction(self.actionLogout)
#    self.menuFile.addSeparator()
#    self.menuFile.addAction(self.actionExit)
#    self.menuView.addAction(self.actionAnalysis_Sections)
#    self.menuView.addAction(self.actionVCRH_VCRLD_VPROJ)
#    self.menuView.addAction(self.actionConstruction_Rehab_History)
#    self.menuView.addAction(self.actionConst_Rehab_Layer_Detail)
#    self.menuView.addAction(self.actionProject)
#    self.menuView.addSeparator()
#    self.menuView.addAction(self.actionEdit_Layers)
#    self.menuHelp.addAction(self.actionContents)
#    self.menuHelp.addSeparator()
#    self.menuHelp.addAction(self.actionAbout)

#    self.actionLogout.triggered.connect(self.onLogout)
#    self.actionExit.triggered.connect(self.onQuit)
#    self.actionContents.triggered.connect(self.onContents)
#    self.actionAbout.triggered.connect(self.onAbout)

#    self.actionLogout.triggered.connect(self.onLogout)
#    self.actionAnalysis_Sections.triggered.connect(self.onVAS)
#    self.actionConstruction_Rehab_History.triggered.connect(self.onVCRH)
#    self.actionConst_Rehab_Layer_Detail.triggered.connect(self.onVCRLD)
#    self.actionProject.triggered.connect(self.onVPRJ)
#    self.actionEdit_Layers.triggered.connect(self.onEditLayers)
#    self.actionVCRH_VCRLD_VPROJ.triggered.connect(self.onVCRHVCRLDVPROJ)

#    QMetaObject.connectSlotsByName(self)
## setupUi


#    self.setWindowTitle(QCoreApplication.translate("MainWindow", u"PVMT_SNAP editor", None))
#    self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#    self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#    self.actionAnalysis_Sections.setText(QCoreApplication.translate("MainWindow", u"Analysis Sections", None))
#    self.actionConstruction_Rehab_History.setText(QCoreApplication.translate("MainWindow", u"Construction Rehab History", None))
#    self.actionConst_Rehab_Layer_Detail.setText(QCoreApplication.translate("MainWindow", u"Const Rehab Layer Detail", None))
#    self.actionProject.setText(QCoreApplication.translate("MainWindow", u"Project", None))
#    self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#    self.actionsplit.setText(QCoreApplication.translate("MainWindow", u"Split", None))
#    self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#    self.actionVCRH_VCRLD_VPROJ.setText(QCoreApplication.translate("MainWindow", u"VCRH_VCRLD_VPROJ", None))
#    self.actionEdit_Layers.setText(QCoreApplication.translate("MainWindow", u"Edit Layers", None))
#    self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
#    self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
#    self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
#    pass



def menu_analysis_sections(self):
    self.actionExit = QAction(self)
    self.actionExit.setObjectName(u"actionExit")
    font = QFont()
    font.setPointSize(12)
    self.actionExit.setFont(font)
    self.actionLogout = QAction(self)
    self.actionLogout.setObjectName(u"actionLogout")
    self.actionLogout.setFont(font)
    self.actionAnalysis_Sections = QAction(self)
    self.actionAnalysis_Sections.setObjectName(u"actionAnalysis_Sections")
    self.actionAnalysis_Sections.setFont(font)
    self.actionConstruction_Rehab_History = QAction(self)
    self.actionConstruction_Rehab_History.setObjectName(u"actionConstruction_Rehab_History")
    self.actionConstruction_Rehab_History.setFont(font)
    self.actionConst_Rehab_Layer_Detail = QAction(self)
    self.actionConst_Rehab_Layer_Detail.setObjectName(u"actionConst_Rehab_Layer_Detail")
    self.actionConst_Rehab_Layer_Detail.setFont(font)
    self.actionProject = QAction(self)
    self.actionProject.setObjectName(u"actionProject")
    self.actionProject.setFont(font)
    self.actionAbout = QAction(self)
    self.actionAbout.setObjectName(u"actionAbout")
    self.actionAbout.setFont(font)
    self.actionContents = QAction(self)
    self.actionContents.setObjectName(u"actionContents")
    self.actionContents.setFont(font)
    self.actionVCRH_VCRLD_VPROJ = QAction(self)
    self.actionVCRH_VCRLD_VPROJ.setObjectName(u"actionVCRH_VCRLD_VPROJ")
    self.actionVCRH_VCRLD_VPROJ.setFont(font)
    self.actionSplit_Section = QAction(self)
    self.actionSplit_Section.setObjectName(u"actionSplit_Section")
    self.actionSplit_Section.setFont(font)
    self.actionTweak_Section = QAction(self)
    self.actionTweak_Section.setObjectName(u"actionTweak_Section")
    self.actionTweak_Section.setFont(font)
    self.actionMove_Section = QAction(self)
    self.actionMove_Section.setObjectName(u"actionMove_Section")
    self.actionMove_Section.setFont(font)
    self.actionCopy_Section = QAction(self)
    self.actionCopy_Section.setObjectName(u"actionCopy_Section")
    self.actionCopy_Section.setFont(font)
    self.actionLog = QAction(self)
    self.actionLog.setObjectName(u"actionLog")
    self.actionLog.setFont(font)
    self.actionNew_Project = QAction(self)
    self.actionNew_Project.setObjectName(u"actionNew_Project")
    self.actionNew_Project.setFont(font)
    self.actionRename_Project = QAction(self)
    self.actionRename_Project.setObjectName(u"actionRename_Project")
    self.actionRename_Project.setFont(font)
    self.actionCopy_Project = QAction(self)
    self.actionCopy_Project.setObjectName(u"actionCopy_Project")
    self.actionCopy_Project.setFont(font)
    self.actionPlace_Construction = QAction(self)
    self.actionPlace_Construction.setObjectName(u"actionPlace_Construction")
    self.actionPlace_Construction.setFont(font)
 
    self.menubar = QMenuBar(self)
    self.menubar.setObjectName(u"menubar")
    self.menubar.setGeometry(QRect(0, 0, 1253, 28))
    self.menubar.setFont(font)
    self.menuFile = QMenu(self.menubar)
    self.menuFile.setObjectName(u"menuFile")
    self.menuView = QMenu(self.menubar)
    self.menuView.setObjectName(u"menuView")
    self.menuHelp = QMenu(self.menubar)
    self.menuHelp.setObjectName(u"menuHelp")
    self.menuEdit = QMenu(self.menubar)
    self.menuEdit.setObjectName(u"menuEdit")
    self.menuProjects = QMenu(self.menubar)
    self.menuProjects.setObjectName(u"menuProjects")
    self.setMenuBar(self.menubar)

    self.menubar.addAction(self.menuFile.menuAction())
    self.menubar.addAction(self.menuView.menuAction())
    self.menubar.addAction(self.menuProjects.menuAction())
    self.menubar.addAction(self.menuEdit.menuAction())
    self.menubar.addAction(self.menuHelp.menuAction())
    self.menuFile.addAction(self.actionLogout)
    self.menuFile.addSeparator()
    self.menuFile.addAction(self.actionExit)
    self.menuView.addAction(self.actionAnalysis_Sections)
    self.menuView.addAction(self.actionVCRH_VCRLD_VPROJ)
    self.menuView.addAction(self.actionConstruction_Rehab_History)
    self.menuView.addAction(self.actionConst_Rehab_Layer_Detail)
    self.menuView.addAction(self.actionProject)
    self.menuView.addSeparator()
    self.menuView.addAction(self.actionLog)
    self.menuHelp.addAction(self.actionContents)
    self.menuHelp.addSeparator()
    self.menuHelp.addAction(self.actionAbout)
    self.menuEdit.addAction(self.actionSplit_Section)
    self.menuEdit.addAction(self.actionTweak_Section)
    self.menuEdit.addAction(self.actionMove_Section)
    self.menuEdit.addAction(self.actionCopy_Section)
    self.menuEdit.addSeparator()
    self.menuProjects.addAction(self.actionNew_Project)
    self.menuProjects.addAction(self.actionRename_Project)
    self.menuProjects.addAction(self.actionCopy_Project)
    self.menuProjects.addAction(self.actionPlace_Construction)

    
  ## File Menu Area 
    self.actionExit.triggered.connect(self.onExit)
    self.actionLogout.triggered.connect(self.onLogout)
    self.actionContents.triggered.connect(self.onContents)
    self.actionAbout.triggered.connect(self.onAbout)
    

   ## view menu area
    self.actionAnalysis_Sections.triggered.connect(self.onVAS)
    self.actionVCRH_VCRLD_VPROJ.triggered.connect(self.onVCRHVCRLDVPROJ)
    self.actionConstruction_Rehab_History.triggered.connect(self.onVCRH)
    self.actionConst_Rehab_Layer_Detail.triggered.connect(self.onVCRLD)
    self.actionProject.triggered.connect(self.onVPRJ)
    self.actionLog.triggered.connect(self.onLog)

   # Project Menu Area
    self.actionNew_Project.triggered.connect(self.onNewProject)
    self.actionRename_Project.triggered.connect(self.onRenameProject)
    self.actionCopy_Project.triggered.connect(self.onCopyProject)
    self.actionPlace_Construction.triggered.connect(self.onEditLayers)
   
    # Edit Menu Section
    self.actionSplit_Section.triggered.connect(self.onSplitSection)
    self.actionTweak_Section.triggered.connect(self.onTweakSection)
    self.actionMove_Section.triggered.connect(self.onMoveSection)
    self.actionCopy_Section.triggered.connect(self.onCopySection)

    QMetaObject.connectSlotsByName(self)
# setupUi


    self.setWindowTitle(QCoreApplication.translate("MainWindow", u"PVMT_SNAP editor", None))
    self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    self.actionAnalysis_Sections.setText(QCoreApplication.translate("MainWindow", u"Analysis Sections", None))
    self.actionConstruction_Rehab_History.setText(QCoreApplication.translate("MainWindow", u"Construction Rehab History", None))
    self.actionConst_Rehab_Layer_Detail.setText(QCoreApplication.translate("MainWindow", u"Const Rehab Layer Detail", None))
    self.actionProject.setText(QCoreApplication.translate("MainWindow", u"Project", None))
    self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
    self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
    self.actionVCRH_VCRLD_VPROJ.setText(QCoreApplication.translate("MainWindow", u"VCRH_VCRLD_VPROJ", None))
    self.actionSplit_Section.setText(QCoreApplication.translate("MainWindow", u"Split Section", None))
    self.actionTweak_Section.setText(QCoreApplication.translate("MainWindow", u"Tweak Section", None))
    self.actionMove_Section.setText(QCoreApplication.translate("MainWindow", u"Move Section", None))
    self.actionCopy_Section.setText(QCoreApplication.translate("MainWindow", u"Copy Section", None))
    self.actionLog.setText(QCoreApplication.translate("MainWindow", u"Log", None))
    self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
    self.actionRename_Project.setText(QCoreApplication.translate("MainWindow", u"Rename Project", None))
    self.actionCopy_Project.setText(QCoreApplication.translate("MainWindow", u"Copy Project", None))
    self.actionPlace_Construction.setText(QCoreApplication.translate("MainWindow", u"Place Construction", None))
    self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    self.menuProjects.setTitle(QCoreApplication.translate("MainWindow", u"Projects", None))
# retranslateUi




    

 