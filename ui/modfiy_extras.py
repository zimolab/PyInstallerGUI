# -*- coding:utf-8 -*-
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

# noinspection PyTypeChecker
from ui.base.ui_modify_extras import Ui_ModifyExtrasDialog

# noinspection PyTypeChecker
from utils import splitSrcAndDest, openFileDialog, notNull, relativePath, getBasename, openDirDialog, isEmpty, \
    absolutePath, isNull, warn, joinSrcAndDest


class ModifyExtrasDialog(QDialog, Ui_ModifyExtrasDialog):
    MODIFY_EXTRA_DATA = 0
    MODIFY_EXTRA_BIN = 1

    extraDataModified = Signal(int, str)
    extraBinaryModified = Signal(int, str)

    def __init__(self, parent):
        super().__init__(parent)
        self._action = -1
        self._index = -1
        self.setupUi()

    def setupUi(self, _=None):
        super(ModifyExtrasDialog, self).setupUi(self)
        self.reselectDirButton.clicked.connect(self.onReselectDir)
        self.reselectFileButton.clicked.connect(self.onReselectFile)
        self.srcAbsoluteButton.clicked.connect(self.onGetAbsolutePathForSource)
        self.srcRelativePathButton.clicked.connect(self.onGetRelativePathForSource)
        self.destRelativePathButton.clicked.connect(self.onGetRelativePathForDest)
        self.destBasenameButton.clicked.connect(self.onGetBasenameForDest)
        self.confirmButton.clicked.connect(self.onConfirm)

    def display(self, action, index, extra):
        self._action = action
        if self._action == self.MODIFY_EXTRA_DATA:
            self.setWindowTitle(self.tr("Modify Extra Data"))
            self.startModifyAction(extra, index)
        elif self._action == self.MODIFY_EXTRA_BIN:
            self.reselectDirButton.setEnabled(False)
            self.setWindowTitle(self.tr("Modify Extra Binary"))
            self.startModifyAction(extra, index)
        else:
            self.hide()
            return
        self.show()

    def hideEvent(self, event):
        self.actionEnd()

    def onReselectFile(self):
        path = openFileDialog(self, self.tr("Extra Data File"))
        if notNull(path):
            self.soureEdit.setText(path)
            self.destinationEdit.setText(relativePath(path, fallback=getBasename))

    def onReselectDir(self):
        path = openDirDialog(self, self.tr("Extra Data Directory"))
        if notNull(path):
            self.soureEdit.setText(path)
            self.destinationEdit.setText(relativePath(path, fallback=getBasename))

    def onGetRelativePathForSource(self):
        path = self.soureEdit.text()
        if isEmpty(path):
            return
        self.soureEdit.setText(relativePath(path))

    def onGetAbsolutePathForSource(self):
        path = self.soureEdit.text()
        if isEmpty(path):
            return
        self.soureEdit.setText(absolutePath(path))

    def onGetRelativePathForDest(self):
        path = self.destinationEdit.text()
        if isEmpty(path):
            return
        self.destinationEdit.setText(relativePath(path))

    def onGetBasenameForDest(self):
        path = self.destinationEdit.text()
        if isEmpty(path):
            return
        self.destinationEdit.setText(getBasename(path))

    def startModifyAction(self, extra, index):
        tmp = splitSrcAndDest(extra)
        self.soureEdit.setText(tmp[0])
        self.destinationEdit.setText(tmp[1])
        self._index = index

    def onConfirm(self):
        if isEmpty(self.soureEdit.text().strip()) or isEmpty(self.destinationEdit.text().strip()):
            warn(self, self.tr(u"Warning"), self.tr("Source and Destination should not be empty！"))
            return
        if self._action == self.MODIFY_EXTRA_DATA:
            self.extraDataModified.emit(self._index,
                                        joinSrcAndDest(self.soureEdit.text().strip(),
                                                       self.destinationEdit.text().strip()))
        else:
            self.extraBinaryModified.emit(self._index,
                                          joinSrcAndDest(self.soureEdit.text().strip(),
                                                         self.destinationEdit.text().strip()))
        self.accept()

    def actionEnd(self):
        self.soureEdit.setText("")
        self.destinationEdit.setText("")
        self.reselectDirButton.setEnabled(True)
        self._index = -1
        self.clearFocus()
