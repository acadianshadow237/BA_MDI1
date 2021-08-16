# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VCRH_view_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_VCRH_Form(QWidget):
    def setupUi(self, VCRH_Form):
        if not VCRH_Form.objectName():
            VCRH_Form.setObjectName(u"VCRH_Form")
        VCRH_Form.resize(1195, 755)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(VCRH_Form.sizePolicy().hasHeightForWidth())
        VCRH_Form.setSizePolicy(sizePolicy)
        VCRH_Form.setMinimumSize(QSize(1181, 755))
        self.horizontalLayout_5 = QHBoxLayout(VCRH_Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, -1, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.labelCounty = QLabel(VCRH_Form)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(VCRH_Form)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(VCRH_Form)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(VCRH_Form)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(VCRH_Form)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(VCRH_Form)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(300, 28))

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.pushButtonReset = QPushButton(VCRH_Form)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(VCRH_Form)
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

        self.verticalLayout_4.addWidget(self.Proj_tableWidget)

        self.tabWidget.addTab(self.Project_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(VCRH_Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(VCRH_Form)
    # setupUi

    def retranslateUi(self, VCRH_Form):
        VCRH_Form.setWindowTitle(QCoreApplication.translate("VCRH_Form", u"VCRH Form", None))
#if QT_CONFIG(tooltip)
        VCRH_Form.setToolTip(QCoreApplication.translate("VCRH_Form", u"Clear Data", None))
#endif // QT_CONFIG(tooltip)
        VCRH_Form.setProperty("filename", QCoreApplication.translate("VCRH_Form", u"VAS", None))
        VCRH_Form.setProperty("formname", "")
        self.labelCounty.setText(QCoreApplication.translate("VCRH_Form", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("VCRH_Form", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("VCRH_Form", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("VCRH_Form", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("VCRH_Form", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("VCRH_Form", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonReset.setText(QCoreApplication.translate("VCRH_Form", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.VCRH_tab.setToolTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.VCRH_tab.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VCRH_tab), QCoreApplication.translate("VCRH_Form", u"Const_Rehab_History", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.VCRH_tab), QCoreApplication.translate("VCRH_Form", u"Construction Rehab History", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.VCRLD_tab.setToolTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections DS Only", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.VCRLD_tab.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections DS Only", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VCRLD_tab), QCoreApplication.translate("VCRH_Form", u"Const_Reh_Lay_Detail", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.VCRLD_tab), QCoreApplication.translate("VCRH_Form", u"Construction Rehab Layer Detail", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Project_tab.setToolTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections DD Only", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Project_tab.setStatusTip(QCoreApplication.translate("VCRH_Form", u"Analysis Sections DD Only", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Project_tab), QCoreApplication.translate("VCRH_Form", u"Project", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Project_tab), QCoreApplication.translate("VCRH_Form", u"Project", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

