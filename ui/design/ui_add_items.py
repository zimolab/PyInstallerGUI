# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_itemsHFJeFq.ui'
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
        AddItemsDialog.resize(507, 261)
        self.verticalLayout = QVBoxLayout(AddItemsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.itemsEdit = QTextEdit(AddItemsDialog)
        self.itemsEdit.setObjectName(u"itemsEdit")

        self.verticalLayout.addWidget(self.itemsEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.multiItemSeparatorLabel = QLabel(AddItemsDialog)
        self.multiItemSeparatorLabel.setObjectName(u"multiItemSeparatorLabel")
        self.multiItemSeparatorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.multiItemSeparatorLabel)

        self.multiItemSeparatorCombo = QComboBox(AddItemsDialog)
        self.multiItemSeparatorCombo.setObjectName(u"multiItemSeparatorCombo")

        self.horizontalLayout_2.addWidget(self.multiItemSeparatorCombo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

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
        self.multiItemSeparatorLabel.setText(QCoreApplication.translate("AddItemsDialog", u"Multi-Item Separator:", None))
        self.addButton.setText(QCoreApplication.translate("AddItemsDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("AddItemsDialog", u"Cancel", None))
    # retranslateUi

