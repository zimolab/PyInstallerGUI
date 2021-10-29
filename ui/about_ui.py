# -*- coding:utf-8 -*-
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog

from core.appmeta import AppMeta
from ui.base.ui_about import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        logo = QPixmap("data/logos/pyinstaller-gui.ico")
        self.logoLabel.setPixmap(logo)
        self.logoLabel.setScaledContents(True)
        self.descriptionTextBrowser.setMarkdown(AppMeta(self).describeMe())