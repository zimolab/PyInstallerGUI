# -*- coding: utf-8 -*-
from os.path import isfile

from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QListWidget, QAbstractItemView

from ui.base.base_listwidget import BasePathListWidget


class PathListWidget(BasePathListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.NoDragDrop)
        self._onDrop = None

    def dragEnterEvent(self, event: QDragEnterEvent):
        if len(event.mimeData().urls()) == 0:
            event.ignore()
            return
        event.acceptProposedAction()

    def setOnDropHandler(self, handler):
        self._onDrop = handler

    def dropEvent(self, event: QDropEvent):
        if self._onDrop is None:
            return
        dirs = [
            url.toLocalFile()
            for url in event.mimeData().urls() if isfile(url.toLocalFile())
        ]
        self._onDrop(dirs)
