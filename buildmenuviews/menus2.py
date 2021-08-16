# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menus2.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1253, 866)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionAnalysis_Sections = QAction(MainWindow)
        self.actionAnalysis_Sections.setObjectName(u"actionAnalysis_Sections")
        self.actionConstruction_Rehab_History = QAction(MainWindow)
        self.actionConstruction_Rehab_History.setObjectName(u"actionConstruction_Rehab_History")
        self.actionConst_Rehab_Layer_Detail = QAction(MainWindow)
        self.actionConst_Rehab_Layer_Detail.setObjectName(u"actionConst_Rehab_Layer_Detail")
        self.actionProject = QAction(MainWindow)
        self.actionProject.setObjectName(u"actionProject")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionsplit = QAction(MainWindow)
        self.actionsplit.setObjectName(u"actionsplit")
        self.actionShift = QAction(MainWindow)
        self.actionShift.setObjectName(u"actionShift")
        self.actionMerge = QAction(MainWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        self.actionAdjust = QAction(MainWindow)
        self.actionAdjust.setObjectName(u"actionAdjust")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1253, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = TBAS(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionAnalysis_Sections)
        self.menuView.addAction(self.actionConstruction_Rehab_History)
        self.menuView.addAction(self.actionConst_Rehab_Layer_Detail)
        self.menuView.addAction(self.actionProject)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionUpdate)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionsplit)
        self.menuEdit.addAction(self.actionShift)
        self.menuEdit.addAction(self.actionMerge)
        self.menuEdit.addAction(self.actionAdjust)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PVMT_SNAP editor", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionAnalysis_Sections.setText(QCoreApplication.translate("MainWindow", u"Analysis Sections", None))
        self.actionConstruction_Rehab_History.setText(QCoreApplication.translate("MainWindow", u"Construction Rehab History", None))
        self.actionConst_Rehab_Layer_Detail.setText(QCoreApplication.translate("MainWindow", u"Const Rehab Layer Detail", None))
        self.actionProject.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionsplit.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.actionShift.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.actionMerge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.actionAdjust.setText(QCoreApplication.translate("MainWindow", u"Adjust", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

