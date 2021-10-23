# -*- coding:utf-8 -*-
"""
执行打包操作的GUI界面
"""
import shlex
from datetime import datetime
from PySide2.QtCore import QProcess
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog, QApplication
from ui.design.ui_start_pack import Ui_StartPackDialog
# noinspection PyTypeChecker
from ui.utils import warn, info


# noinspection PyTypeChecker
class StartPackUI(QDialog, Ui_StartPackDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.cwd = ""
        self.cmd = ""
        self._cmdProcess = QProcess(self)
        self.setupUi(self)
        self.setupCMDProcess()

    def setupUi(self, _):
        super().setupUi(_)
        self.setupCommandEdit()
        self.setupStartButton()
        self.setupTerminateButton()
        self.setupClearOutputButton()
        self.setupCopyCommandButton()

    def setupCMDProcess(self):
        self._cmdProcess.setReadChannel(QProcess.StandardOutput)
        self._cmdProcess.errorOccurred.connect(self.onErrorOccurred)
        self._cmdProcess.finished.connect(self.onCommandFinished)
        self._cmdProcess.readyReadStandardError.connect(self.onStderrReadyRead)
        self._cmdProcess.readyReadStandardOutput.connect(self.onStdoutReadyRead)
        self._cmdProcess.started.connect(self.onCommandStarted)

    def display(self, cmd, cwd):
        self.cmd = cmd
        self.cwd = cwd
        self._cmdProcess.setWorkingDirectory(self.cwd)
        self.commandEdit.setPlainText(self.cmd)
        self.show()

    def onCommandStarted(self):
        self.startButton.setDisabled(True)
        self.outputTextBrowser.append(f"[{datetime.now()}]" + self.tr("Start"))

    def onCommandFinished(self, exitCode, exitStatus):
        self.startButton.setEnabled(True)
        self.outputTextBrowser.append(
            f"[{datetime.now()}]" + self.tr("Finished") + f"(exitCode={exitCode} exitStatus={exitStatus})"
        )

    def onStdoutReadyRead(self):
        output = self._cmdProcess.readAllStandardOutput()
        self.outputTextBrowser.append(bytes(output).decode())

    def onStderrReadyRead(self):
        output = self._cmdProcess.readAllStandardError()
        self.outputTextBrowser.append(bytes(output).decode())

    def onErrorOccurred(self, error):
        self.outputTextBrowser.append(f"[{datetime.now()}]" + self.tr("An error occurred:") + f"{error}")

    def hideEvent(self, event):
        super().hideEvent(event)
        self.cwd = ""
        self.cmd = None

    def closeEvent(self, event: QCloseEvent):
        if self._cmdProcess.state() != QProcess.NotRunning:
            warn(self, self.tr("Warning"), self.tr("Command is executing..."))
            event.ignore()
            return
        event.accept()

    def setupCommandEdit(self):
        def onUpdate():
            self.cmd = self.commandEdit.toPlainText()

        self.commandEdit.textChanged.connect(onUpdate)

    def setupStartButton(self):
        def onStartPack():
            if self.cmd is None or self.cmd == "":
                info(self, self.tr("Empty Command"), self.tr("Command cannot be empty"))
                return
            tmp = shlex.split(self.cmd)
            cmd = tmp[0]
            args = tmp[1:]
            self.outputTextBrowser.append(f"{cmd} {args}")
            self._cmdProcess.start(cmd, args)

        self.startButton.clicked.connect(onStartPack)

    def setupTerminateButton(self):
        def onTerminatePack():
            if self._cmdProcess.state() != QProcess.NotRunning:
                self._cmdProcess.kill()

        self.terminateButton.clicked.connect(onTerminatePack)

    def setupClearOutputButton(self):

        self.clearOutputButton.clicked.connect(lambda: self.outputTextBrowser.setText(""))

    def setupCopyCommandButton(self):
        def onCopyCommand():
            if self.cmd is None or self.cmd == "":
                warn(self, self.tr("Copy Command"), self.tr("Command cannot be empty"))
                return
            QApplication.clipboard().setText(self.cmd)
            warn(self, self.tr("Copy Command"), self.tr("Command is copied to the clipboard"))
        self.copyCommandButton.clicked.connect(onCopyCommand)
