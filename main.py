# -*- coding:utf-8 -*-
"""
一个将PyInstaller工具图形化的小工具。方便调整PyInstaller命令的各种参数。
图形界面使用PySide2编写。
"""
import sys
from PySide2.QtWidgets import QApplication
from ui.main_ui import MainUI

configs = {
    "fontSize": 12
}


def startUI():
    app = QApplication(sys.argv)
    font = app.font()
    font.setPointSize(configs["fontSize"])
    app.setFont(font)
    mainUI = MainUI()
    mainUI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    startUI()
