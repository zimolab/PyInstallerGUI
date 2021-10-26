# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upx_excludesQNokPy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UPXExcludesDialog(object):
    def setupUi(self, UPXExcludesDialog):
        if not UPXExcludesDialog.objectName():
            UPXExcludesDialog.setObjectName(u"UPXExcludesDialog")
        UPXExcludesDialog.setWindowModality(Qt.WindowModal)
        UPXExcludesDialog.resize(621, 365)
        UPXExcludesDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(UPXExcludesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.descriptionLabel = QLabel(UPXExcludesDialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.filenamesEdit = QPlainTextEdit(UPXExcludesDialog)
        self.filenamesEdit.setObjectName(u"filenamesEdit")

        self.verticalLayout.addWidget(self.filenamesEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filenameSeparatorLabel = QLabel(UPXExcludesDialog)
        self.filenameSeparatorLabel.setObjectName(u"filenameSeparatorLabel")
        self.filenameSeparatorLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.filenameSeparatorLabel)

        self.filenameSeparatorCombo = QComboBox(UPXExcludesDialog)
        self.filenameSeparatorCombo.setObjectName(u"filenameSeparatorCombo")

        self.horizontalLayout.addWidget(self.filenameSeparatorCombo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectButton = QPushButton(UPXExcludesDialog)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout_2.addWidget(self.selectButton)

        self.addButton = QPushButton(UPXExcludesDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.cancelButton = QPushButton(UPXExcludesDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(UPXExcludesDialog)
        self.cancelButton.clicked.connect(UPXExcludesDialog.reject)

        QMetaObject.connectSlotsByName(UPXExcludesDialog)
    # setupUi

    def retranslateUi(self, UPXExcludesDialog):
        UPXExcludesDialog.setWindowTitle(QCoreApplication.translate("UPXExcludesDialog", u"UPX Excludes", None))
        self.descriptionLabel.setText(QCoreApplication.translate("UPXExcludesDialog", u"Binaries to be excluded(filenames without path):", None))
        self.filenameSeparatorLabel.setText(QCoreApplication.translate("UPXExcludesDialog", u"Filename Separator", None))
        self.selectButton.setText(QCoreApplication.translate("UPXExcludesDialog", u"Select", None))
        self.addButton.setText(QCoreApplication.translate("UPXExcludesDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("UPXExcludesDialog", u"Cancel", None))
    # retranslateUi

