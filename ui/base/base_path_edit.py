# -*- coding: utf-8 -*-
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QLineEdit, QAction, QApplication, QMenu
from utils import absolutePath, ask, relativePath, isNull, notNull, isEmpty


class BasePathEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

        self.actionCopy = QAction(self, text=self.tr(u"Copy"))
        self.actionPaste = QAction(self, text=self.tr(u"Paste"))
        self.actionClear = QAction(self, text=self.tr(u"Clear"))
        self.actionRestoreDefault = QAction(self, text=self.tr(u"Restore Default"))
        self.actionAbsolutePath = QAction(self, text=self.tr(u"Absolute Path"))
        self.actionRelativePath = QAction(self, text=self.tr(u"Relative Path"))

        self.contextMenu = QMenu(self)

        self.actionRestoreDefaultHandler = None
        self.actionAbsolutePathHandler = None
        self.actionRelativePathHandler = None

        self.setupContextMenu()
        self.enableCustomContextMenu()

    def enableCustomContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu.setEnabled(True)

    def disableCustomContextMenu(self):
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.contextMenu.setEnabled(False)

    def setupActions(self):
        # 连接slot
        self.actionCopy.triggered.connect(self.onActionTriggered)
        self.actionPaste.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionRestoreDefault.triggered.connect(self.onActionTriggered)
        self.actionAbsolutePath.triggered.connect(self.onActionTriggered)
        self.actionRelativePath.triggered.connect(self.onActionTriggered)

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
        self.contextMenu.addAction(self.actionRelativePath)
        self.customContextMenuRequested.connect(self._onRequestContextMenu)

    def onActionTriggered(self):
        action = self.sender()
        handler = None
        args = []
        if action is self.actionCopy:
            if self.selectionLength() == 0:
                text = self.text().strip()
            else:
                text = self.selectedText().strip()
            if not isEmpty(text):
                clipboard = QApplication.clipboard()
                clipboard.setText(text)
        elif action is self.actionPaste:
            self.paste()
        elif action is self.actionClear:
            self.clear()
        elif action is self.actionRestoreDefault:
            handler = self.getHandler(self.actionRestoreDefaultHandler, self._actionRestoreDefaultHandler)
            args.append(self)
        elif action is self.actionAbsolutePath:
            handler = self.getHandler(self.actionAbsolutePathHandler, self._actionAbsolutePathHandler)
        elif action is self.actionRelativePath:
            handler = self.getHandler(self.actionRelativePathHandler, self._actionRelativePathHandler)
        else:
            pass

        if notNull(handler):
            handler(*args)

    def _actionAbsolutePathHandler(self):
        if ask(self, self.tr(u"Convert"), self.tr(u"Convert to absolute path?")):
            self.setText(absolutePath(self.text().strip()).strip())

    def _actionRestoreDefaultHandler(self, *args):
        self.clear()

    def _actionRelativePathHandler(self):
        if ask(self, self.tr(u"Convert"), self.tr(u"Convert to relative path?")):
            self.setText(relativePath(self.text().strip()).strip())

    def _onRequestContextMenu(self):
        self.contextMenu.exec_(QCursor.pos())

    @classmethod
    def getHandler(cls, handler, defaultHandler):
        if isNull(handler):
            return defaultHandler
        else:
            return handler
