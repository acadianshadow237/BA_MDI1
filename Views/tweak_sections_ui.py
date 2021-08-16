# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tweak_sections_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DialogTweakSections(QWidget):
    def setupUi(self, DialogTweakSections):
        if not DialogTweakSections.objectName():
            DialogTweakSections.setObjectName(u"DialogTweakSections")
        DialogTweakSections.resize(1113, 495)
        font = QFont()
        font.setPointSize(12)
        DialogTweakSections.setFont(font)
        self.verticalLayout = QVBoxLayout(DialogTweakSections)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCounty = QLabel(DialogTweakSections)
        self.labelCounty.setObjectName(u"labelCounty")
        self.labelCounty.setFont(font)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(DialogTweakSections)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setMaximumSize(QSize(200, 16777215))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(DialogTweakSections)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(DialogTweakSections)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setMaximumSize(QSize(200, 16777215))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(DialogTweakSections)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(DialogTweakSections)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(250, 35))
        self.comboBoxDirection.setMaximumSize(QSize(200, 16777215))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.FilterColumncheckBox = QCheckBox(DialogTweakSections)
        self.FilterColumncheckBox.setObjectName(u"FilterColumncheckBox")
        self.FilterColumncheckBox.setFont(font)

        self.horizontalLayout.addWidget(self.FilterColumncheckBox)

        self.pushButtonReset = QPushButton(DialogTweakSections)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(DialogTweakSections)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(DialogTweakSections)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.textEditFrom = QTextEdit(DialogTweakSections)
        self.textEditFrom.setObjectName(u"textEditFrom")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditFrom.sizePolicy().hasHeightForWidth())
        self.textEditFrom.setSizePolicy(sizePolicy)
        self.textEditFrom.setMinimumSize(QSize(0, 35))
        self.textEditFrom.setMaximumSize(QSize(16777215, 28))
        self.textEditFrom.setFont(font)
        self.textEditFrom.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEditFrom)

        self.label_2 = QLabel(DialogTweakSections)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.textEditTo = QTextEdit(DialogTweakSections)
        self.textEditTo.setObjectName(u"textEditTo")
        sizePolicy.setHeightForWidth(self.textEditTo.sizePolicy().hasHeightForWidth())
        self.textEditTo.setSizePolicy(sizePolicy)
        self.textEditTo.setMinimumSize(QSize(0, 35))
        self.textEditTo.setMaximumSize(QSize(16777215, 28))
        self.textEditTo.setFont(font)
        self.textEditTo.setLayoutDirection(Qt.RightToLeft)
        self.textEditTo.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEditTo)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 20)
        self.horizontalLayout_2.setStretch(3, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label_3 = QLabel(DialogTweakSections)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit = QLineEdit(DialogTweakSections)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaxLength(7)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.label_4 = QLabel(DialogTweakSections)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(DialogTweakSections)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setMaxLength(7)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_4.setStretch(0, 20)
        self.horizontalLayout_4.setStretch(2, 20)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButtonTweak = QPushButton(DialogTweakSections)
        self.pushButtonTweak.setObjectName(u"pushButtonTweak")
        self.pushButtonTweak.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonTweak)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 40)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DialogTweakSections)

        QMetaObject.connectSlotsByName(DialogTweakSections)
    # setupUi

    def retranslateUi(self, DialogTweakSections):
        DialogTweakSections.setWindowTitle(QCoreApplication.translate("DialogTweakSections", u"Tweak Sections", None))
        self.labelCounty.setText(QCoreApplication.translate("DialogTweakSections", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("DialogTweakSections", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("DialogTweakSections", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("DialogTweakSections", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("DialogTweakSections", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("DialogTweakSections", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("DialogTweakSections", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("DialogTweakSections", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("DialogTweakSections", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.FilterColumncheckBox.setText(QCoreApplication.translate("DialogTweakSections", u"FilterColumn", None))
        self.pushButtonReset.setText(QCoreApplication.translate("DialogTweakSections", u"Reset", None))
        self.label.setText(QCoreApplication.translate("DialogTweakSections", u"From:", None))
        self.label_2.setText(QCoreApplication.translate("DialogTweakSections", u"To:", None))
        self.label_3.setText(QCoreApplication.translate("DialogTweakSections", u"New MP_START : ", None))
        self.label_4.setText(QCoreApplication.translate("DialogTweakSections", u"New MP END : ", None))
        self.pushButtonTweak.setText(QCoreApplication.translate("DialogTweakSections", u"Tweak", None))
    # retranslateUi

