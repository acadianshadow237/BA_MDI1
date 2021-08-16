# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VProj_Edit_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_VProj_Edit_Form(QWidget):
    def setupUi(self, VProj_Edit_Form):
        if not VProj_Edit_Form.objectName():
            VProj_Edit_Form.setObjectName(u"VProj_Edit_Form")
        VProj_Edit_Form.resize(1081, 661)
        self.horizontalLayout_3 = QHBoxLayout(VProj_Edit_Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCounty = QLabel(VProj_Edit_Form)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)
        self.labelCounty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(VProj_Edit_Form)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(VProj_Edit_Form)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)
        self.labelRoute.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(VProj_Edit_Form)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(VProj_Edit_Form)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)
        self.labelDirection.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(VProj_Edit_Form)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(300, 28))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.pushButtonReset = QPushButton(VProj_Edit_Form)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonAdd = QPushButton(VProj_Edit_Form)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setMaximumSize(QSize(16777215, 28))
        self.pushButtonAdd.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonAdd)

        self.pushButtonEdit = QPushButton(VProj_Edit_Form)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setMaximumSize(QSize(16777215, 28))
        self.pushButtonEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonEdit)

        self.pushButtonDelete = QPushButton(VProj_Edit_Form)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMaximumSize(QSize(16777215, 28))
        self.pushButtonDelete.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonDelete)

        self.pushButtonClearChanges = QPushButton(VProj_Edit_Form)
        self.pushButtonClearChanges.setObjectName(u"pushButtonClearChanges")
        self.pushButtonClearChanges.setMaximumSize(QSize(16777215, 28))
        self.pushButtonClearChanges.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonClearChanges)

        self.pushButtonApply = QPushButton(VProj_Edit_Form)
        self.pushButtonApply.setObjectName(u"pushButtonApply")
        self.pushButtonApply.setMaximumSize(QSize(16777215, 28))
        self.pushButtonApply.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonApply)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(VProj_Edit_Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(VProj_Edit_Form)

        QMetaObject.connectSlotsByName(VProj_Edit_Form)
    # setupUi

    def retranslateUi(self, VProj_Edit_Form):
        VProj_Edit_Form.setWindowTitle(QCoreApplication.translate("VProj_Edit_Form", u"VProject Edit", None))
        self.labelCounty.setText(QCoreApplication.translate("VProj_Edit_Form", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("VProj_Edit_Form", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("VProj_Edit_Form", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("VProj_Edit_Form", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("VProj_Edit_Form", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("VProj_Edit_Form", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("VProj_Edit_Form", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("VProj_Edit_Form", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("VProj_Edit_Form", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonReset.setText(QCoreApplication.translate("VProj_Edit_Form", u"Reset", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("VProj_Edit_Form", u"Add", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("VProj_Edit_Form", u"Edit", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("VProj_Edit_Form", u"Delete", None))
        self.pushButtonClearChanges.setText(QCoreApplication.translate("VProj_Edit_Form", u"Clear Changes", None))
        self.pushButtonApply.setText(QCoreApplication.translate("VProj_Edit_Form", u"Apply Changes", None))
    # retranslateUi

