# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_extrasIYOHMi.ui'
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
        AddExtrasDialog.resize(563, 182)
        AddExtrasDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(AddExtrasDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddExtrasDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.destinationLabel = QLabel(AddExtrasDialog)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.gridLayout.addWidget(self.destinationLabel, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectDirButton = QPushButton(AddExtrasDialog)
        self.selectDirButton.setObjectName(u"selectDirButton")

        self.horizontalLayout.addWidget(self.selectDirButton)

        self.selectFileButton = QPushButton(AddExtrasDialog)
        self.selectFileButton.setObjectName(u"selectFileButton")

        self.horizontalLayout.addWidget(self.selectFileButton)

        self.relativePathButton = QPushButton(AddExtrasDialog)
        self.relativePathButton.setObjectName(u"relativePathButton")

        self.horizontalLayout.addWidget(self.relativePathButton)

        self.absolutePathButton = QPushButton(AddExtrasDialog)
        self.absolutePathButton.setObjectName(u"absolutePathButton")

        self.horizontalLayout.addWidget(self.absolutePathButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.sourceLabel = QLabel(AddExtrasDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.gridLayout.addWidget(self.sourceLabel, 0, 0, 1, 1)

        self.destinationEdit = QLineEdit(AddExtrasDialog)
        self.destinationEdit.setObjectName(u"destinationEdit")

        self.gridLayout.addWidget(self.destinationEdit, 2, 1, 1, 1)

        self.soureEdit = QLineEdit(AddExtrasDialog)
        self.soureEdit.setObjectName(u"soureEdit")

        self.gridLayout.addWidget(self.soureEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(AddExtrasDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.exitButton = QPushButton(AddExtrasDialog)
        self.exitButton.setObjectName(u"exitButton")

        self.horizontalLayout_2.addWidget(self.exitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AddExtrasDialog)
        self.exitButton.clicked.connect(AddExtrasDialog.hide)

        QMetaObject.connectSlotsByName(AddExtrasDialog)
    # setupUi

    def retranslateUi(self, AddExtrasDialog):
        AddExtrasDialog.setWindowTitle(QCoreApplication.translate("AddExtrasDialog", u"Add Extras", None))
        self.label.setText(QCoreApplication.translate("AddExtrasDialog", u"Note: glob format is supported!", None))
        self.destinationLabel.setText(QCoreApplication.translate("AddExtrasDialog", u"Destination", None))
        self.selectDirButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Select Dir", None))
        self.selectFileButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Select File", None))
        self.relativePathButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Relative Path", None))
        self.absolutePathButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Absolute Path", None))
        self.sourceLabel.setText(QCoreApplication.translate("AddExtrasDialog", u"Source", None))
        self.addButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Add", None))
        self.exitButton.setText(QCoreApplication.translate("AddExtrasDialog", u"Exit", None))
    # retranslateUi

