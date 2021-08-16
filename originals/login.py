# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(442, 507)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 170, 169, 37))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 210, 169, 38))
        self.label_4.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 169, 38))
        self.label_2.setFont(font)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 42, 169, 38))
        self.label_7.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 169, 37))
        self.label.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 250, 169, 37))
        self.label_5.setFont(font)
        self.cb_database_type = QComboBox(Dialog)
        self.cb_database_type.addItem("")
        self.cb_database_type.addItem("")
        self.cb_database_type.setObjectName(u"cb_database_type")
        self.cb_database_type.setGeometry(QRect(240, 260, 171, 31))
        self.tb_user_name = QPlainTextEdit(Dialog)
        self.tb_user_name.setObjectName(u"tb_user_name")
        self.tb_user_name.setGeometry(QRect(240, 50, 171, 31))
        self.tb_user_password = QPlainTextEdit(Dialog)
        self.tb_user_password.setObjectName(u"tb_user_password")
        self.tb_user_password.setGeometry(QRect(240, 90, 171, 31))
        self.tb_server_name = QPlainTextEdit(Dialog)
        self.tb_server_name.setObjectName(u"tb_server_name")
        self.tb_server_name.setGeometry(QRect(240, 130, 171, 31))
        self.tb_database_name = QPlainTextEdit(Dialog)
        self.tb_database_name.setObjectName(u"tb_database_name")
        self.tb_database_name.setGeometry(QRect(240, 170, 171, 31))
        self.tb_schema = QPlainTextEdit(Dialog)
        self.tb_schema.setObjectName(u"tb_schema")
        self.tb_schema.setGeometry(QRect(240, 210, 171, 31))
        self.pb_Ok = QPushButton(Dialog)
        self.pb_Ok.setObjectName(u"pb_Ok")
        self.pb_Ok.setGeometry(QRect(200, 420, 75, 24))
        self.pb_Cancel = QPushButton(Dialog)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        self.pb_Cancel.setGeometry(QRect(300, 420, 75, 24))

        self.retranslateUi(Dialog)
        self.pb_Ok.clicked.connect(Dialog.accept)
        self.pb_Cancel.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Database Name:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Schema", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Server Name:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"User ID:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Database Type:", None))
        self.cb_database_type.setItemText(0, QCoreApplication.translate("Dialog", u"Oracle", None))
        self.cb_database_type.setItemText(1, QCoreApplication.translate("Dialog", u"MS SQL", None))

        self.pb_Ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pb_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

