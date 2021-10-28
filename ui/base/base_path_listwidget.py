# -*- coding: utf-8 -*-
from os.path import isfile, isdir

from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import QListWidget, QMenu, QAction

from utils import systemOpen, warn, ask, notNull, isNull, requestRemove, requestClear, requestPathsConversion, \
    absolutePath, relativePath


class BasePathListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.actionOpenPath = QAction(self, text=self.tr(u"Open"))
        self.actionAdd = QAction(self, text=self.tr(u"Add"))
        self.actionRemove = QAction(self, text=self.tr(u"Remove"))
        self.actionClear = QAction(self, text=self.tr(u"Clear"))
        self.actionModify = QAction(self, text=self.tr(u"Modify"))
        self.actionAbsolutePaths = QAction(self, text=self.tr(u"Absolute Paths"))
        self.actionAllAbsolutePaths = QAction(self, text=self.tr(u"Absolute Paths (All)"))
        self.actionRelativePaths = QAction(self, text=self.tr(u"Relative Paths"))
        self.actionAllRelativePaths = QAction(self, text=self.tr(u"Relative Paths (All)"))


        self.actionOpenPathHandler = None
        self.actionAddHandler = None
        self.actionRemoveHandler = None
        self.actionClearHandler = None
        self.actionModifyHandler = None
        self.actionAbsolutePathsHandler = None
        self.actionAllAbsolutePathsHandler = None
        self.actionRelativePathsHandler = None
        self.actionAllRelativePathsHandler = None

        self.bindingList = None

        self.contextMenu = QMenu(self)
        self.setupContextMenu()
        self._stateChange()
        self.disableCustomContextMenu()

    def setupActions(self):
        self.actionOpenPath.triggered.connect(self.onActionTriggered)
        self.actionAdd.triggered.connect(self.onActionTriggered)
        self.actionRemove.triggered.connect(self.onActionTriggered)
        self.actionClear.triggered.connect(self.onActionTriggered)
        self.actionModify.triggered.connect(self.onActionTriggered)
        self.actionAbsolutePaths.triggered.connect(self.onActionTriggered)
        self.actionAllAbsolutePaths.triggered.connect(self.onActionTriggered)
        self.actionRelativePaths.triggered.connect(self.onActionTriggered)
        self.actionAllRelativePaths.triggered.connect(self.onActionTriggered)


    def enableCustomContextMenu(self, bindingList):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.bindingList = bindingList
        self.contextMenu.setEnabled(True)

    def disableCustomContextMenu(self):
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.bindingList = None
        self.contextMenu.setEnabled(False)

    def setupContextMenu(self):
        self.setupActions()
        self.contextMenu.addAction(self.actionOpenPath)
        self.contextMenu.addAction(self.actionAdd)
        self.contextMenu.addAction(self.actionRemove)
        self.contextMenu.addAction(self.actionClear)
        self.contextMenu.addAction(self.actionModify)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionAbsolutePaths)
        self.contextMenu.addAction(self.actionRelativePaths)
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(self.actionAllAbsolutePaths)
        self.contextMenu.addAction(self.actionAllRelativePaths)
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
        # actionAbsolutePaths
        elif action == self.actionAbsolutePaths:
            if hasSelection:
                handler = self.getHandler(self.actionAbsolutePathsHandler, self._actionAbsolutePathsHandler)
                args.append(self.selectedItems())
        # actionAllAbsolutePaths
        elif action == self.actionAllAbsolutePaths:
            handler = self.getHandler(self.actionAllAbsolutePathsHandler, self._actionAllAbsolutePathsHandler)
            args.append(None)
        # actionRelativePathsHandler
        elif action == self.actionRelativePaths:
            if hasSelection:
                handler = self.getHandler(self.actionRelativePathsHandler, self._actionRelativePathsHandler)
                args.append(self.selectedItems())
        # actionAllRelativePaths
        elif action == self.actionAllRelativePaths:
            handler = self.getHandler(self.actionAllRelativePathsHandler, self._actionAllRelativePathsHandler)
            args.append(None)
        else:
            pass
        self._callActionHandler(handler, *args)

    def _stateChange(self):
        hasSelection = len(self.selectedItems()) > 0
        self.actionOpenPath.setEnabled(hasSelection)
        self.actionRemove.setEnabled(hasSelection)
        self.actionModify.setEnabled(hasSelection)
        self.actionAbsolutePaths.setEnabled(hasSelection)
        self.actionRelativePaths.setEnabled(hasSelection)

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
        requestRemove(self, self.bindingList, self._itemTextsOf(selectedItems))

    def _actionClearHandler(self):
        """actionClear的默认动作"""
        requestClear(self, self.bindingList)

    def _actionAbsolutePathsHandler(self, selectedItems):
        """actionToAbsolutePaths的默认动作"""
        requestPathsConversion(self, self.bindingList, self._itemTextsOf(selectedItems), absolutePath)

    def _actionAllAbsolutePathsHandler(self, _):
        """actionAllToAbsolutePaths的默认动作"""
        requestPathsConversion(self, self.bindingList, None, absolutePath)

    def _actionRelativePathsHandler(self, selectedItems):
        print("_actionRelativePathsHandler")
        requestPathsConversion(self, self.bindingList, self._itemTextsOf(selectedItems), relativePath)

    def _actionAllRelativePathsHandler(self, _):
        requestPathsConversion(self, self.bindingList, _, relativePath)

    @classmethod
    def _itemTextsOf(cls, selectedItems):
        if isNull(selectedItems) or len(selectedItems) == 0:
            return None
        return [i.text() for i in selectedItems]
