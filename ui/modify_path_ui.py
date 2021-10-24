# -*- coding:utf-8 -*-
from os.path import relpath

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

from ui.constants import FILTER_PY_SOURCE_FILE
from ui.design.ui_modify_path import Ui_ModifyPathDialog
from ui.utils import warn, openFileDialog, openDirDialog


# noinspection PyTypeChecker
class ModifyPathDialog(QDialog, Ui_ModifyPathDialog):
    MODIFY_SCRIPT_PATH = 0
    MODIFY_SEARCH_PATH = 1

    scriptPathModified = Signal(int, str)
    searchPathModified = Signal(int, str)

    def __init__(self, parent):
        super().__init__(parent)
        self._currentIndex = -1
        self._action = -1
        self.setupUi()

    def setupUi(self, _=None):
        super(ModifyPathDialog, self).setupUi(self)
        self.confirmButton.clicked.connect(lambda: self.onPathModified() or self.accept())
        self.relpathButton.clicked.connect(self.onCalcRelPath)
        self.reselectButton.clicked.connect(self.onReselect)

    def display(self, action, originPath, index):
        self.originPathEdit.setText(originPath)
        self._currentIndex = index
        self._action = action
        self.show()

    def onCalcRelPath(self):
        try:
            rel = relpath(self.originPathEdit.text())
        except Exception as e:
            warn(self, self.tr("Warning"),
                 self.tr("Cannot get relative path of") + f"'{self.originPathEdit.text()}'(error: {e})")
        else:
            self.modifiedPathEdit.setText(rel)

    def onReselect(self):
        if self._action == self.MODIFY_SCRIPT_PATH:
            path = openFileDialog(self, self.tr("Reselect Script"), None, FILTER_PY_SOURCE_FILE)
            if path is not None:
                self.modifiedPathEdit.setText(path)
        elif self._action == self.MODIFY_SEARCH_PATH:
            path = openDirDialog(self, self.tr("Reselect Search Path"))
            if path is not None:
                self.modifiedPathEdit.setText(path)
        else:
            raise ValueError("unknown action")

    # noinspection PyUnresolvedReferences
    def onPathModified(self):
        if self._action == self.MODIFY_SCRIPT_PATH:
            self.scriptPathModified.emit(self._currentIndex, self.modifiedPathEdit.text())
        elif self._action == self.MODIFY_SEARCH_PATH:
            self.searchPathModified.emit(self._currentIndex, self.modifiedPathEdit.text())
        else:
            raise ValueError("unknown action")

    def hideEvent(self, event):
        self.originPathEdit.setText("")
        self.modifiedPathEdit.setText("")
        self._currentIndex = -1
        self._action = -1
