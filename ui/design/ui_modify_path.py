# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_pathDpkVpd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModifyPathDialog(object):
    def setupUi(self, ModifyPathDialog):
        if not ModifyPathDialog.objectName():
            ModifyPathDialog.setObjectName(u"ModifyPathDialog")
        ModifyPathDialog.setWindowModality(Qt.WindowModal)
        ModifyPathDialog.resize(418, 194)
        self.verticalLayout = QVBoxLayout(ModifyPathDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.modifiedPathEdit = QLineEdit(ModifyPathDialog)
        self.modifiedPathEdit.setObjectName(u"modifiedPathEdit")

        self.gridLayout.addWidget(self.modifiedPathEdit, 1, 1, 1, 1)

        self.modifiedPathLabel = QLabel(ModifyPathDialog)
        self.modifiedPathLabel.setObjectName(u"modifiedPathLabel")

        self.gridLayout.addWidget(self.modifiedPathLabel, 1, 0, 1, 1)

        self.originPathLabel = QLabel(ModifyPathDialog)
        self.originPathLabel.setObjectName(u"originPathLabel")

        self.gridLayout.addWidget(self.originPathLabel, 0, 0, 1, 1)

        self.originPathEdit = QLineEdit(ModifyPathDialog)
        self.originPathEdit.setObjectName(u"originPathEdit")
        self.originPathEdit.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.originPathEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.relpathButton = QPushButton(ModifyPathDialog)
        self.relpathButton.setObjectName(u"relpathButton")

        self.horizontalLayout.addWidget(self.relpathButton)

        self.confirmButton = QPushButton(ModifyPathDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(ModifyPathDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ModifyPathDialog)
        self.cancelButton.clicked.connect(ModifyPathDialog.reject)

        QMetaObject.connectSlotsByName(ModifyPathDialog)
    # setupUi

    def retranslateUi(self, ModifyPathDialog):
        ModifyPathDialog.setWindowTitle(QCoreApplication.translate("ModifyPathDialog", u"Modify Path", None))
        self.modifiedPathLabel.setText(QCoreApplication.translate("ModifyPathDialog", u"Modified", None))
        self.originPathLabel.setText(QCoreApplication.translate("ModifyPathDialog", u"Origin", None))
        self.relpathButton.setText(QCoreApplication.translate("ModifyPathDialog", u"Relative Path", None))
        self.confirmButton.setText(QCoreApplication.translate("ModifyPathDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("ModifyPathDialog", u"Cancel", None))
    # retranslateUi

