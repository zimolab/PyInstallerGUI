# -*- coding:utf-8 -*-
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

from core.options import BindingMultipleOption
from ui.design.ui_add_items import Ui_AddItemsDialog


# noinspection PyTypeChecker
from ui.utils import warn


# noinspection PyTypeChecker
class AddItemsDialog(QDialog, Ui_AddItemsDialog):
    ADD_EXCLUDE_MODULES = 0
    ADD_HIDDEN_IMPORTS = 1
    COLLECT_ALL_SUBMODULES = 3
    COLLECT_ALL_DATA = 4
    COLLECT_ALL_BINARIES = 5
    COLLECT_ALL = 6
    COPY_METADATA = 7
    DEEP_COPY_METADATA = 8

    DEFAULT_ITEMS_SEP = ";"
    itemSeparators = {
        "semicolon(;)": ";",
        "ampersand(&)": "&",
        "comma(,)": ",",
        "colon(:)": ":",
        "slash(/)": "/",
        "backslash(\\)": "\\",
        "white space": " "
    }

    itemsAdded = Signal(BindingMultipleOption, list)

    def __init__(self, parent):
        super().__init__(parent)
        self._action = -1
        self._option = None
        self.setupUi()

    def setupUi(self, _=None):
        super(AddItemsDialog, self).setupUi(self)
        self.multiItemSeparatorCombo.addItems(self.itemSeparators.keys())
        self.addButton.clicked.connect(self.onAddItem)

    def onAddItem(self):
        content = self.itemsEdit.toPlainText().strip().replace("\n", "").replace("\r", "")
        if content == "":
            warn(self, self.tr(u"Warning"), self.tr("Items cannot be empty!"))
            return
        content = content.replace("；", ";").replace("，", ",")
        sepKey = self.multiItemSeparatorCombo.currentText()
        if sepKey in self.itemSeparators:
            sep = self.itemSeparators[sepKey]
        else:
            sep = self.DEFAULT_ITEMS_SEP
        items = content.split(sep)
        items = [item for item in items if item is not None and item != ""]
        self.itemsAdded.emit(self._option, items)
        self.accept()

    def display(self, action, option):
        self._action = action
        self._option = option
        self.updateTitle()
        self.show()

    def updateTitle(self):
        if self._action == self.ADD_EXCLUDE_MODULES:
            self.setWindowTitle(self.tr("Add Exclude Modules"))
        elif self._action == self.ADD_HIDDEN_IMPORTS:
            self.setWindowTitle(self.tr("Add Hidden Imports"))
        elif self._action == self.COLLECT_ALL_SUBMODULES:
            self.setWindowTitle(self.tr("Collect all submodules from:"))
        elif self._action == self.COLLECT_ALL_DATA:
            self.setWindowTitle(self.tr("Collect all data from:"))
        elif self._action == self.COLLECT_ALL_BINARIES:
            self.setWindowTitle(self.tr("Collect all binaries from:"))
        elif self._action == self.COLLECT_ALL:
            self.setWindowTitle(self.tr("Collect all(submodules,data, bin...) from:"))
        elif self._action == self.COPY_METADATA:
            self.setWindowTitle(self.tr("Copy metadata for:"))
        elif self._action == self.DEEP_COPY_METADATA:
            self.setWindowTitle(self.tr("Copy metadata for(recursively):"))
        else:
            raise ValueError("unknown action")


    def hideEvent(self, event):
        super().hideEvent(event)
        self._action = -1
        self._option = None
        self.setWindowTitle("")
        self.itemsEdit.setText("")

