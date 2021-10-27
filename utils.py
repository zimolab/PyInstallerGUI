# -*- coding:utf-8 -*-
"""
封装一些实用工具
"""
import os
import platform
import subprocess
from os.path import isfile, isdir, relpath, basename, abspath

from PySide2.QtCore import QDir
from PySide2.QtWidgets import QMessageBox, QFileDialog, QApplication, QWidget, QListView, QAbstractItemView, QTreeView, \
    QInputDialog, QFontDialog

from core.options import DEFAULT_VALUE_UNSET
from ui.base.constants import ITEM_SEPARATORS


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


def openDirsDialog(parent, title):
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


def filterFiles(paths, *extensions):
    if len(extensions) == 0:
        return [path for path in paths if isfile(path)]
    else:
        return [path for path in paths if isfile(path) and hasExtension(path, *extensions)]


def hasExtension(path, *extensions):
    ext = os.path.splitext(path)[-1]
    return ext in extensions


def filterDirs(paths):
    return [path for path in paths if isdir(path)]


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


def isEmpty(text):
    return text is None or text == ""


def isNotEmpty(text):
    return not isEmpty(text)


# noinspection PyBroadException
def baseName(path):
    try:
        return basename(path)
    except Exception:
        return path


# noinspection PyBroadException
def absolutePath(path):
    if isEmpty(path) or path == DEFAULT_VALUE_UNSET:
        return path
    try:
        p = abspath(path)
    except Exception:
        return path
    else:
        return p


# noinspection PyBroadException
def relativePath(path, fallback=baseName, parent=None):
    if isEmpty(path) or path == DEFAULT_VALUE_UNSET:
        if notNull(fallback):
            return fallback(path)
        else:
            return path
    try:
        return relpath(path)
    except Exception as e:
        if notNull(parent):
            warn(parent, parent.tr("Error"), parent.tr("Cannot path convert to absolute path(error: ") + f"{e})!")
        if notNull(fallback):
            return fallback(path)
        else:
            return path


def systemOpen(path):
    if not isfile(path) and not isdir(path):
        return
    if platform.system().lower() == "windows":
        os.startfile(path)
    elif platform.system().lower() == "darwin":
        subprocess.call(["open"], path)
    else:
        subprocess.call("xdg-open", path)


def isNull(obj):
    return obj is None


def notNull(obj):
    return obj is not None


def askAndRemove(parent, bindingList, itemsToRemove):
    if isNull(itemsToRemove) or len(itemsToRemove) == 0:
        return
    if ask(parent, parent.tr("Remove"), parent.tr("Remove ") + f"{len(itemsToRemove)}" + parent.tr(" item(s)?")):
        for item in itemsToRemove:
            if item in bindingList:
                bindingList.remove(item)


def askAndClear(parent, bindingList):
    if isNull(bindingList) or len(bindingList) == 0:
        return
    if ask(parent, parent.tr("Clear"), parent.tr("Remove all ") + f"{len(bindingList)}" + parent.tr(" item(s)?")):
        del bindingList[:]
        bindingList.clear()


def askAndToAbsPaths(parent, bindingList, paths):
    if isNull(paths) or len(paths) == 0:
        if ask(parent, parent.tr("Convert to Absolute Path"),
               parent.tr("Convert all ") + f"{len(bindingList)}" + parent.tr(" items to absolute path?")):
            for i in range(0, len(bindingList)):
                p = absolutePath(bindingList[i])
                if p in bindingList:
                    continue
                bindingList[i] = p
    else:
        if ask(parent, parent.tr("Convert to Absolute Path"),
               parent.tr("Convert ") + f"{len(paths)}" + parent.tr(" items to absolute path?")):
            for path in paths:
                index = bindingList.index(path)
                if index >= 0:
                    p = absolutePath(bindingList[index])
                    if p in bindingList:
                        continue
                    bindingList[index] = p


def askAndToRelPaths(parent, bindingList, paths):
    if isNull(paths) or len(paths) == 0:
        if ask(parent, parent.tr("Convert to Relative Path"),
               parent.tr("Convert ") + f"{len(bindingList)}" + parent.tr(" items to relative path?")):
            for i in range(0, len(bindingList)):
                p = relativePath(bindingList[i], fallback=None, parent=parent)
                if p in bindingList:
                    continue
                bindingList[i] = p
    else:
        if ask(parent, parent.tr("Convert to Relative Path"),
               parent.tr("Convert ") + f"{len(paths)}" + parent.tr(" items to relative path?")):
            for path in paths:
                index = bindingList.index(path)
                if index >= 0:
                    p = relativePath(path, fallback=None, parent=parent)
                    if p in bindingList:
                        continue
                    bindingList[index] = p
