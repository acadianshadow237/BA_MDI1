# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'split_sections_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DialogSplitSections(QWidget):
    def setupUi(self, DialogSplitSections):
        if not DialogSplitSections.objectName():
            DialogSplitSections.setObjectName(u"DialogSplitSections")
        DialogSplitSections.resize(1089, 467)
        font = QFont()
        font.setPointSize(12)
        DialogSplitSections.setFont(font)
        self.verticalLayout = QVBoxLayout(DialogSplitSections)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCounty = QLabel(DialogSplitSections)
        self.labelCounty.setObjectName(u"labelCounty")
        self.labelCounty.setFont(font)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(DialogSplitSections)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setMaximumSize(QSize(200, 16777215))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(DialogSplitSections)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(DialogSplitSections)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setMaximumSize(QSize(200, 16777215))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(DialogSplitSections)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(DialogSplitSections)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(250, 35))
        self.comboBoxDirection.setMaximumSize(QSize(200, 16777215))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.FilterColumncheckBox = QCheckBox(DialogSplitSections)
        self.FilterColumncheckBox.setObjectName(u"FilterColumncheckBox")
        self.FilterColumncheckBox.setFont(font)

        self.horizontalLayout.addWidget(self.FilterColumncheckBox)

        self.pushButtonReset = QPushButton(DialogSplitSections)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(DialogSplitSections)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(DialogSplitSections)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.textEditFrom = QTextEdit(DialogSplitSections)
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

        self.label_3 = QLabel(DialogSplitSections)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEditSplit = QLineEdit(DialogSplitSections)
        self.lineEditSplit.setObjectName(u"lineEditSplit")
        self.lineEditSplit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.lineEditSplit)

        self.label_2 = QLabel(DialogSplitSections)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.textEditTo = QTextEdit(DialogSplitSections)
        self.textEditTo.setObjectName(u"textEditTo")
        sizePolicy.setHeightForWidth(self.textEditTo.sizePolicy().hasHeightForWidth())
        self.textEditTo.setSizePolicy(sizePolicy)
        self.textEditTo.setMinimumSize(QSize(0, 35))
        self.textEditTo.setMaximumSize(QSize(16777215, 28))
        self.textEditTo.setFont(font)
        self.textEditTo.setLayoutDirection(Qt.RightToLeft)
        self.textEditTo.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEditTo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButtonSplit = QPushButton(DialogSplitSections)
        self.pushButtonSplit.setObjectName(u"pushButtonSplit")
        self.pushButtonSplit.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonSplit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 40)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DialogSplitSections)

        QMetaObject.connectSlotsByName(DialogSplitSections)
    # setupUi

    def retranslateUi(self, DialogSplitSections):
        DialogSplitSections.setWindowTitle(QCoreApplication.translate("DialogSplitSections", u"Split Sections", None))
        self.labelCounty.setText(QCoreApplication.translate("DialogSplitSections", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("DialogSplitSections", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("DialogSplitSections", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("DialogSplitSections", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("DialogSplitSections", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("DialogSplitSections", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("DialogSplitSections", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("DialogSplitSections", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("DialogSplitSections", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.FilterColumncheckBox.setText(QCoreApplication.translate("DialogSplitSections", u"FilterColumn", None))
        self.pushButtonReset.setText(QCoreApplication.translate("DialogSplitSections", u"Reset", None))
        self.label.setText(QCoreApplication.translate("DialogSplitSections", u"From:", None))
        self.label_3.setText(QCoreApplication.translate("DialogSplitSections", u"Split Mileage:", None))
        self.lineEditSplit.setInputMask(QCoreApplication.translate("DialogSplitSections", u"9999999", None))
        self.label_2.setText(QCoreApplication.translate("DialogSplitSections", u"To:", None))
        self.pushButtonSplit.setText(QCoreApplication.translate("DialogSplitSections", u"Split", None))
    # retranslateUi

