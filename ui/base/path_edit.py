# -*- coding: utf-8 -*-
from os.path import abspath

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLineEdit, QAction, QApplication

from core.options import DEFAULT_VALUE_UNSET


class PathEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.actionCopy = QAction(self)
        self.actionPaste = QAction(self)
        self.actionClear = QAction(self)
        self.actionAbsolutePath = QAction(self)
        self.actionRelativePath = QAction(self)
        self.actionRestoreDefault = QAction(self)

        self.actionRestoreDefaultHandler = None
        self.actionAbsolutePathHandler = None
        self.actionRelativePathHandler = None

        self.setupContextMenu()

    def createActions(self):
        self.actionCopy.setText(self.tr(u"Copy"))
        self.actionPaste.setText(self.tr(u"Paste"))
        self.actionClear.setText(self.tr(u"Clear"))
        self.actionRestoreDefault.setText(self.tr(u"Restore Default"))
        self.actionAbsolutePath.setText(self.tr(u"Absolute Path"))
        self.actionRelativePath.setText(self.tr(u"Relative Path"))

        self.actionCopy.triggered.connect(self.onActionTriggered)
        self.actionPaste.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionRestoreDefault.triggered.connect(self.onActionTriggered)
        self.actionAbsolutePath.triggered.connect(self.onActionTriggered)
        self.actionRelativePath.triggered.connect(self.onActionTriggered)

    def setupContextMenu(self):
        self.createActions()
        self.addAction(self.actionCopy)
        self.addAction(self.actionPaste)
        self.addAction(self.actionClear)
        self.addAction(self.actionRestoreDefault)
        self.addAction(self.actionAbsolutePath)
        self.addAction(self.actionRelativePath)

        self.setContextMenuPolicy(Qt.ActionsContextMenu)


    def onActionTriggered(self):
        action = self.sender()
        if action is self.actionCopy:
            if self.selectionLength() == 0:
                text = self.text()
            else:
                text = self.selectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
        elif action is self.actionPaste:
            self.paste()
        elif action is self.actionClear:
            self.clear()
        elif action is self.actionRestoreDefault:
            if self.actionRestoreDefaultHandler is not None:
                self.actionRestoreDefaultHandler(self)
        elif action is self.actionAbsolutePath:
            pass
        elif action is self.actionRelativePath:
            pass
        else:
            raise ValueError("unknown action")

    def _actionAbsolutePathHandler(self):
        currentPath = self.text()
        if currentPath is None or currentPath == "":
            return
        if currentPath == DEFAULT_VALUE_UNSET:
            return

    def _actionRelativePathHandler(self):
        pass