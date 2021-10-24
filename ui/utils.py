# -*- coding:utf-8 -*-

"""
封装与UI界面有关的一些实用工具，比如文件对话框等
"""
import os

from PySide2.QtCore import QDir
from PySide2.QtWidgets import QMessageBox, QFileDialog, QApplication, QWidget, QListView, QAbstractItemView, QTreeView


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
