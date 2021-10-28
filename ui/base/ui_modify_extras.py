# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_extrasEFtZQp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModifyExtrasDialog(object):
    def setupUi(self, ModifyExtrasDialog):
        if not ModifyExtrasDialog.objectName():
            ModifyExtrasDialog.setObjectName(u"ModifyExtrasDialog")
        ModifyExtrasDialog.resize(553, 219)
        self.verticalLayout = QVBoxLayout(ModifyExtrasDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sourceLabel = QLabel(ModifyExtrasDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.gridLayout.addWidget(self.sourceLabel, 0, 0, 1, 1)

        self.soureEdit = QLineEdit(ModifyExtrasDialog)
        self.soureEdit.setObjectName(u"soureEdit")

        self.gridLayout.addWidget(self.soureEdit, 0, 1, 1, 1)

        self.destinationEdit = QLineEdit(ModifyExtrasDialog)
        self.destinationEdit.setObjectName(u"destinationEdit")

        self.gridLayout.addWidget(self.destinationEdit, 1, 1, 1, 1)

        self.destinationLabel = QLabel(ModifyExtrasDialog)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.gridLayout.addWidget(self.destinationLabel, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.reselectButton = QPushButton(ModifyExtrasDialog)
        self.reselectButton.setObjectName(u"reselectButton")

        self.horizontalLayout_2.addWidget(self.reselectButton)

        self.relativePathButton = QPushButton(ModifyExtrasDialog)
        self.relativePathButton.setObjectName(u"relativePathButton")

        self.horizontalLayout_2.addWidget(self.relativePathButton)

        self.basenameButton = QPushButton(ModifyExtrasDialog)
        self.basenameButton.setObjectName(u"basenameButton")

        self.horizontalLayout_2.addWidget(self.basenameButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label = QLabel(ModifyExtrasDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmButton = QPushButton(ModifyExtrasDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(ModifyExtrasDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ModifyExtrasDialog)

        QMetaObject.connectSlotsByName(ModifyExtrasDialog)
    # setupUi

    def retranslateUi(self, ModifyExtrasDialog):
        ModifyExtrasDialog.setWindowTitle(QCoreApplication.translate("ModifyExtrasDialog", u"Modify Extras", None))
        self.sourceLabel.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Source", None))
        self.destinationLabel.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Destination", None))
        self.reselectButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Reselect", None))
        self.relativePathButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Relative Path", None))
        self.basenameButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Basename", None))
        self.label.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Note: glob format is supported!", None))
        self.confirmButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Cancel", None))
    # retranslateUi

