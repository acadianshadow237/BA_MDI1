# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VCRHVCRLDVPROJ_view_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_VCRHVCRLDVPROJ_Form(QWidget):
    def setupUi(self, VCRHVCRLDVPROJ_Form):
        if not VCRHVCRLDVPROJ_Form.objectName():
            VCRHVCRLDVPROJ_Form.setObjectName(u"VCRHVCRLDVPROJ_Form")
        VCRHVCRLDVPROJ_Form.resize(983, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VCRHVCRLDVPROJ_Form.sizePolicy().hasHeightForWidth())
        VCRHVCRLDVPROJ_Form.setSizePolicy(sizePolicy)
        VCRHVCRLDVPROJ_Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(VCRHVCRLDVPROJ_Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.labelCounty = QLabel(VCRHVCRLDVPROJ_Form)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(VCRHVCRLDVPROJ_Form)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(VCRHVCRLDVPROJ_Form)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(VCRHVCRLDVPROJ_Form)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(VCRHVCRLDVPROJ_Form)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(VCRHVCRLDVPROJ_Form)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(300, 28))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.pushButtonReset = QPushButton(VCRHVCRLDVPROJ_Form)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)

        self.pushButtonEdit = QPushButton(VCRHVCRLDVPROJ_Form)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        sizePolicy.setHeightForWidth(self.pushButtonEdit.sizePolicy().hasHeightForWidth())
        self.pushButtonEdit.setSizePolicy(sizePolicy)
        self.pushButtonEdit.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(VCRHVCRLDVPROJ_Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setFont(font)
        self.VCRH_tab = QWidget()
        self.VCRH_tab.setObjectName(u"VCRH_tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VCRH_tab.sizePolicy().hasHeightForWidth())
        self.VCRH_tab.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.VCRH_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VCRH_tableWidget = QTableWidget(self.VCRH_tab)
        self.VCRH_tableWidget.setObjectName(u"VCRH_tableWidget")
        self.VCRH_tableWidget.setFont(font)
        self.VCRH_tableWidget.setAutoFillBackground(True)
        self.VCRH_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_2.addWidget(self.VCRH_tableWidget)

        self.tabWidget.addTab(self.VCRH_tab, "")
        self.VCRLD_tab = QWidget()
        self.VCRLD_tab.setObjectName(u"VCRLD_tab")
        sizePolicy2.setHeightForWidth(self.VCRLD_tab.sizePolicy().hasHeightForWidth())
        self.VCRLD_tab.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.VCRLD_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VCRLD_tableWidget = QTableWidget(self.VCRLD_tab)
        self.VCRLD_tableWidget.setObjectName(u"VCRLD_tableWidget")
        self.VCRLD_tableWidget.setFont(font)
        self.VCRLD_tableWidget.setAutoFillBackground(True)
        self.VCRLD_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_3.addWidget(self.VCRLD_tableWidget)

        self.tabWidget.addTab(self.VCRLD_tab, "")
        self.Project_tab = QWidget()
        self.Project_tab.setObjectName(u"Project_tab")
        sizePolicy2.setHeightForWidth(self.Project_tab.sizePolicy().hasHeightForWidth())
        self.Project_tab.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.Project_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Proj_tableWidget = QTableWidget(self.Project_tab)
        self.Proj_tableWidget.setObjectName(u"Proj_tableWidget")
        self.Proj_tableWidget.setFont(font)
        self.Proj_tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_4.addWidget(self.Proj_tableWidget)

        self.tabWidget.addTab(self.Project_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(VCRHVCRLDVPROJ_Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VCRHVCRLDVPROJ_Form)
    # setupUi

    def retranslateUi(self, VCRHVCRLDVPROJ_Form):
        VCRHVCRLDVPROJ_Form.setWindowTitle(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"VCRH -VCRLD - VPROJECT", None))
#if QT_CONFIG(tooltip)
        VCRHVCRLDVPROJ_Form.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Clear Data", None))
#endif // QT_CONFIG(tooltip)
        VCRHVCRLDVPROJ_Form.setProperty("filename", QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"VAS", None))
        VCRHVCRLDVPROJ_Form.setProperty("formname", "")
        self.labelCounty.setText(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonReset.setText(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Reset", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.VCRH_tab.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.VCRH_tab.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VCRH_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Const_Rehab_History", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.VCRH_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Construction Rehab History", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.VCRLD_tab.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections DS Only", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.VCRLD_tab.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections DS Only", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VCRLD_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Const_Reh_Lay_Detail", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.VCRLD_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Construction Rehab Layer Detail", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Project_tab.setToolTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections DD Only", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Project_tab.setStatusTip(QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Analysis Sections DD Only", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Project_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Project", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Project_tab), QCoreApplication.translate("VCRHVCRLDVPROJ_Form", u"Project", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

