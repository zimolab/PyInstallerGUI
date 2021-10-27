# -*- coding: utf-8 -*-
from os.path import isfile, isdir

from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QListWidget, QMenu, QAction

from utils import systemOpen, warn, ask, notNull, isNull, askAndRemove, askAndClear, askAndToAbsPaths, askAndToRelPaths


class BasePathListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.actionOpenPath = QAction(self, text=self.tr(u"Open"))
        self.actionAdd = QAction(self, text=self.tr(u"Add"))
        self.actionRemove = QAction(self, text=self.tr(u"Remove"))
        self.actionClear = QAction(self, text=self.tr(u"Clear"))
        self.actionModify = QAction(self, text=self.tr(u"Modify"))
        self.actionToAbsolutePaths = QAction(self, text=self.tr(u"Absolute Paths"))
        self.actionToRelativePaths = QAction(self, text=self.tr(u"Relative Paths"))
        self.actionAllToAbsolutePaths = QAction(self, text=self.tr(u"Absolute Paths (All)"))
        self.actionAllToRelativePaths = QAction(self, text=self.tr(u"Relative Paths (All)"))

        self.actionOpenPathHandler = None
        self.actionAddHandler = None
        self.actionRemoveHandler = None
        self.actionClearHandler = None
        self.actionModifyHandler = None
        self.actionToAbsolutePathsHandler = None
        self.actionToRelativePathsHandler = None
        self.actionAllToAbsolutePathsHandler = None
        self.actionAllToRelativePathsHandler = None

        self.bindingList = None

        self.contextMenu = QMenu(self)
        self.setupContextMenu()
        self._stateChange()

    def setupActions(self):
        self.actionOpenPath.triggered.connect(self.onActionTriggered)
        self.actionAdd.triggered.connect(self.onActionTriggered)
        self.actionRemove.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionModify.triggered.connect(self.onActionTriggered)
        self.actionToAbsolutePaths.triggered.connect(self.onActionTriggered)
        self.actionToRelativePaths.triggered.connect(self.onActionTriggered)
        self.actionAllToAbsolutePaths.triggered.connect(self.onActionTriggered)
        self.actionAllToRelativePaths.triggered.connect(self.onActionTriggered)

    def enableCustomContextMenu(self, enabled):
        if not enabled:
            self.setContextMenuPolicy(Qt.NoContextMenu)
        else:
            self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu.setEnabled(enabled)

    def setupContextMenu(self):
        self.setupActions()
        self.contextMenu.addAction(self.actionOpenPath)
        self.contextMenu.addAction(self.actionAdd)
        self.contextMenu.addAction(self.actionRemove)
        self.contextMenu.addAction(self.actionClear)
        self.contextMenu.addAction(self.actionModify)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionToAbsolutePaths)
        self.contextMenu.addAction(self.actionToRelativePaths)
        self.contextMenu.addAction(self.actionAllToAbsolutePaths)
        self.contextMenu.addAction(self.actionAllToRelativePaths)
        # 连接slot
        self.customContextMenuRequested.connect(self._onRequestContextMenu)
        self.itemSelectionChanged.connect(self._stateChange)

    def onActionTriggered(self):
        action = self.sender()
        handler = None
        args = []
        hasSelection = len(self.selectedItems()) > 0
        # actionOpenPath
        if action == self.actionOpenPath:
            if hasSelection:
                handler = self.getHandler(self.actionOpenPathHandler, self._actionOpenPathHandler)
                args.append(self.selectedItems())
        # actionAdd
        elif action == self.actionAdd:
            handler = self.getHandler(self.actionAddHandler, self._handlerNotImplemented)
        # actionRemove
        elif action == self.actionRemove:
            if hasSelection:
                handler = self.getHandler(self.actionRemoveHandler, self._actionRemoveHandler)
                args.append(self.selectedItems())
        # actionClear
        elif action == self.actionClear:
            handler = self.getHandler(self.actionClearHandler, self._actionClearHandler)
        # actionModify
        elif action == self.actionModify:
            if hasSelection:
                handler = self.getHandler(self.actionModifyHandler, self._handlerNotImplemented)
                args.append(self.selectedItems()[0])
        # actionToAbsolutePaths
        elif action == self.actionToAbsolutePaths:
            if hasSelection:
                handler = self.getHandler(self.actionToAbsolutePathsHandler, self._actionToAbsolutePathsHandler)
                args.append(self.selectedItems())
        elif action == self.actionToRelativePaths:
            if hasSelection:
                handler = self.getHandler(self.actionToRelativePathsHandler, self._actionToRelativePathsHandler)
                args.append(self.selectedItems())
        # actionAllToAbsolutePaths
        elif action == self.actionAllToAbsolutePaths:
            handler = self.getHandler(self.actionAllToAbsolutePathsHandler, self._actionAllToAbsolutePathsHandler)
            args.append(None)
        # actionAllToRelativePaths
        elif action == self.actionAllToRelativePaths:
            handler = self.getHandler(self.actionAllToRelativePathsHandler, self._actionAllToRelativePathsHandler)
            args.append(None)
        else:
            pass
        self._callActionHandler(handler, *args)

    def _stateChange(self):
        hasSelection = len(self.selectedItems()) > 0
        self.actionRemove.setEnabled(hasSelection)
        self.actionModify.setEnabled(hasSelection)
        self.actionToAbsolutePaths.setEnabled(hasSelection)
        self.actionToRelativePaths.setEnabled(hasSelection)
        self.actionOpenPath.setEnabled(hasSelection)

    def _onRequestContextMenu(self):
        self.contextMenu.exec_(QCursor.pos())

    @classmethod
    def _callActionHandler(cls, handler, *args, **kwargs):
        if notNull(handler):
            handler(*args, **kwargs)

    @classmethod
    def getHandler(cls, handler, defaultHandler):
        if notNull(handler):
            return handler
        return defaultHandler

    def _handlerNotImplemented(self, *args, **kwargs):
        """_actionAdd的默认动作"""
        warn(self, "Warning", "ACTION HANDLER NOT IMPLEMENTED!")

    def _actionOpenPathHandler(self, selectedItems):
        """actionOpenPath的默认动作"""
        paths = self._itemTextsOf(selectedItems)
        if isNull(paths):
            return
        if ask(self, self.tr(u"Open"), self.tr("Open ") + f"{len(paths)}" + self.tr(" paths?")):
            for path in paths:
                if isfile(path) or isdir(path):
                    systemOpen(path)
                else:
                    warn(self, self.tr("Warning"), f'"{path}"' + self.tr(" is not exist"))

    def _actionRemoveHandler(self, selectedItems):
        """actionRemove的默认动作"""
        askAndRemove(self, self.bindingList, self._itemTextsOf(selectedItems))

    def _actionClearHandler(self):
        """actionClear的默认动作"""
        askAndClear(self, self.bindingList)

    def _actionToAbsolutePathsHandler(self, selectedItems):
        """actionToAbsolutePaths的默认动作"""
        askAndToAbsPaths(self, self.bindingList, self._itemTextsOf(selectedItems))

    def _actionToRelativePathsHandler(self, selectedItems):
        """actionToRelativePaths的默认动作"""
        askAndToRelPaths(self, self.bindingList, self._itemTextsOf(selectedItems))

    def _actionAllToAbsolutePathsHandler(self, _):
        """actionAllToAbsolutePaths的默认动作"""
        askAndToAbsPaths(self, self.bindingList, None)

    def _actionAllToRelativePathsHandler(self, _):
        """actionAllToRelativePaths的默认动作"""
        askAndToRelPaths(self, self.bindingList, None)

    @classmethod
    def _itemTextsOf(cls, selectedItems):
        if isNull(selectedItems) or len(selectedItems) == 0:
            return None
        return [i.text() for i in selectedItems]
