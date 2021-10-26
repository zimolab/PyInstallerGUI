# -*- coding:utf-8 -*-
"""
封装一些实用工具
"""
import os
from os.path import isfile, isdir, relpath, basename

from PySide2.QtCore import QDir
from PySide2.QtWidgets import QMessageBox, QFileDialog, QApplication, QWidget, QListView, QAbstractItemView, QTreeView, \
    QInputDialog, QLineEdit, QFontDialog

from ui.constants import ITEM_SEPARATORS


def info(parent, title, content):
    return QMessageBox.information(parent, title, content)


def warn(parent, title, content):
    return QMessageBox.warning(parent, title, content)


def error(parent, title, content):
    return QMessageBox.critical(parent, title, content)


def ask(parent, title, content):
    return QMessageBox.question(parent, title, content, QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes


def openFileDialog(parent, title, path=None, filters=None):
    if path is None:
        path = os.getcwd()
    selected = QFileDialog.getOpenFileName(parent, title, path, filters)[0]
    if selected == "":
        return None
    return selected


def openFilesDialog(parent, title, path=None, filters=None):
    if path is None:
        path = os.getcwd()
    files = QFileDialog.getOpenFileNames(parent, title, path, filters)[0]
    if files is None or len(files) == 0:
        return None
    return files


def saveFileDialog(parent, title, path=None, filters=None):
    if path is None:
        path = os.getcwd()
    savePath = QFileDialog.getSaveFileName(parent, title, path, filters)[0]
    if savePath is None or savePath == "":
        return None
    return savePath


def openDirDialog(parent, title, path=None):
    if path is None:
        path = os.getcwd()
    selectDir = QFileDialog.getExistingDirectory(parent, title, path)
    if selectDir is None or selectDir == "":
        return None
    return selectDir


def openDirsDialog(parent, title, path=None):
    if path is None:
        path = os.getcwd()
    dialog = QFileDialog(parent)
    dialog.setWindowTitle(title)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.DontUseNativeDialog)
    listView = dialog.findChild(QListView, "listView")
    if listView is not None:
        listView.setSelectionMode(QAbstractItemView.MultiSelection)

    treeView = dialog.findChild(QTreeView)
    if treeView is not None:
        treeView.setSelectionMode(QAbstractItemView.MultiSelection)

    dialog.setFilter(QDir.Dirs)
    dialog.exec_()
    selectedDirs = dialog.selectedFiles()
    return selectedDirs


def globalCentralize(w: QWidget):
    x = int((QApplication.desktop().width() - w.width()) / 2)
    y = int((QApplication.desktop().height() - w.height()) / 2)
    w.move(x, y)


def localCentralize(w: QWidget):
    currentScreen = QApplication.desktop().screenNumber(w)
    currentGeometry = QApplication.desktop().screenGeometry(currentScreen)
    x = int((currentGeometry.width() - w.width()) / 2)
    y = int((currentGeometry.height() - w.height()) / 2)
    w.move(x, y)


def joinSrcAndDest(src, dest, pathsep=None):
    if pathsep is None:
        pathsep = os.pathsep
    return f"{src}{pathsep}{dest}"


def splitSrcAndDest(joined: str, pathsep=None):
    if pathsep is None:
        result = joined.split(pathsep, maxsplit=1)
        if len(result) <= 1:
            return joined, ""
        return result

    pathsep = ";"
    tmp = joined.split(pathsep)
    if len(tmp) == 2:
        return tmp

    pathsep = ":"
    tmp = joined.split(pathsep)
    if len(tmp) == 2:
        return tmp
    return joined, ""


def filterFiles(paths):
    return [path for path in paths if isfile(path)]


def filterDirs(paths):
    return [path for path in paths if isdir(path)]


# noinspection PyBroadException
def relativePath(path, basenameIfFail=True):
    try:
        p = relpath(path)
    except Exception:
        if basenameIfFail:
            try:
                return basename(path)
            except Exception:
                return path
        else:
            return path
    else:
        return p


def getTextInput(parent, title, label, text=""):
    dialog = QInputDialog(parent)
    dialog.setWindowTitle(title)
    dialog.setLabelText(label)
    dialog.setTextValue(text)
    dialog.setFixedSize(350, 200)
    dialog.show()
    if dialog.exec_() == QInputDialog.Accepted:
        inputText = dialog.textValue()
        return inputText
    return None


def getFont(parent, initial=None, title=None):
    if title is None:
        title = parent.tr(u"Select Font")
    if initial is None:
        ok, font = QFontDialog.getFont(parent=parent, title=title)
    else:
        ok, font = QFontDialog.getFont(initial=initial, parent=parent, title=title)
    if ok:
        return font
    return None


def splitItems(content, sepKey, defaultSep=";"):
    if sepKey in ITEM_SEPARATORS:
        sep = ITEM_SEPARATORS[sepKey]
    else:
        sep = defaultSep
    items = content.split(sep)
    return [item for item in items if item is not None and item != ""]


def toBaseNames(paths, filters=None):
    results = []
    for path in paths:
        if filters is not None:
            if not filters(path):
                continue
        try:
            bn = basename(path)
        except:
            results.append(path)
        else:
            results.append(bn)
    return results
