# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_edit_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DialogSimpleEdit(QDialog):
    def setupUi(self, DialogSimpleEdit):
        if not DialogSimpleEdit.objectName():
            DialogSimpleEdit.setObjectName(u"DialogSimpleEdit")
        DialogSimpleEdit.resize(500, 604)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSimpleEdit.sizePolicy().hasHeightForWidth())
        DialogSimpleEdit.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(DialogSimpleEdit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(DialogSimpleEdit)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEditFieldName = QLineEdit(DialogSimpleEdit)
        self.lineEditFieldName.setObjectName(u"lineEditFieldName")
        self.lineEditFieldName.setMinimumSize(QSize(0, 35))
        self.lineEditFieldName.setFont(font)
        self.lineEditFieldName.setMaxLength(50)
        self.lineEditFieldName.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditFieldName)

        self.label_2 = QLabel(DialogSimpleEdit)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEditFieldCurrentValue = QLineEdit(DialogSimpleEdit)
        self.lineEditFieldCurrentValue.setObjectName(u"lineEditFieldCurrentValue")
        self.lineEditFieldCurrentValue.setMinimumSize(QSize(0, 35))
        self.lineEditFieldCurrentValue.setFont(font)
        self.lineEditFieldCurrentValue.setMaxLength(50)
        self.lineEditFieldCurrentValue.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditFieldCurrentValue)

        self.label_3 = QLabel(DialogSimpleEdit)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.lineEditFieldNewValue = QLineEdit(DialogSimpleEdit)
        self.lineEditFieldNewValue.setObjectName(u"lineEditFieldNewValue")
        self.lineEditFieldNewValue.setMinimumSize(QSize(0, 35))
        self.lineEditFieldNewValue.setFont(font)
        self.lineEditFieldNewValue.setMaxLength(50)

        self.verticalLayout.addWidget(self.lineEditFieldNewValue)

        self.label_4 = QLabel(DialogSimpleEdit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.tableWidget = QTableWidget(DialogSimpleEdit)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.label_5 = QLabel(DialogSimpleEdit)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.lineEditAssList = QLineEdit(DialogSimpleEdit)
        self.lineEditAssList.setObjectName(u"lineEditAssList")
        self.lineEditAssList.setMinimumSize(QSize(0, 35))
        self.lineEditAssList.setFont(font)
        self.lineEditAssList.setMaxLength(50)
        self.lineEditAssList.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditAssList)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonSave = QPushButton(DialogSimpleEdit)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonSave)

        self.pushButtonCancel = QPushButton(DialogSimpleEdit)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(DialogSimpleEdit)
        self.pushButtonCancel.clicked.connect(DialogSimpleEdit.close)

        QMetaObject.connectSlotsByName(DialogSimpleEdit)
    # setupUi

    def retranslateUi(self, DialogSimpleEdit):
        DialogSimpleEdit.setWindowTitle(QCoreApplication.translate("DialogSimpleEdit", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogSimpleEdit", u"<html><head/><body><p align=\"center\">Field Being Edited</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("DialogSimpleEdit", u"<html><head/><body><p align=\"center\">Current Value</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DialogSimpleEdit", u"<html><head/><body><p align=\"center\">New Value</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DialogSimpleEdit", u"<html><head/><body><p align=\"center\">Possible Values</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DialogSimpleEdit", u"<html><head/><body><p align=\"center\">Associated Values</p></body></html>", None))
        self.pushButtonSave.setText(QCoreApplication.translate("DialogSimpleEdit", u"Save", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("DialogSimpleEdit", u"Cancel", None))
    # retranslateUi

