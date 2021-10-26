# -*- coding:utf-8 -*-
from os.path import isfile

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QDialog

from core.options import BindingMultipleOption
from ui.constants import ITEM_SEPARATORS
from ui.design.ui_upx_excludes import Ui_UPXExcludesDialog


# noinspection PyTypeChecker
from ui.utils import warn, splitItems, openFilesDialog, toBaseNames


# noinspection PyTypeChecker,PyUnresolvedReferences
class UPXExcludesDialog(QDialog, Ui_UPXExcludesDialog):
    DEFAULT_SEP = ";"
    upxExcludesAdded = Signal(list, BindingMultipleOption)

    def __init__(self, parent):
        super().__init__(parent)
        self._option = None
        self.setupUi()

    def setupUi(self, _=None):
        super(UPXExcludesDialog, self).setupUi(self)
        self.filenameSeparatorCombo.addItems(ITEM_SEPARATORS.keys())
        self.addButton.clicked.connect(self.onAddUPXExcludes)
        self.selectButton.clicked.connect(self.onSelectUPXExcludes)

    def display(self, option):
        self._option = option
        self.show()

    def onAddUPXExcludes(self):
        content = self.filenamesEdit.toPlainText().strip().replace("\n", "").replace("\r", "")
        if content == "":
            warn(self, self.tr(u"Warning"), self.tr("Items cannot be empty!"))
            return
        content = content.replace("；", ";").replace("，", ",")
        sepKey = self.filenameSeparatorCombo.currentText()
        items = splitItems(content, sepKey, self.DEFAULT_SEP)
        if isinstance(items, list) and isinstance(self._option, BindingMultipleOption):
            self.upxExcludesAdded.emit(items, self._option)
            self.accept()
        else:
            self.reject()

    def onSelectUPXExcludes(self):
        filenames = openFilesDialog(self, self.tr("Select UPX Exclude Files"))
        if filenames is not None:
            excludes = toBaseNames(filenames, isfile)
            if len(excludes) > 0:
                sepKey = self.filenameSeparatorCombo.currentText()
                if sepKey in ITEM_SEPARATORS:
                    sep = ITEM_SEPARATORS[sepKey]
                else:
                    sep = self.DEFAULT_SEP
                content = sep.join(excludes)
                currentContent = self.filenamesEdit.toPlainText()
                if currentContent.endswith(sep):
                    self.filenamesEdit.setPlainText(currentContent + content)
                else:
                    self.filenamesEdit.setPlainText(currentContent + sep + content)

    def hideEvent(self, event):
        self.filenamesEdit.setPlainText("")
        self._option = None
