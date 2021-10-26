# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_upx_excludesqAmCPm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectUPXExcludesDialog(object):
    def setupUi(self, SelectUPXExcludesDialog):
        if not SelectUPXExcludesDialog.objectName():
            SelectUPXExcludesDialog.setObjectName(u"SelectUPXExcludesDialog")
        SelectUPXExcludesDialog.setWindowModality(Qt.WindowModal)
        SelectUPXExcludesDialog.resize(621, 365)
        SelectUPXExcludesDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(SelectUPXExcludesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.descriptionLabel = QLabel(SelectUPXExcludesDialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.filenamesEdit = QPlainTextEdit(SelectUPXExcludesDialog)
        self.filenamesEdit.setObjectName(u"filenamesEdit")

        self.verticalLayout.addWidget(self.filenamesEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filenameSeparatorLabel = QLabel(SelectUPXExcludesDialog)
        self.filenameSeparatorLabel.setObjectName(u"filenameSeparatorLabel")
        self.filenameSeparatorLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.filenameSeparatorLabel)

        self.filenameSeparatorCombo = QComboBox(SelectUPXExcludesDialog)
        self.filenameSeparatorCombo.setObjectName(u"filenameSeparatorCombo")

        self.horizontalLayout.addWidget(self.filenameSeparatorCombo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectButton = QPushButton(SelectUPXExcludesDialog)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout_2.addWidget(self.selectButton)

        self.addButton = QPushButton(SelectUPXExcludesDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.cancelButton = QPushButton(SelectUPXExcludesDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SelectUPXExcludesDialog)

        QMetaObject.connectSlotsByName(SelectUPXExcludesDialog)
    # setupUi

    def retranslateUi(self, SelectUPXExcludesDialog):
        SelectUPXExcludesDialog.setWindowTitle(QCoreApplication.translate("SelectUPXExcludesDialog", u"Select UPX Excludes", None))
        self.descriptionLabel.setText(QCoreApplication.translate("SelectUPXExcludesDialog", u"Binaries to be excluded(filenames without path):", None))
        self.filenameSeparatorLabel.setText(QCoreApplication.translate("SelectUPXExcludesDialog", u"Filename Separator", None))
        self.selectButton.setText(QCoreApplication.translate("SelectUPXExcludesDialog", u"Select", None))
        self.addButton.setText(QCoreApplication.translate("SelectUPXExcludesDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("SelectUPXExcludesDialog", u"Cancel", None))
    # retranslateUi

