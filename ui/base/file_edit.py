# -*- coding: utf-8 -*-
from os.path import isfile

from PySide2.QtGui import QDragEnterEvent, QDropEvent

from ui.base.base_path_edit import BasePathEdit


class FileEdit(BasePathEdit):
    """
    实现单个文件拖放的LineEdit
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if len(event.mimeData().urls()) != 1:
            event.ignore()
            return
        path = event.mimeData().urls()[0].toLocalFile()
        if isfile(path):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        path = event.mimeData().urls()[0].toLocalFile()
        self.setText(path)
