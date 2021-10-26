# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_cmdJRCmWT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartCommandDialog(object):
    def setupUi(self, StartCommandDialog):
        if not StartCommandDialog.objectName():
            StartCommandDialog.setObjectName(u"StartCommandDialog")
        StartCommandDialog.setWindowModality(Qt.ApplicationModal)
        StartCommandDialog.resize(821, 698)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        StartCommandDialog.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(StartCommandDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(StartCommandDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.outputLabel = QLabel(self.layoutWidget)
        self.outputLabel.setObjectName(u"outputLabel")

        self.verticalLayout_2.addWidget(self.outputLabel)

        self.outputTextBrowser = QTextBrowser(self.layoutWidget)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        self.outputTextBrowser.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.outputTextBrowser)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.commandLabel = QLabel(self.layoutWidget1)
        self.commandLabel.setObjectName(u"commandLabel")

        self.verticalLayout.addWidget(self.commandLabel)

        self.commandEdit = QPlainTextEdit(self.layoutWidget1)
        self.commandEdit.setObjectName(u"commandEdit")

        self.verticalLayout.addWidget(self.commandEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startButton = QPushButton(self.layoutWidget1)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.terminateButton = QPushButton(self.layoutWidget1)
        self.terminateButton.setObjectName(u"terminateButton")

        self.horizontalLayout.addWidget(self.terminateButton)

        self.copyCommandButton = QPushButton(self.layoutWidget1)
        self.copyCommandButton.setObjectName(u"copyCommandButton")

        self.horizontalLayout.addWidget(self.copyCommandButton)

        self.clearOutputButton = QPushButton(self.layoutWidget1)
        self.clearOutputButton.setObjectName(u"clearOutputButton")

        self.horizontalLayout.addWidget(self.clearOutputButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(StartCommandDialog)

        QMetaObject.connectSlotsByName(StartCommandDialog)
    # setupUi

    def retranslateUi(self, StartCommandDialog):
        StartCommandDialog.setWindowTitle(QCoreApplication.translate("StartCommandDialog", u"Start Command", None))
        self.outputLabel.setText(QCoreApplication.translate("StartCommandDialog", u"Output:", None))
        self.outputTextBrowser.setMarkdown("")
        self.outputTextBrowser.setHtml(QCoreApplication.translate("StartCommandDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:7.2pt;\"><br /></p></body></html>", None))
        self.commandLabel.setText(QCoreApplication.translate("StartCommandDialog", u"Command:", None))
        self.startButton.setText(QCoreApplication.translate("StartCommandDialog", u"Start", None))
        self.terminateButton.setText(QCoreApplication.translate("StartCommandDialog", u"Terminate", None))
        self.copyCommandButton.setText(QCoreApplication.translate("StartCommandDialog", u"Copy Command", None))
        self.clearOutputButton.setText(QCoreApplication.translate("StartCommandDialog", u"Clear Output", None))
    # retranslateUi

