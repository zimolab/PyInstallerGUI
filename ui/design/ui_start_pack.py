# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_packkEsAUG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartPackDialog(object):
    def setupUi(self, StartPackDialog):
        if not StartPackDialog.objectName():
            StartPackDialog.setObjectName(u"StartPackDialog")
        StartPackDialog.setWindowModality(Qt.ApplicationModal)
        StartPackDialog.resize(821, 698)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(9)
        StartPackDialog.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(StartPackDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(StartPackDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.outputLabel = QLabel(self.widget)
        self.outputLabel.setObjectName(u"outputLabel")

        self.verticalLayout_2.addWidget(self.outputLabel)

        self.outputTextBrowser = QTextBrowser(self.widget)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        self.outputTextBrowser.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.outputTextBrowser)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.commandLabel = QLabel(self.widget1)
        self.commandLabel.setObjectName(u"commandLabel")

        self.verticalLayout.addWidget(self.commandLabel)

        self.commandEdit = QPlainTextEdit(self.widget1)
        self.commandEdit.setObjectName(u"commandEdit")

        self.verticalLayout.addWidget(self.commandEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startButton = QPushButton(self.widget1)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.terminateButton = QPushButton(self.widget1)
        self.terminateButton.setObjectName(u"terminateButton")

        self.horizontalLayout.addWidget(self.terminateButton)

        self.copyCommandButton = QPushButton(self.widget1)
        self.copyCommandButton.setObjectName(u"copyCommandButton")

        self.horizontalLayout.addWidget(self.copyCommandButton)

        self.clearOutputButton = QPushButton(self.widget1)
        self.clearOutputButton.setObjectName(u"clearOutputButton")

        self.horizontalLayout.addWidget(self.clearOutputButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(StartPackDialog)

        QMetaObject.connectSlotsByName(StartPackDialog)
    # setupUi

    def retranslateUi(self, StartPackDialog):
        StartPackDialog.setWindowTitle(QCoreApplication.translate("StartPackDialog", u"Start Pack", None))
        self.outputLabel.setText(QCoreApplication.translate("StartPackDialog", u"Output:", None))
        self.outputTextBrowser.setMarkdown("")
        self.outputTextBrowser.setHtml(QCoreApplication.translate("StartPackDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:7.2pt;\"><br /></p></body></html>", None))
        self.commandLabel.setText(QCoreApplication.translate("StartPackDialog", u"Command:", None))
        self.startButton.setText(QCoreApplication.translate("StartPackDialog", u"Start", None))
        self.terminateButton.setText(QCoreApplication.translate("StartPackDialog", u"Terminate", None))
        self.copyCommandButton.setText(QCoreApplication.translate("StartPackDialog", u"Copy Command", None))
        self.clearOutputButton.setText(QCoreApplication.translate("StartPackDialog", u"Clear Output", None))
    # retranslateUi

