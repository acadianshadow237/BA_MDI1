# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditVAS_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EditVAS_AS_Dialog(QWidget):
    def setupUi(self, EditVAS_AS_Dialog):
        if not EditVAS_AS_Dialog.objectName():
            EditVAS_AS_Dialog.setObjectName(u"EditVAS_AS_Dialog")
        EditVAS_AS_Dialog.resize(961, 623)
        
        self.verticalLayout_3 = QVBoxLayout(EditVAS_AS_Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(EditVAS_AS_Dialog)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.textEditID = QTextEdit(EditVAS_AS_Dialog)
        self.textEditID.setObjectName(u"textEditID")
        self.textEditID.setMaximumSize(QSize(16777215, 35))
        self.textEditID.setFont(font)
        self.textEditID.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEditID)

        self.label = QLabel(EditVAS_AS_Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.textEditName = QTextEdit(EditVAS_AS_Dialog)
        self.textEditName.setObjectName(u"textEditName")
        self.textEditName.setMaximumSize(QSize(100, 35))
        self.textEditName.setFont(font)
        self.textEditName.setAutoFillBackground(False)
        self.textEditName.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEditName)

        self.label_2 = QLabel(EditVAS_AS_Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(98, 16777215))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.textEditRoadName = QTextEdit(EditVAS_AS_Dialog)
        self.textEditRoadName.setObjectName(u"textEditRoadName")
        self.textEditRoadName.setMaximumSize(QSize(100, 35))
        self.textEditRoadName.setFont(font)
        self.textEditRoadName.setAutoFillBackground(False)
        self.textEditRoadName.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEditRoadName)

        self.label_5 = QLabel(EditVAS_AS_Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 16777215))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.textEditpasid = QTextEdit(EditVAS_AS_Dialog)
        self.textEditpasid.setObjectName(u"textEditpasid")
        self.textEditpasid.setMaximumSize(QSize(110, 35))
        self.textEditpasid.setFont(font)
        self.textEditpasid.setAutoFillBackground(False)
        self.textEditpasid.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEditpasid)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(EditVAS_AS_Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.textEditFrom = QTextEdit(EditVAS_AS_Dialog)
        self.textEditFrom.setObjectName(u"textEditFrom")
        self.textEditFrom.setMaximumSize(QSize(100, 35))
        self.textEditFrom.setFont(font)
        self.textEditFrom.setAutoFillBackground(False)
        self.textEditFrom.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEditFrom)

        self.label_4 = QLabel(EditVAS_AS_Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.textEditTo = QTextEdit(EditVAS_AS_Dialog)
        self.textEditTo.setObjectName(u"textEditTo")
        self.textEditTo.setMaximumSize(QSize(100, 35))
        self.textEditTo.setFont(font)
        self.textEditTo.setAutoFillBackground(True)
        self.textEditTo.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEditTo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(EditVAS_AS_Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(500, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonEdit = QPushButton(EditVAS_AS_Dialog)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonEdit)

        self.pushButtonCancel = QPushButton(EditVAS_AS_Dialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 30)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(EditVAS_AS_Dialog)

        QMetaObject.connectSlotsByName(EditVAS_AS_Dialog)
    # setupUi

    def retranslateUi(self, EditVAS_AS_Dialog):
        EditVAS_AS_Dialog.setWindowTitle(QCoreApplication.translate("EditVAS_AS_Dialog", u"Edit Analysis Sections", None))
        self.label_7.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"ID:", None))
        self.label.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"RoadName:", None))
        self.label_5.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"pvmt_analysis_section_id:", None))
        self.label_3.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"From:", None))
        self.label_4.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"To:", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"Edit", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("EditVAS_AS_Dialog", u"Cancel", None))
    # retranslateUi

