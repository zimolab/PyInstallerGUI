# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutzGLJcj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.setWindowModality(Qt.WindowModal)
        AboutDialog.resize(600, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMinimumSize(QSize(600, 260))
        AboutDialog.setMaximumSize(QSize(600, 260))
        AboutDialog.setModal(True)
        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(250, 220, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.logoLabel = QLabel(AboutDialog)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(10, 30, 151, 151))
        self.logoLabel.setTextFormat(Qt.PlainText)
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignCenter)
        self.descriptionTextBrowser = QTextBrowser(AboutDialog)
        self.descriptionTextBrowser.setObjectName(u"descriptionTextBrowser")
        self.descriptionTextBrowser.setGeometry(QRect(165, 10, 431, 201))
        self.descriptionTextBrowser.setOpenExternalLinks(True)
        self.descriptionTextBrowser.setOpenLinks(False)

        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.logoLabel.setText("")
    # retranslateUi

