# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_extrasWrmpLu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddExtrasDialog(object):
    def setupUi(self, AddExtrasDialog):
        if not AddExtrasDialog.objectName():
            AddExtrasDialog.setObjectName(u"AddExtrasDialog")
        AddExtrasDialog.setWindowModality(Qt.WindowModal)
        AddExtrasDialog.resize(537, 216)
        AddExtrasDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(AddExtrasDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sourceLabel = QLabel(AddExtrasDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.gridLayout.addWidget(self.sourceLabel, 0, 0, 1, 1)

        self.soureEdit = QLineEdit(AddExtrasDialog)
        self.soureEdit.setObjectName(u"soureEdit")

        self.gridLayout.addWidget(self.soureEdit, 0, 1, 1, 1)

        self.destinationLabel = QLabel(AddExtrasDialog)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.gridLayout.addWidget(self.destinationLabel, 1, 0, 1, 1)

        self.destinationEdit = QLineEdit(AddExtrasDialog)
        self.destinationEdit.setObjectName(u"destinationEdit")

        self.gridLayout.addWidget(self.destinationEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label = QLabel(AddExtrasDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectFileButton = QPushButton(AddExtrasDialog)
        self.selectFileButton.setObjectName(u"selectFileButton")

        self.horizontalLayout.addWidget(self.selectFileButton)

        self.selectDirButton = QPushButton(AddExtrasDialog)
        self.selectDirButton.setObjectName(u"selectDirButton")

        self.horizontalLayout.addWidget(self.selectDirButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.actButton = QPushButton(AddExtrasDialog)
        self.actButton.setObjectName(u"actButton")

        self.horizontalLayout_2.addWidget(self.actButton)

        self.exitButton = QPushButton(AddExtrasDialog)
        self.exitButton.setObjectName(u"exitButton")

        self.horizontalLayout_2.addWidget(self.exitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AddExtrasDialog)
        self.exitButton.clicked.connect(AddExtrasDialog.hide)

        QMetaObject.connectSlotsByName(AddExtrasDialog)
    # setupUi

    def retranslateUi(self, AddExtrasDialog):
        AddExtrasDialog.setWindowTitle(QCoreApplication.translate("AddExtrasDialog", u"Add Extras", None))
        self.sourceLabel.setText(QCoreApplication.translate("AddExtrasDialog", u"Source", None))
        self.destinationLabel.setText(QCoreApplication.translate("AddExtrasDialog", u"Destination", None))
        self.label.setText(QCoreApplication.translate("AddExtrasDialog", u"Note: glob format is supported!", None))
        self.selectFileButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Select File", None))
        self.selectDirButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Select Dir", None))
        self.actButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Add", None))
        self.exitButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Exit", None))
    # retranslateUi

