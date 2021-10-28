# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_extrasyHbuon.ui'
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
        ModifyExtrasDialog.setWindowModality(Qt.WindowModal)
        ModifyExtrasDialog.resize(586, 214)
        ModifyExtrasDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ModifyExtrasDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.destinationEdit = QLineEdit(ModifyExtrasDialog)
        self.destinationEdit.setObjectName(u"destinationEdit")

        self.gridLayout.addWidget(self.destinationEdit, 2, 1, 1, 1)

        self.soureEdit = QLineEdit(ModifyExtrasDialog)
        self.soureEdit.setObjectName(u"soureEdit")

        self.gridLayout.addWidget(self.soureEdit, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.reselectFileButton = QPushButton(ModifyExtrasDialog)
        self.reselectFileButton.setObjectName(u"reselectFileButton")

        self.horizontalLayout_4.addWidget(self.reselectFileButton)

        self.reselectDirButton = QPushButton(ModifyExtrasDialog)
        self.reselectDirButton.setObjectName(u"reselectDirButton")

        self.horizontalLayout_4.addWidget(self.reselectDirButton)

        self.srcRelativePathButton = QPushButton(ModifyExtrasDialog)
        self.srcRelativePathButton.setObjectName(u"srcRelativePathButton")

        self.horizontalLayout_4.addWidget(self.srcRelativePathButton)

        self.srcAbsoluteButton = QPushButton(ModifyExtrasDialog)
        self.srcAbsoluteButton.setObjectName(u"srcAbsoluteButton")

        self.horizontalLayout_4.addWidget(self.srcAbsoluteButton)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.destinationLabel = QLabel(ModifyExtrasDialog)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.gridLayout.addWidget(self.destinationLabel, 2, 0, 1, 1)

        self.sourceLabel = QLabel(ModifyExtrasDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.gridLayout.addWidget(self.sourceLabel, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.destBasenameButton = QPushButton(ModifyExtrasDialog)
        self.destBasenameButton.setObjectName(u"destBasenameButton")

        self.horizontalLayout_2.addWidget(self.destBasenameButton)

        self.destRelativePathButton = QPushButton(ModifyExtrasDialog)
        self.destRelativePathButton.setObjectName(u"destRelativePathButton")

        self.horizontalLayout_2.addWidget(self.destRelativePathButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmButton = QPushButton(ModifyExtrasDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(ModifyExtrasDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ModifyExtrasDialog)
        self.cancelButton.clicked.connect(ModifyExtrasDialog.reject)

        QMetaObject.connectSlotsByName(ModifyExtrasDialog)
    # setupUi

    def retranslateUi(self, ModifyExtrasDialog):
        ModifyExtrasDialog.setWindowTitle(QCoreApplication.translate("ModifyExtrasDialog", u"Modify Extras", None))
        self.reselectFileButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Reselect File", None))
        self.reselectDirButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Reselect Dir", None))
        self.srcRelativePathButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Relative Path", None))
        self.srcAbsoluteButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Absolute Path", None))
        self.destinationLabel.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Destination", None))
        self.sourceLabel.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Source", None))
        self.destBasenameButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Basename", None))
        self.destRelativePathButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Relative Path", None))
        self.confirmButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("ModifyExtrasDialog", u"Cancel", None))
    # retranslateUi

