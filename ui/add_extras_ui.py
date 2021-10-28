# -*- coding:utf-8 -*-
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

from ui.base.ui_add_extras import Ui_AddExtrasDialog
# noinspection PyTypeChecker
from utils import openDirDialog, openFileDialog, warn, relativePath, getBasename, notNull, isNull, joinSrcAndDest


# noinspection PyTypeChecker
class AddExtrasDialog(QDialog, Ui_AddExtrasDialog):
    ADD_EXTRA_DATA = 0
    ADD_EXTRA_BIN = 1

    extraDataAdded = Signal(str)
    extraBinaryAdded = Signal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self._action = -1
        self._index = None
        self.setupUi()

    def setupUi(self, _=None):
        super(AddExtrasDialog, self).setupUi(self)

        self.selectDirButton.clicked.connect(self.onSelectDir)
        self.selectFileButton.clicked.connect(self.onSelectFile)
        self.addButton.clicked.connect(self.onConfirm)

    def display(self, action):
        self._action = action
        if self._action == self.ADD_EXTRA_DATA:
            self.setWindowTitle(self.tr("Add Extra Data"))
        elif self._action == self.ADD_EXTRA_BIN:
            self.setWindowTitle(self.tr("Add Extra Binary"))
            self.selectDirButton.setEnabled(False)
        else:
            self.hide()
            return
        self.show()

    def hideEvent(self, event):
        self._action = -1
        self._index = -1
        self.soureEdit.setText("")
        self.destinationEdit.setText("")
        self.selectFileButton.setEnabled(True)
        self.selectDirButton.setEnabled(True)

    def onSelectDir(self):
        selectedDir = openDirDialog(
            self,
            self.tr("Select Directory"),
        )
        if notNull(selectedDir):
            self.soureEdit.setText(selectedDir)
            self.destinationEdit.setText(relativePath(selectedDir, fallback=getBasename))

    def onSelectFile(self):
        selectedFile = openFileDialog(
            self,
            self.tr("Select File")
        )
        if notNull(selectedFile):
            self.soureEdit.setText(selectedFile)
            self.destinationEdit.setText(relativePath(selectedFile, fallback=getBasename))

    # noinspection PyUnresolvedReferences
    def onConfirm(self):
        if isNull(self.soureEdit.text().strip()) or isNull(self.destinationEdit.text().strip()):
            warn(self, self.tr("Warning"), self.tr("Source and Destination cannot be empty!"))
            return
        extra = joinSrcAndDest(self.soureEdit.text().strip(), self.destinationEdit.text().strip())
        if self._action == self.ADD_EXTRA_DATA:
            self.extraDataAdded.emit(extra.strip())
        elif self._action == self.ADD_EXTRA_BIN:
            self.extraBinaryAdded.emit(extra.strip())
        else:
            raise RuntimeError("Unknown action")
