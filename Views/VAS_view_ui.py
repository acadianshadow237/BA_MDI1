# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VAS_view_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_VAS_Form(QWidget):
    def setupUi(self, VAS_Form):
        if not VAS_Form.objectName():
            VAS_Form.setObjectName(u"VAS_Form")
        VAS_Form.resize(1033, 616)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(VAS_Form.sizePolicy().hasHeightForWidth())
        VAS_Form.setSizePolicy(sizePolicy)
        VAS_Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(VAS_Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.labelCounty = QLabel(VAS_Form)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(VAS_Form)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setMaximumSize(QSize(200, 16777215))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(VAS_Form)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(VAS_Form)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setMaximumSize(QSize(200, 16777215))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(VAS_Form)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(VAS_Form)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(250, 28))
        self.comboBoxDirection.setMaximumSize(QSize(200, 16777215))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.FilterColumncheckBox = QCheckBox(VAS_Form)
        self.FilterColumncheckBox.setObjectName(u"FilterColumncheckBox")
        self.FilterColumncheckBox.setFont(font)

        self.horizontalLayout.addWidget(self.FilterColumncheckBox)

        self.pushButtonReset = QPushButton(VAS_Form)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)

        self.pushButtonEdit = QPushButton(VAS_Form)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonEdit2 = QPushButton(VAS_Form)
        self.pushButtonEdit2.setObjectName(u"pushButtonEdit2")
        self.pushButtonEdit2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonEdit2)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(5, 4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(VAS_Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.VAS_tab = QWidget()
        self.VAS_tab.setObjectName(u"VAS_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VAS_tab.sizePolicy().hasHeightForWidth())
        self.VAS_tab.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.VAS_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.VAS_tableWidget = QTableWidget(self.VAS_tab)
        self.VAS_tableWidget.setObjectName(u"VAS_tableWidget")
        self.VAS_tableWidget.setFont(font)
        self.VAS_tableWidget.setAutoFillBackground(True)
        self.VAS_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}\n"
"QHeaderView::section {font-size: 12 pt;}\n"
"")
        self.VAS_tableWidget.setSortingEnabled(True)

        self.horizontalLayout_3.addWidget(self.VAS_tableWidget)

        self.tabWidget.addTab(self.VAS_tab, "")
        self.VAS_DS_tab = QWidget()
        self.VAS_DS_tab.setObjectName(u"VAS_DS_tab")
        self.verticalLayout_2 = QVBoxLayout(self.VAS_DS_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VAS_DS_tableWidget = QTableWidget(self.VAS_DS_tab)
        self.VAS_DS_tableWidget.setObjectName(u"VAS_DS_tableWidget")
        self.VAS_DS_tableWidget.setFont(font)
        self.VAS_DS_tableWidget.setAutoFillBackground(True)
        self.VAS_DS_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_2.addWidget(self.VAS_DS_tableWidget)

        self.tabWidget.addTab(self.VAS_DS_tab, "")
        self.VAS_DD_tab = QWidget()
        self.VAS_DD_tab.setObjectName(u"VAS_DD_tab")
        self.verticalLayout_3 = QVBoxLayout(self.VAS_DD_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VAS_DD_tableWidget = QTableWidget(self.VAS_DD_tab)
        self.VAS_DD_tableWidget.setObjectName(u"VAS_DD_tableWidget")
        self.VAS_DD_tableWidget.setFont(font)
        self.VAS_DD_tableWidget.setAutoFillBackground(True)
        self.VAS_DD_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_3.addWidget(self.VAS_DD_tableWidget)

        self.tabWidget.addTab(self.VAS_DD_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(VAS_Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VAS_Form)
    # setupUi

    def retranslateUi(self, VAS_Form):
        VAS_Form.setWindowTitle(QCoreApplication.translate("VAS_Form", u"View Analysis Sections ", None))
#if QT_CONFIG(tooltip)
        VAS_Form.setToolTip(QCoreApplication.translate("VAS_Form", u"Clear Data", None))
#endif // QT_CONFIG(tooltip)
        VAS_Form.setProperty("filename", QCoreApplication.translate("VAS_Form", u"VAS", None))
        VAS_Form.setProperty("formname", "")
        self.labelCounty.setText(QCoreApplication.translate("VAS_Form", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("VAS_Form", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("VAS_Form", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("VAS_Form", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("VAS_Form", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("VAS_Form", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("VAS_Form", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("VAS_Form", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("VAS_Form", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.FilterColumncheckBox.setText(QCoreApplication.translate("VAS_Form", u"FilterColumn", None))
        self.pushButtonReset.setText(QCoreApplication.translate("VAS_Form", u"Reset", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("VAS_Form", u"Edit", None))
        self.pushButtonEdit2.setText(QCoreApplication.translate("VAS_Form", u"Edit 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VAS_tab), QCoreApplication.translate("VAS_Form", u"VAS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VAS_DS_tab), QCoreApplication.translate("VAS_Form", u"DS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VAS_DD_tab), QCoreApplication.translate("VAS_Form", u"DD", None))
    # retranslateUi

