# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RouteProjectEntry_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_rtProjEntryForm(QWidget):
    def setupUi(self, rtProjEntryForm):
        if not rtProjEntryForm.objectName():
            rtProjEntryForm.setObjectName(u"rtProjEntryForm")
        rtProjEntryForm.resize(1175, 417)
        self.verticalLayout_2 = QVBoxLayout(rtProjEntryForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCounty = QLabel(rtProjEntryForm)
        self.labelCounty.setObjectName(u"labelCounty")
        font = QFont()
        font.setPointSize(12)
        self.labelCounty.setFont(font)
        self.labelCounty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelCounty)

        self.comboBoxCounty = QComboBox(rtProjEntryForm)
        self.comboBoxCounty.setObjectName(u"comboBoxCounty")
        self.comboBoxCounty.setMinimumSize(QSize(100, 28))
        self.comboBoxCounty.setFont(font)
        self.comboBoxCounty.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBoxCounty)

        self.labelRoute = QLabel(rtProjEntryForm)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setFont(font)
        self.labelRoute.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelRoute)

        self.comboBoxRoute = QComboBox(rtProjEntryForm)
        self.comboBoxRoute.setObjectName(u"comboBoxRoute")
        self.comboBoxRoute.setMinimumSize(QSize(100, 28))
        self.comboBoxRoute.setFont(font)
        self.comboBoxRoute.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBoxRoute)

        self.labelDirection = QLabel(rtProjEntryForm)
        self.labelDirection.setObjectName(u"labelDirection")
        self.labelDirection.setFont(font)
        self.labelDirection.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelDirection)

        self.comboBoxDirection = QComboBox(rtProjEntryForm)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        self.comboBoxDirection.setMinimumSize(QSize(300, 28))
        self.comboBoxDirection.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDirection)

        self.pushButtonReset = QPushButton(rtProjEntryForm)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonReset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelFrom = QLabel(rtProjEntryForm)
        self.labelFrom.setObjectName(u"labelFrom")
        self.labelFrom.setFont(font)
        self.labelFrom.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelFrom)

        self.comboBoxFrom = QComboBox(rtProjEntryForm)
        self.comboBoxFrom.setObjectName(u"comboBoxFrom")
        self.comboBoxFrom.setMinimumSize(QSize(100, 28))
        self.comboBoxFrom.setFont(font)
        self.comboBoxFrom.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBoxFrom)

        self.labelTo = QLabel(rtProjEntryForm)
        self.labelTo.setObjectName(u"labelTo")
        self.labelTo.setFont(font)
        self.labelTo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTo)

        self.comboBoxTo = QComboBox(rtProjEntryForm)
        self.comboBoxTo.setObjectName(u"comboBoxTo")
        self.comboBoxTo.setMinimumSize(QSize(100, 28))
        self.comboBoxTo.setFont(font)
        self.comboBoxTo.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBoxTo)

        self.pushButtonVASSelect = QPushButton(rtProjEntryForm)
        self.pushButtonVASSelect.setObjectName(u"pushButtonVASSelect")
        self.pushButtonVASSelect.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonVASSelect)

        self.pushButtonVASSplit = QPushButton(rtProjEntryForm)
        self.pushButtonVASSplit.setObjectName(u"pushButtonVASSplit")
        self.pushButtonVASSplit.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonVASSplit)

        self.pushButtonSyncAll = QPushButton(rtProjEntryForm)
        self.pushButtonSyncAll.setObjectName(u"pushButtonSyncAll")
        self.pushButtonSyncAll.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonSyncAll)

        self.pushButtonVASReview = QPushButton(rtProjEntryForm)
        self.pushButtonVASReview.setObjectName(u"pushButtonVASReview")
        self.pushButtonVASReview.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonVASReview)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelProject = QLabel(rtProjEntryForm)
        self.labelProject.setObjectName(u"labelProject")
        self.labelProject.setFont(font)
        self.labelProject.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelProject)

        self.comboBoxProjNmbr = QComboBox(rtProjEntryForm)
        self.comboBoxProjNmbr.setObjectName(u"comboBoxProjNmbr")
        self.comboBoxProjNmbr.setMinimumSize(QSize(200, 28))
        self.comboBoxProjNmbr.setFont(font)
        self.comboBoxProjNmbr.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBoxProjNmbr)

        self.labelDetail = QLabel(rtProjEntryForm)
        self.labelDetail.setObjectName(u"labelDetail")
        self.labelDetail.setFont(font)
        self.labelDetail.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelDetail)

        self.comboBoxProjDetail = QComboBox(rtProjEntryForm)
        self.comboBoxProjDetail.setObjectName(u"comboBoxProjDetail")
        self.comboBoxProjDetail.setMinimumSize(QSize(200, 28))
        self.comboBoxProjDetail.setFont(font)
        self.comboBoxProjDetail.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBoxProjDetail)

        self.pushButtonProjReset = QPushButton(rtProjEntryForm)
        self.pushButtonProjReset.setObjectName(u"pushButtonProjReset")
        self.pushButtonProjReset.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonProjReset)

        self.pushButtonProjSelect = QPushButton(rtProjEntryForm)
        self.pushButtonProjSelect.setObjectName(u"pushButtonProjSelect")
        self.pushButtonProjSelect.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonProjSelect)

        self.pushButtonProjAdd = QPushButton(rtProjEntryForm)
        self.pushButtonProjAdd.setObjectName(u"pushButtonProjAdd")
        self.pushButtonProjAdd.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonProjAdd)

        self.pushButtonProjUpdate = QPushButton(rtProjEntryForm)
        self.pushButtonProjUpdate.setObjectName(u"pushButtonProjUpdate")
        self.pushButtonProjUpdate.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonProjUpdate)

        self.pushButtonProjDelete = QPushButton(rtProjEntryForm)
        self.pushButtonProjDelete.setObjectName(u"pushButtonProjDelete")
        self.pushButtonProjDelete.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonProjDelete)

        self.pushButtonReviewProj = QPushButton(rtProjEntryForm)
        self.pushButtonReviewProj.setObjectName(u"pushButtonReviewProj")
        self.pushButtonReviewProj.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonReviewProj)

        self.pushButtonReviewAllProj = QPushButton(rtProjEntryForm)
        self.pushButtonReviewAllProj.setObjectName(u"pushButtonReviewAllProj")
        self.pushButtonReviewAllProj.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonReviewAllProj)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelLayers = QLabel(rtProjEntryForm)
        self.labelLayers.setObjectName(u"labelLayers")
        self.labelLayers.setMaximumSize(QSize(16777215, 16777215))
        self.labelLayers.setFont(font)
        self.labelLayers.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelLayers)

        self.pushButtonLayersReset = QPushButton(rtProjEntryForm)
        self.pushButtonLayersReset.setObjectName(u"pushButtonLayersReset")
        self.pushButtonLayersReset.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayersReset)

        self.pushButtonLayerUp = QPushButton(rtProjEntryForm)
        self.pushButtonLayerUp.setObjectName(u"pushButtonLayerUp")
        self.pushButtonLayerUp.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerUp)

        self.pushButtonLayerDown = QPushButton(rtProjEntryForm)
        self.pushButtonLayerDown.setObjectName(u"pushButtonLayerDown")
        self.pushButtonLayerDown.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerDown)

        self.pushButtonLayerAdd = QPushButton(rtProjEntryForm)
        self.pushButtonLayerAdd.setObjectName(u"pushButtonLayerAdd")
        self.pushButtonLayerAdd.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerAdd)

        self.pushButtonLayerUpdate = QPushButton(rtProjEntryForm)
        self.pushButtonLayerUpdate.setObjectName(u"pushButtonLayerUpdate")
        self.pushButtonLayerUpdate.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerUpdate)

        self.pushButtonLayerDelete = QPushButton(rtProjEntryForm)
        self.pushButtonLayerDelete.setObjectName(u"pushButtonLayerDelete")
        self.pushButtonLayerDelete.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerDelete)

        self.pushButtonTemplet = QPushButton(rtProjEntryForm)
        self.pushButtonTemplet.setObjectName(u"pushButtonTemplet")
        self.pushButtonTemplet.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonTemplet)

        self.pushButtonLayerApply = QPushButton(rtProjEntryForm)
        self.pushButtonLayerApply.setObjectName(u"pushButtonLayerApply")
        self.pushButtonLayerApply.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonLayerApply)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tableWidget = QTableWidget(rtProjEntryForm)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {background-color: rgb(211,211,211); color: rgb(0, 0, 0);}\n"
"QHeaderView::section:horizontal{   border-top: 1px solid #fffff8;}")

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 20)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(rtProjEntryForm)

        QMetaObject.connectSlotsByName(rtProjEntryForm)
    # setupUi

    def retranslateUi(self, rtProjEntryForm):
        rtProjEntryForm.setWindowTitle(QCoreApplication.translate("rtProjEntryForm", u"Route Project Entry", None))
        self.labelCounty.setText(QCoreApplication.translate("rtProjEntryForm", u"County:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCounty.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxCounty.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelRoute.setText(QCoreApplication.translate("rtProjEntryForm", u"Route:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxRoute.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxRoute.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.labelDirection.setText(QCoreApplication.translate("rtProjEntryForm", u"Direction:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDirection.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"Please Select Direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxDirection.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select Direction", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonReset.setText(QCoreApplication.translate("rtProjEntryForm", u"Reset All", None))
        self.labelFrom.setText(QCoreApplication.translate("rtProjEntryForm", u"From:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxFrom.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxFrom.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelTo.setText(QCoreApplication.translate("rtProjEntryForm", u"To:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxTo.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxTo.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonVASSelect.setText(QCoreApplication.translate("rtProjEntryForm", u"Select by VAS", None))
        self.pushButtonVASSplit.setText(QCoreApplication.translate("rtProjEntryForm", u"Split", None))
        self.pushButtonSyncAll.setText(QCoreApplication.translate("rtProjEntryForm", u"Sync", None))
        self.pushButtonVASReview.setText(QCoreApplication.translate("rtProjEntryForm", u"Review", None))
        self.labelProject.setText(QCoreApplication.translate("rtProjEntryForm", u"Project:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxProjNmbr.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select County</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxProjNmbr.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select County", None))
#endif // QT_CONFIG(statustip)
        self.labelDetail.setText(QCoreApplication.translate("rtProjEntryForm", u"Detail:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxProjDetail.setToolTip(QCoreApplication.translate("rtProjEntryForm", u"<html><head/><body><p>Please Select Route</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxProjDetail.setStatusTip(QCoreApplication.translate("rtProjEntryForm", u"Select Route", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonProjReset.setText(QCoreApplication.translate("rtProjEntryForm", u"Reset", None))
        self.pushButtonProjSelect.setText(QCoreApplication.translate("rtProjEntryForm", u"Select", None))
        self.pushButtonProjAdd.setText(QCoreApplication.translate("rtProjEntryForm", u"Add", None))
        self.pushButtonProjUpdate.setText(QCoreApplication.translate("rtProjEntryForm", u"Update", None))
        self.pushButtonProjDelete.setText(QCoreApplication.translate("rtProjEntryForm", u"Delete", None))
        self.pushButtonReviewProj.setText(QCoreApplication.translate("rtProjEntryForm", u"Review", None))
        self.pushButtonReviewAllProj.setText(QCoreApplication.translate("rtProjEntryForm", u"Review All", None))
        self.labelLayers.setText(QCoreApplication.translate("rtProjEntryForm", u"Layers:", None))
        self.pushButtonLayersReset.setText(QCoreApplication.translate("rtProjEntryForm", u"Reset", None))
        self.pushButtonLayerUp.setText(QCoreApplication.translate("rtProjEntryForm", u"Move Up", None))
        self.pushButtonLayerDown.setText(QCoreApplication.translate("rtProjEntryForm", u"Move Down", None))
        self.pushButtonLayerAdd.setText(QCoreApplication.translate("rtProjEntryForm", u"Add", None))
        self.pushButtonLayerUpdate.setText(QCoreApplication.translate("rtProjEntryForm", u"Update", None))
        self.pushButtonLayerDelete.setText(QCoreApplication.translate("rtProjEntryForm", u"Delete", None))
        self.pushButtonTemplet.setText(QCoreApplication.translate("rtProjEntryForm", u"Templetet", None))
        self.pushButtonLayerApply.setText(QCoreApplication.translate("rtProjEntryForm", u"Apply", None))
    # retranslateUi

