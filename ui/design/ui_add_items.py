# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_itemsSMhwRv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddItemsDialog(object):
    def setupUi(self, AddItemsDialog):
        if not AddItemsDialog.objectName():
            AddItemsDialog.setObjectName(u"AddItemsDialog")
        AddItemsDialog.resize(507, 209)
        self.verticalLayout = QVBoxLayout(AddItemsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.itemsLabel = QLabel(AddItemsDialog)
        self.itemsLabel.setObjectName(u"itemsLabel")

        self.verticalLayout.addWidget(self.itemsLabel)

        self.itemsEdit = QTextEdit(AddItemsDialog)
        self.itemsEdit.setObjectName(u"itemsEdit")

        self.verticalLayout.addWidget(self.itemsEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(AddItemsDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(AddItemsDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddItemsDialog)
        self.cancelButton.clicked.connect(AddItemsDialog.reject)

        QMetaObject.connectSlotsByName(AddItemsDialog)
    # setupUi

    def retranslateUi(self, AddItemsDialog):
        AddItemsDialog.setWindowTitle(QCoreApplication.translate("AddItemsDialog", u"Add Items", None))
        self.itemsLabel.setText(QCoreApplication.translate("AddItemsDialog", u"Items(use semicolon to splite multiple items)", None))
        self.addButton.setText(QCoreApplication.translate("AddItemsDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("AddItemsDialog", u"Cancel", None))
    # retranslateUi

