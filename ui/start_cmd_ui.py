# -*- coding:utf-8 -*-
"""
执行命令界面
"""
import shlex
from datetime import datetime

from PySide2.QtCore import QProcess
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog, QApplication

from ui.design.ui_start_cmd import Ui_StartCommandDialog
# noinspection PyTypeChecker
from ui.utils import warn, info


# noinspection PyTypeChecker
class StartCommandDialog(QDialog, Ui_StartCommandDialog):
    START_PACK = 0
    START_GEN_SPEC_FILE = 1

    def __init__(self, parent):
        super().__init__(parent)
        self._cwd = ""
        self._cmd = ""
        self._action = -1
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

    def display(self, action, cmd, cwd):
        self._action = action

        if self._action == self.START_PACK:
            self.setWindowTitle(self.tr("Pack"))
        elif self._action == self.START_GEN_SPEC_FILE:
            self.setWindowTitle(self.tr("Generate Spec File"))
        else:
            raise ValueError("unknown action")

        self._cmd = cmd
        self._cwd = cwd
        print(shlex.split(cmd))
        self._cmdProcess.setWorkingDirectory(self._cwd)
        self.commandEdit.setPlainText(self._cmd)
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
        self._cwd = ""
        self._cmd = ""
        self._action = -1

    def closeEvent(self, event: QCloseEvent):
        if self._cmdProcess.state() != QProcess.NotRunning:
            warn(self, self.tr("Warning"), self.tr("Command is executing..."))
            event.ignore()
            return
        event.accept()

    def setupCommandEdit(self):
        def onUpdate():
            self._cmd = self.commandEdit.toPlainText()

        self.commandEdit.textChanged.connect(onUpdate)

    def setupStartButton(self):
        def onStartPack():
            if self._cmd is None or self._cmd == "":
                info(self, self.tr("Empty Command"), self.tr("Command cannot be empty"))
                return
            tmp = shlex.split(self._cmd)
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
            if self._cmd is None or self._cmd == "":
                warn(self, self.tr("Copy Command"), self.tr("Command cannot be empty"))
                return
            QApplication.clipboard().setText(self._cmd)
            warn(self, self.tr("Copy Command"), self.tr("Command is copied to the clipboard"))

        self.copyCommandButton.clicked.connect(onCopyCommand)
