# -*- coding:utf-8 -*-
"""
封装一些实用工具
"""
import os
import platform
import subprocess
from pathlib import *

from PySide2.QtCore import QDir
from PySide2.QtWidgets import QMessageBox, QFileDialog, QApplication, QWidget, QListView, QAbstractItemView, \
    QTreeView, QInputDialog, QFontDialog

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
    return Path(selected).as_posix()


def openFilesDialog(parent, title, path=None, filters=None):
    if path is None:
        path = os.getcwd()
    files = QFileDialog.getOpenFileNames(parent, title, path, filters)[0]
    if files is None or len(files) == 0:
        return None
    return [Path(f).as_posix() for f in files]


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
    return Path(selectDir).as_posix()


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
    return [Path(p).as_posix() for p in selectedDirs]


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


def isEmpty(val):
    return val is None or val == ""


def isNotEmpty(text):
    return not isEmpty(text)


def cwd():
    return Path.cwd().as_posix()


def isFile(path):
    if isinstance(path, Path):
        return path.is_file()
    else:
        return Path(path).is_file()


def isDir(path):
    if isinstance(path, Path):
        return path.is_dir()
    else:
        return Path(path).is_dir()


def getFiles(paths, *suffixes):
    results = []
    for path in paths:
        if not isinstance(path, Path):
            path = Path(path)
        if not path.is_file():
            continue
        if len(suffixes) <= 0:
            results.append(path.as_posix())
        else:
            suffix = path.suffix
            if suffix in suffixes:
                results.append(path.as_posix())
    return results


def getDirs(paths):
    results = []
    for path in paths:
        if not isinstance(path, Path):
            path = Path(path)
        if path.is_dir():
            results.append(path.as_posix())
    return results


# noinspection PyBroadException
def getBasename(path):
    if isinstance(path, Path):
        return path.name
    else:
        path = Path(path)
        return path.name


# noinspection PyBroadException
def getBasenames(paths, filters=None):
    results = []
    for path in paths:
        try:
            if not isinstance(path, Path):
                path = Path(path)
            if filters is not None:
                if not filters(path.as_posix()):
                    continue
            results.append(path.name)
        except:
            results.append(path)
    return results


# noinspection PyBroadException
def absolutePath(path):
    if isEmpty(path) or path == DEFAULT_VALUE_UNSET:
        return path

    if not isinstance(path, Path):
        path = Path(path)

    try:
        return Path(path).absolute().as_posix()
    except Exception as e:
        return path.as_posix()


def relativePath(path, relativeTo=None, fallback=None):
    if isEmpty(path) or path == DEFAULT_VALUE_UNSET:
        return path

    if not isinstance(path, Path):
        path = Path(path)

    if isEmpty(relativeTo) or relativeTo == DEFAULT_VALUE_UNSET:
        relativeTo = cwd()

    try:
        return path.relative_to(relativeTo).as_posix()
    except ValueError:
        if fallback is None:
            return path.as_posix()
        else:
            return fallback(path.as_posix())


def isExist(path):
    if isinstance(path, Path):
        return path.exists()
    else:
        return Path(path).exists()


def joinPath(path, *other):
    if isinstance(path, Path):
        return path.joinpath(*other).as_posix()
    else:
        return Path(path).joinpath(*other).as_posix()


def systemOpen(path):
    if not isFile(path) and not isDir(path):
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


def requestRemove(parent, bindingList, itemsToRemove):
    if isNull(itemsToRemove) or len(itemsToRemove) == 0:
        return
    if ask(parent, parent.tr("Remove"), parent.tr("Remove ") + f"{len(itemsToRemove)}" + parent.tr(" item(s)?")):
        for item in itemsToRemove:
            if item in bindingList:
                bindingList.remove(item)


def requestClear(parent, bindingList):
    if isNull(bindingList) or len(bindingList) == 0:
        return
    if ask(parent, parent.tr("Clear"), parent.tr("Remove all ") + f"{len(bindingList)}" + parent.tr(" item(s)?")):
        del bindingList[:]
        bindingList.clear()


def requestPathsConversion(parent, bindingList, paths, converter, *args, **kwargs):
    if isNull(paths) or len(paths) == 0:
        if ask(parent, parent.tr("Convert"),
               parent.tr("Convert all ") + f"{len(bindingList)}" + parent.tr(" path(s)?")):
            for i in range(0, len(bindingList)):
                p = converter(bindingList[i], *args, **kwargs)
                if p in bindingList:
                    continue
                bindingList[i] = p
    else:
        if ask(parent, parent.tr("Convert"),
               parent.tr("Convert ") + f"{len(paths)}" + parent.tr(" path(s)?")):
            for path in paths:
                index = bindingList.index(path)
                if index >= 0:
                    p = converter(bindingList[index], *args, **kwargs)
                    if p in bindingList:
                        continue
                    bindingList[index] = p