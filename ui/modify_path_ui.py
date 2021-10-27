# -*- coding:utf-8 -*-
from os.path import relpath, abspath

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

from ui.base.constants import FILTER_PY_SOURCE_FILE
from ui.base.ui_modify_path import Ui_ModifyPathDialog
from utils import warn, openFileDialog, openDirDialog


# noinspection PyTypeChecker
class ModifyPathDialog(QDialog, Ui_ModifyPathDialog):
    MODIFY_SCRIPT_PATH = 0
    MODIFY_SEARCH_PATH = 1
    MODIFY_ADDITIONAL_HOOKS_DIR = 2
    MODIFY_RUNTIME_HOOKS = 3

    scriptPathModified = Signal(int, str)
    searchPathModified = Signal(int, str)
    additionalHooksDirModified = Signal(int, str)
    runtimeHooksModified = Signal(int, str)

    def __init__(self, parent):
        super().__init__(parent)
        self._currentIndex = -1
        self._action = -1
        self.setupUi()

    def setupUi(self, _=None):
        super(ModifyPathDialog, self).setupUi(self)
        self.confirmButton.clicked.connect(self.onConfirm)
        self.relpathButton.clicked.connect(self.onCalcRelPath)
        self.abspathButton.clicked.connect(self.onCalcAbsPath)
        self.reselectButton.clicked.connect(self.onReselect)

    def display(self, action, originPath, index):
        self.originPathEdit.setText(originPath)
        self._currentIndex = index
        self._action = action
        self.updateTitle()
        self.show()

    def onCalcRelPath(self):
        try:
            rel = relpath(self.originPathEdit.text())
        except Exception as e:
            warn(self, self.tr("Warning"),
                 self.tr("Cannot get relative path of") + f"'{self.originPathEdit.text()}'(error: {e})")
        else:
            self.modifiedPathEdit.setText(rel)

    def onCalcAbsPath(self):
        try:
            _abspath = abspath(self.originPathEdit.text())
        except Exception as e:
            warn(self, self.tr("Warning"),
                 self.tr("Cannot get absolute path of") + f"'{self.originPathEdit.text()}'(error: {e})")
        else:
            self.modifiedPathEdit.setText(_abspath)

    def onReselect(self):
        if self._action == self.MODIFY_SCRIPT_PATH:
            path = openFileDialog(self, self.tr("Reselect Script"), None, FILTER_PY_SOURCE_FILE)
            if path is not None:
                self.modifiedPathEdit.setText(path)
        elif self._action == self.MODIFY_SEARCH_PATH:
            path = openDirDialog(self, self.tr("Reselect Search Path"))
            if path is not None:
                self.modifiedPathEdit.setText(path)
        elif self._action == self.MODIFY_ADDITIONAL_HOOKS_DIR:
            path = openDirDialog(self, self.tr("Reselect Additional Hooks Dir"))
            if path is not None:
                self.modifiedPathEdit.setText(path)
        elif self._action == self.MODIFY_RUNTIME_HOOKS:
            path = openFileDialog(self, self.tr("Reselect Runtime Hooks"), filters=FILTER_PY_SOURCE_FILE)
            if path is not None:
                self.modifiedPathEdit.setText(path)
        else:
            raise ValueError("unknown action")

    def onConfirm(self):
        modified = self.modifiedPathEdit.text()
        if modified == "":
            warn(self, self.tr("Warning"), self.tr("path cannot be empty"))
            return
        else:
            self.onPathModified()
            self.accept()

    # noinspection PyUnresolvedReferences
    def onPathModified(self):
        if self._action == self.MODIFY_SCRIPT_PATH:
            signal = self.scriptPathModified
        elif self._action == self.MODIFY_SEARCH_PATH:
            signal = self.searchPathModified
        elif self._action == self.MODIFY_ADDITIONAL_HOOKS_DIR:
            signal = self.additionalHooksDirModified
        elif self._action == self.MODIFY_RUNTIME_HOOKS:
            signal = self.runtimeHooksModified
        else:
            raise ValueError("unknown action")
        signal.emit(self._currentIndex, self.modifiedPathEdit.text())

    def updateTitle(self):
        if self._action == self.MODIFY_SCRIPT_PATH:
            title = self.tr("Modify Script Path")
        elif self._action == self.MODIFY_SEARCH_PATH:
            title = self.tr("Modify Search Path")
        elif self._action == self.MODIFY_ADDITIONAL_HOOKS_DIR:
            title = self.tr("Modify Additional Hooks Dir")
        elif self._action == self.MODIFY_RUNTIME_HOOKS:
            title = self.tr("Modify Runtime Hooks")
        else:
            raise ValueError("unknown action")
        self.setWindowTitle(title)

    def hideEvent(self, event):
        self.originPathEdit.setText("")
        self.modifiedPathEdit.setText("")
        self.setWindowTitle("")
        self._currentIndex = -1
        self._action = -1
