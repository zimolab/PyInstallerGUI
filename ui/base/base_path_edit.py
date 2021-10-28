# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QLineEdit, QAction, QApplication, QMenu

from utils import absolutePath


class BasePathEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

        self.actionCopy = QAction(self)
        self.actionPaste = QAction(self)
        self.actionClear = QAction(self)
        self.actionAbsolutePath = QAction(self)
        self.actionRestoreDefault = QAction(self)
        self.contextMenu = QMenu(self)
        self.actionRestoreDefaultHandler = None
        self.actionAbsolutePathHandler = None

        self.setupContextMenu()

    def enableCustomContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu.setEnabled(True)

    def disableCustomContextMenu(self):
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.contextMenu.setEnabled(False)

    def setupActions(self):
        # 设置文本
        self.actionCopy.setText(self.tr(u"Copy"))
        self.actionPaste.setText(self.tr(u"Paste"))
        self.actionClear.setText(self.tr(u"Clear"))
        self.actionRestoreDefault.setText(self.tr(u"Restore Default"))
        self.actionAbsolutePath.setText(self.tr(u"Absolute Path"))
        # 连接slot
        self.actionCopy.triggered.connect(self.onActionTriggered)
        self.actionPaste.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionRestoreDefault.triggered.connect(self.onActionTriggered)
        self.actionAbsolutePath.triggered.connect(self.onActionTriggered)

    def setupContextMenu(self):
        self.setupActions()
        # 添加action
        self.contextMenu.addAction(self.actionCopy)
        self.contextMenu.addAction(self.actionPaste)
        self.contextMenu.addAction(self.actionClear)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionRestoreDefault)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionAbsolutePath)
        # 连接slot
        self.customContextMenuRequested.connect(self._onRequestContextMenu)

    def onActionTriggered(self):
        action = self.sender()
        if action is self.actionCopy:
            if self.selectionLength() == 0:
                text = self.text()
            else:
                text = self.selectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            processed = True
        elif action is self.actionPaste:
            self.paste()
            processed = True
        elif action is self.actionClear:
            self.clear()
            processed = True
        elif action is self.actionRestoreDefault:
            if self.actionRestoreDefaultHandler is not None:
                self.actionRestoreDefaultHandler(self)
            else:
                self._actionRestoreDefaultHandler()
            processed = True
        elif action is self.actionAbsolutePath:
            if self.actionAbsolutePathHandler is not None:
                self.actionAbsolutePathHandler(self)
            else:
                self._actionAbsolutePathHandler()
            processed = True
        else:
            processed = False
        return processed

    def _actionAbsolutePathHandler(self):
        self.setText(absolutePath(self.text()))

    def _actionRestoreDefaultHandler(self):
        self.clear()

    def _onRequestContextMenu(self):
        self.contextMenu.exec_(QCursor.pos())