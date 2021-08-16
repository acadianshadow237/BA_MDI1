# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VCRH_Edit_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_VCRH_Edit_Form(QWidget):
    def setupUi(self, VCRH_Edit_Form):
        if not VCRH_Edit_Form.objectName():
            VCRH_Edit_Form.setObjectName(u"VCRH_Edit_Form")
        VCRH_Edit_Form.resize(1217, 716)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VCRH_Edit_Form.sizePolicy().hasHeightForWidth())
        VCRH_Edit_Form.setSizePolicy(sizePolicy)
        VCRH_Edit_Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(VCRH_Edit_Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCounty = QLabel(VCRH_Edit_Form)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)
        self.labelCounty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(VCRH_Edit_Form)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(VCRH_Edit_Form)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)
        self.labelRoute.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(VCRH_Edit_Form)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(VCRH_Edit_Form)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)
        self.labelDirection.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(VCRH_Edit_Form)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(300, 28))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.pushButtonReset = QPushButton(VCRH_Edit_Form)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(VCRH_Edit_Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabSelect = QWidget()
        self.tabSelect.setObjectName(u"tabSelect")
        self.tabSelect.setFont(font)
        self.verticalLayout = QVBoxLayout(self.tabSelect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidgetVCRH = QTableWidget(self.tabSelect)
        self.tableWidgetVCRH.setObjectName(u"tableWidgetVCRH")
        self.tableWidgetVCRH.setFont(font)
        self.tableWidgetVCRH.setAutoFillBackground(True)
        self.tableWidgetVCRH.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")
        self.tableWidgetVCRH.setFrameShape(QFrame.Panel)
        self.tableWidgetVCRH.setLineWidth(1)
        self.tableWidgetVCRH.setMidLineWidth(1)
        self.tableWidgetVCRH.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.tableWidgetVCRH)

        self.tabWidget.addTab(self.tabSelect, "")
        self.tabEdit = QWidget()
        self.tabEdit.setObjectName(u"tabEdit")
        self.verticalLayout_5 = QVBoxLayout(self.tabEdit)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tabEdit)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.textEditFrom = QTextEdit(self.tabEdit)
        self.textEditFrom.setObjectName(u"textEditFrom")
        self.textEditFrom.setMaximumSize(QSize(100, 35))
        self.textEditFrom.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEditFrom)

        self.label_4 = QLabel(self.tabEdit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 35))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.textEditTo = QTextEdit(self.tabEdit)
        self.textEditTo.setObjectName(u"textEditTo")
        self.textEditTo.setMaximumSize(QSize(100, 35))
        self.textEditTo.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEditTo)

        self.label = QLabel(self.tabEdit)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.textEditid = QTextEdit(self.tabEdit)
        self.textEditid.setObjectName(u"textEditid")
        self.textEditid.setMaximumSize(QSize(500, 35))
        self.textEditid.setMidLineWidth(1)
        self.textEditid.setReadOnly(True)
        self.textEditid.setAcceptRichText(False)

        self.horizontalLayout_3.addWidget(self.textEditid)

        self.label_2 = QLabel(self.tabEdit)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 35))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEditName = QTextEdit(self.tabEdit)
        self.textEditName.setObjectName(u"textEditName")
        self.textEditName.setMaximumSize(QSize(200, 35))
        self.textEditName.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEditName)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 3)
        self.horizontalLayout_3.setStretch(6, 1)
        self.horizontalLayout_3.setStretch(7, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.tabEdit)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 35))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.textEditpasid = QTextEdit(self.tabEdit)
        self.textEditpasid.setObjectName(u"textEditpasid")
        self.textEditpasid.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_4.addWidget(self.textEditpasid)

        self.label_6 = QLabel(self.tabEdit)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 35))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.textEditproj_nmbr = QTextEdit(self.tabEdit)
        self.textEditproj_nmbr.setObjectName(u"textEditproj_nmbr")
        self.textEditproj_nmbr.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_4.addWidget(self.textEditproj_nmbr)

        self.label_7 = QLabel(self.tabEdit)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 35))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.textEditproj_detail_nmbr = QTextEdit(self.tabEdit)
        self.textEditproj_detail_nmbr.setObjectName(u"textEditproj_detail_nmbr")
        self.textEditproj_detail_nmbr.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.textEditproj_detail_nmbr)

        self.label_10 = QLabel(self.tabEdit)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 35))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.dateEditactl_end_date = QDateEdit(self.tabEdit)
        self.dateEditactl_end_date.setObjectName(u"dateEditactl_end_date")
        self.dateEditactl_end_date.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.dateEditactl_end_date)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 1)
        self.horizontalLayout_4.setStretch(7, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.tabEdit)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 35))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.textEditsoil_type_code = QTextEdit(self.tabEdit)
        self.textEditsoil_type_code.setObjectName(u"textEditsoil_type_code")
        self.textEditsoil_type_code.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_5.addWidget(self.textEditsoil_type_code)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_9 = QLabel(self.tabEdit)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 35))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.textEditsoil_type_desc = QTextEdit(self.tabEdit)
        self.textEditsoil_type_desc.setObjectName(u"textEditsoil_type_desc")
        self.textEditsoil_type_desc.setMaximumSize(QSize(350, 35))

        self.horizontalLayout_5.addWidget(self.textEditsoil_type_desc)

        self.horizontalSpacer_6 = QSpacerItem(255, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.tabEdit)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 35))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.textEditrehab_affctd_srfc_pct = QTextEdit(self.tabEdit)
        self.textEditrehab_affctd_srfc_pct.setObjectName(u"textEditrehab_affctd_srfc_pct")
        self.textEditrehab_affctd_srfc_pct.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_6.addWidget(self.textEditrehab_affctd_srfc_pct)

        self.label_16 = QLabel(self.tabEdit)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 35))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_16)

        self.comboBoxstructure_removed_ind = QComboBox(self.tabEdit)
        self.comboBoxstructure_removed_ind.addItem("")
        self.comboBoxstructure_removed_ind.addItem("")
        self.comboBoxstructure_removed_ind.setObjectName(u"comboBoxstructure_removed_ind")
        self.comboBoxstructure_removed_ind.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_6.addWidget(self.comboBoxstructure_removed_ind)

        self.horizontalSpacer_2 = QSpacerItem(255, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.tabEdit)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 35))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.textEditrehab_thickness = QTextEdit(self.tabEdit)
        self.textEditrehab_thickness.setObjectName(u"textEditrehab_thickness")
        self.textEditrehab_thickness.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_7.addWidget(self.textEditrehab_thickness)

        self.label_18 = QLabel(self.tabEdit)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 35))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_18)

        self.textEditrehab_type_code = QTextEdit(self.tabEdit)
        self.textEditrehab_type_code.setObjectName(u"textEditrehab_type_code")
        self.textEditrehab_type_code.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_7.addWidget(self.textEditrehab_type_code)

        self.label_19 = QLabel(self.tabEdit)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 35))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_19)

        self.textEditrehab_type_desc = QTextEdit(self.tabEdit)
        self.textEditrehab_type_desc.setObjectName(u"textEditrehab_type_desc")
        self.textEditrehab_type_desc.setMaximumSize(QSize(255, 35))

        self.horizontalLayout_7.addWidget(self.textEditrehab_type_desc)

        self.horizontalSpacer_5 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.tabEdit)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.label_20)

        self.textEditresurfacing_type_code = QTextEdit(self.tabEdit)
        self.textEditresurfacing_type_code.setObjectName(u"textEditresurfacing_type_code")
        self.textEditresurfacing_type_code.setMaximumSize(QSize(100, 35))

        self.horizontalLayout_8.addWidget(self.textEditresurfacing_type_code)

        self.label_21 = QLabel(self.tabEdit)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.label_21)

        self.textEditresurfacing_type_desc = QTextEdit(self.tabEdit)
        self.textEditresurfacing_type_desc.setObjectName(u"textEditresurfacing_type_desc")
        self.textEditresurfacing_type_desc.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.textEditresurfacing_type_desc)

        self.horizontalSpacer_7 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.tabEdit)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.label_11)

        self.comboBoxedge_drain_ind = QComboBox(self.tabEdit)
        self.comboBoxedge_drain_ind.addItem("")
        self.comboBoxedge_drain_ind.addItem("")
        self.comboBoxedge_drain_ind.setObjectName(u"comboBoxedge_drain_ind")
        self.comboBoxedge_drain_ind.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.comboBoxedge_drain_ind)

        self.label_12 = QLabel(self.tabEdit)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.label_12)

        self.textEditmilling_thickness = QTextEdit(self.tabEdit)
        self.textEditmilling_thickness.setObjectName(u"textEditmilling_thickness")
        self.textEditmilling_thickness.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.textEditmilling_thickness)

        self.label_13 = QLabel(self.tabEdit)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.dateEditoverlay_data_entered_date = QDateEdit(self.tabEdit)
        self.dateEditoverlay_data_entered_date.setObjectName(u"dateEditoverlay_data_entered_date")
        self.dateEditoverlay_data_entered_date.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.dateEditoverlay_data_entered_date)

        self.label_14 = QLabel(self.tabEdit)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.label_14)

        self.comboBoxpaving_fabric_ind = QComboBox(self.tabEdit)
        self.comboBoxpaving_fabric_ind.addItem("")
        self.comboBoxpaving_fabric_ind.addItem("")
        self.comboBoxpaving_fabric_ind.setObjectName(u"comboBoxpaving_fabric_ind")
        self.comboBoxpaving_fabric_ind.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.comboBoxpaving_fabric_ind)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_22 = QLabel(self.tabEdit)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 35))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.textEdittotal_courses_qty = QTextEdit(self.tabEdit)
        self.textEdittotal_courses_qty.setObjectName(u"textEdittotal_courses_qty")
        self.textEdittotal_courses_qty.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_9.addWidget(self.textEdittotal_courses_qty)

        self.label_23 = QLabel(self.tabEdit)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 35))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_23)

        self.textEdittotal_courses_thickness_qty = QTextEdit(self.tabEdit)
        self.textEdittotal_courses_thickness_qty.setObjectName(u"textEdittotal_courses_thickness_qty")
        self.textEdittotal_courses_thickness_qty.setMaximumSize(QSize(70, 35))

        self.horizontalLayout_9.addWidget(self.textEdittotal_courses_thickness_qty)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonSave = QPushButton(self.tabEdit)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_2.addWidget(self.pushButtonSave)

        self.pushButtonClear = QPushButton(self.tabEdit)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.horizontalLayout_2.addWidget(self.pushButtonClear)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_4.setStretch(5, 1)
        self.verticalLayout_4.setStretch(6, 1)
        self.verticalLayout_4.setStretch(7, 2)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tabEdit, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 20)

        self.retranslateUi(VCRH_Edit_Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VCRH_Edit_Form)
    # setupUi

    def retranslateUi(self, VCRH_Edit_Form):
        VCRH_Edit_Form.setWindowTitle(QCoreApplication.translate("VCRH_Edit_Form", u"VCRH Edit", None))
#if QT_CONFIG(tooltip)
        VCRH_Edit_Form.setToolTip(QCoreApplication.translate("VCRH_Edit_Form", u"Clear Data", None))
#endif // QT_CONFIG(tooltip)
        VCRH_Edit_Form.setProperty("filename", QCoreApplication.translate("VCRH_Edit_Form", u"VCRH_Edit", None))
        VCRH_Edit_Form.setProperty("formname", QCoreApplication.translate("VCRH_Edit_Form", u"VCRH_Edit", None))
        self.labelCounty.setText(QCoreApplication.translate("VCRH_Edit_Form", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("VCRH_Edit_Form", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("VCRH_Edit_Form", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("VCRH_Edit_Form", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("VCRH_Edit_Form", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("VCRH_Edit_Form", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("VCRH_Edit_Form", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonReset.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSelect), QCoreApplication.translate("VCRH_Edit_Form", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("VCRH_Edit_Form", u"From:", None))
        self.textEditFrom.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("VCRH_Edit_Form", u"To:", None))
        self.textEditTo.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("VCRH_Edit_Form", u"ID:", None))
        self.textEditid.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Name:", None))
        self.textEditName.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("VCRH_Edit_Form", u"pvmt_analysis_section_id:", None))
        self.textEditpasid.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("VCRH_Edit_Form", u"proj_nmbr:", None))
        self.textEditproj_nmbr.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("VCRH_Edit_Form", u"proj_detail_nmbr:", None))
        self.textEditproj_detail_nmbr.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("VCRH_Edit_Form", u"actl_end_date:", None))
        self.label_8.setText(QCoreApplication.translate("VCRH_Edit_Form", u"soil_type_code:", None))
        self.textEditsoil_type_code.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("VCRH_Edit_Form", u"<html><head/><body><p>soil_type_desc:</p></body></html>", None))
        self.textEditsoil_type_desc.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("VCRH_Edit_Form", u"rehab_affctd_srfc_pct:", None))
        self.textEditrehab_affctd_srfc_pct.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("VCRH_Edit_Form", u"structure_removed_ind:", None))
        self.comboBoxstructure_removed_ind.setItemText(0, QCoreApplication.translate("VCRH_Edit_Form", u"N", None))
        self.comboBoxstructure_removed_ind.setItemText(1, QCoreApplication.translate("VCRH_Edit_Form", u"Y", None))

        self.label_17.setText(QCoreApplication.translate("VCRH_Edit_Form", u"rehab_thickness:", None))
        self.textEditrehab_thickness.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("VCRH_Edit_Form", u"rehab_type_code:", None))
        self.textEditrehab_type_code.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("VCRH_Edit_Form", u"rehab_type_desc:", None))
        self.textEditrehab_type_desc.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("VCRH_Edit_Form", u"resurfacing_type_code:", None))
        self.textEditresurfacing_type_code.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("VCRH_Edit_Form", u"resurfacing_type_desc:", None))
        self.label_11.setText(QCoreApplication.translate("VCRH_Edit_Form", u"edge_drain_ind:", None))
        self.comboBoxedge_drain_ind.setItemText(0, QCoreApplication.translate("VCRH_Edit_Form", u"N", None))
        self.comboBoxedge_drain_ind.setItemText(1, QCoreApplication.translate("VCRH_Edit_Form", u"Y", None))

        self.label_12.setText(QCoreApplication.translate("VCRH_Edit_Form", u"milling_thickness:", None))
        self.textEditmilling_thickness.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("VCRH_Edit_Form", u"overlay_data_entered_date:", None))
        self.label_14.setText(QCoreApplication.translate("VCRH_Edit_Form", u"paving_fabric_ind:", None))
        self.comboBoxpaving_fabric_ind.setItemText(0, QCoreApplication.translate("VCRH_Edit_Form", u"N", None))
        self.comboBoxpaving_fabric_ind.setItemText(1, QCoreApplication.translate("VCRH_Edit_Form", u"Y", None))

        self.label_22.setText(QCoreApplication.translate("VCRH_Edit_Form", u"total_courses_qty:", None))
        self.textEdittotal_courses_qty.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("VCRH_Edit_Form", u"total_courses_thickness:", None))
        self.textEdittotal_courses_thickness_qty.setHtml(QCoreApplication.translate("VCRH_Edit_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButtonSave.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Save", None))
        self.pushButtonClear.setText(QCoreApplication.translate("VCRH_Edit_Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEdit), QCoreApplication.translate("VCRH_Edit_Form", u"Edit", None))
    # retranslateUi

