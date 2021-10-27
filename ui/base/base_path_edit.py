# -*- coding: utf-8 -*-
from os.path import abspath

from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QLineEdit, QAction, QApplication, QMenu

from core.options import DEFAULT_VALUE_UNSET
from utils import absolutePath, relativePath, baseName


class BasePathEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

        self.actionCopy = QAction(self)
        self.actionPaste = QAction(self)
        self.actionClear = QAction(self)
        self.actionAbsolutePath = QAction(self)
        self.actionRelativePath = QAction(self)
        self.actionBaseName = QAction(self)
        self.actionRestoreDefault = QAction(self)
        self.contextMenu = QMenu(self)

        self.actionRestoreDefaultHandler = None
        self.actionAbsolutePathHandler = None
        self.actionRelativePathHandler = None
        self.actionBaseNameHandler = None

        self.setupContextMenu()

    def createActions(self):
        # 设置文本
        self.actionCopy.setText(self.tr(u"Copy"))
        self.actionPaste.setText(self.tr(u"Paste"))
        self.actionClear.setText(self.tr(u"Clear"))
        self.actionRestoreDefault.setText(self.tr(u"Restore Default"))
        self.actionAbsolutePath.setText(self.tr(u"Absolute Path"))
        self.actionRelativePath.setText(self.tr(u"Relative Path"))
        self.actionBaseName.setText(self.tr(u"Basename"))
        # 连接slot
        self.actionCopy.triggered.connect(self.onActionTriggered)
        self.actionPaste.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionRestoreDefault.triggered.connect(self.onActionTriggered)
        self.actionAbsolutePath.triggered.connect(self.onActionTriggered)
        self.actionRelativePath.triggered.connect(self.onActionTriggered)
        self.actionBaseName.triggered.connect(self.onActionTriggered)

    def setupContextMenu(self):
        self.createActions()
        # 添加action
        self.contextMenu.addAction(self.actionCopy)
        self.contextMenu.addAction(self.actionPaste)
        self.contextMenu.addAction(self.actionClear)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionRestoreDefault)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionAbsolutePath)
        self.contextMenu.addAction(self.actionRelativePath)
        self.contextMenu.addAction(self.actionBaseName)
        # 设置策略
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 连接slot
        self.customContextMenuRequested.connect(self._onRequestContextMenu)

    def onActionTriggered(self):
        action = self.sender()
        processed = False
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
        elif action is self.actionRelativePath:
            if self.actionRelativePathHandler is not None:
                self.actionRelativePathHandler(self)
            else:
                self._actionRelativePathHandler()
            processed = True
        elif action is self.actionBaseName:
            if self.actionBaseNameHandler is not None:
                self.actionBaseNameHandler(self)
            else:
                self._actionBaseNameHandler()
            processed = True
        else:
            processed = False
        return processed

    def _actionAbsolutePathHandler(self):
        self.setText(absolutePath(self.text()))

    def _actionRelativePathHandler(self):
        self.setText(relativePath(self.text(), fallback=None, parent=self))

    def _actionBaseNameHandler(self):
        self.setText(baseName(self.text()))

    def _actionRestoreDefaultHandler(self):
        self.clear()

    def _onRequestContextMenu(self):
        self.contextMenu.exec_(QCursor.pos())