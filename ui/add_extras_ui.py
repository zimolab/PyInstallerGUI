# -*- coding:utf-8 -*-
import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog
from QBinder import Binder
from ui.base.ui_add_extras import Ui_AddExtrasDialog
# noinspection PyTypeChecker
from utils import openDirDialog, openFileDialog, warn, relativePath, getBasename


# noinspection PyTypeChecker
class AddExtrasDialog(QDialog, Ui_AddExtrasDialog):
    ADD_EXTRA_DATA = 0
    ADD_EXTRA_BIN = 1
    MODIFY_EXTRA_DATA = 2
    MODIFY_EXTRA_BIN = 3

    extraDataAdded = Signal(str)
    extraBinaryAdded = Signal(str)
    extraDataChanged = Signal(int, str)
    extraBinaryChanged = Signal(int, str)

    def __init__(self, parent):
        super().__init__(parent)
        self._action = self.ADD_EXTRA_DATA
        self._state = Binder()
        self._state.sourcePath = ""
        self._state.destinationPath = ""
        self._index = None
        self.setupUi()

    def setupUi(self, _=None):
        super(AddExtrasDialog, self).setupUi(self)
        self.soureEdit.setText(lambda: self._state.sourcePath)
        self.destinationEdit.setText(lambda: self._state.destinationPath)
        self.selectDirButton.clicked.connect(self.onSelectDir)
        self.selectFileButton.clicked.connect(self.onSelectFile)
        self.actButton.clicked.connect(self.onAction)

    def display(self, action, extra=None, index=None):
        self._action = action
        if self._action == self.ADD_EXTRA_DATA:
            self.setWindowTitle(self.tr("Add Extra Data"))
            self.actButton.setText(self.tr("Add"))
        elif self._action == self.ADD_EXTRA_BIN:
            self.setWindowTitle(self.tr("Add Extra Binary"))
            self.actButton.setText(self.tr("Add"))
            self.selectDirButton.setEnabled(False)
        elif self._action == self.MODIFY_EXTRA_DATA:
            self.setWindowTitle(self.tr("Modify Extra Data"))
            self.startModifyAction(extra, index)
        elif self._action == self.MODIFY_EXTRA_BIN:
            self.setWindowTitle(self.tr("Modify Extra Binary"))
            self.actButton.setText(self.tr("Modify"))
            self.startModifyAction(extra, index)
        else:
            self.hide()
            return
        self.show()

    def hideEvent(self, event):
        self.actionEnd()

    def onSelectDir(self):
        selectedDir = openDirDialog(
            self,
            self.tr("Select Directory"),
        )
        if selectedDir is not None:
            self._state.sourcePath = selectedDir
            self._state.destinationPath = relativePath(selectedDir, fallback=getBasename)

    def onSelectFile(self):
        selectedFile = openFileDialog(
            self,
            self.tr("Select File")
        )
        if selectedFile is not None:
            self._state.sourcePath = selectedFile
            self._state.destinationPath = relativePath(selectedFile, fallback=getBasename)

    # noinspection PyUnresolvedReferences
    def onAction(self):
        if self._state.sourcePath is None or self._state.sourcePath == "":
            warn(self, self.tr("Warning"), self.tr("Source path is empty!"))
            return
        if self._state.destinationPath is None or self._state.destinationPath == "":
            warn(self, self.tr("Warning"), self.tr("Destination path is empty!"))
            return
        extra = self.join(self._state.sourcePath, self._state.destinationPath)
        if self._action == self.ADD_EXTRA_DATA:
            self.extraDataAdded.emit(extra)
        elif self._action == self.ADD_EXTRA_BIN:
            self.extraBinaryAdded.emit(extra)
        elif self._action == self.MODIFY_EXTRA_DATA:
            self.extraDataChanged.emit(self._index, extra)
        elif self._action == self.MODIFY_EXTRA_BIN:
            self.extraBinaryChanged.emit(self._index, extra)
        else:
            raise RuntimeError("Unknown action")

    @staticmethod
    def join(source, destination, pathsep=None):
        if pathsep is None:
            pathsep = os.pathsep
        return f"{source}{pathsep}{destination}"

    @staticmethod
    def split(extra):
        pathsep = ";"
        tmp = extra.split(pathsep)
        if len(tmp) == 2:
            return tmp
        pathsep = ":"
        tmp = extra.split(pathsep)
        if len(tmp) == 2:
            return tmp
        return extra, ""

    def startModifyAction(self, extra, index):
        self.actButton.setText(self.tr("Modify"))
        tmp = self.split(extra)
        self._state.sourcePath = tmp[0]
        self._state.destinationPath = tmp[1]
        self._index = index
        self.selectFileButton.setEnabled(False)
        self.selectDirButton.setEnabled(False)
        self.soureEdit.setEnabled(False)

    def actionEnd(self):
        self.actButton.setText("")
        self._state.sourcePath = ""
        self._state.destinationPath = ""
        self._index = -1
        self.selectFileButton.setEnabled(True)
        self.selectDirButton.setEnabled(True)
        self.soureEdit.setEnabled(True)

