# -*- coding:utf-8 -*-

"""
主ui界面，使用pyside2实现
"""
import os
import uuid
from os.path import isfile, exists, join
from PySide2 import QtCore
from PySide2.QtGui import QDropEvent
from PySide2.QtWidgets import QMainWindow, QAbstractItemView, QLineEdit
from QBinder import QEventHook, Binder
from core.package_config_states import PackageConfigStates
from core.package_configs import PackageConfigs
from ui.design.ui_main import Ui_MainWindow
from ui.start_pack_ui import StartPackUI
# noinspection PyTypeChecker
from ui.utils import ask, warn, openFileDialog, openFilesDialog, saveFileDialog, openDirDialog, error, \
    globalCentralize, localCentralize, openDirsDialog

DEFAULT_PACKAGE_CONFIG_FILE = "package.json"


# noinspection PyTypeChecker
class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)

        self._packageConfigs = PackageConfigs()
        self._commonOptions = self._packageConfigs.commonOptions
        self._upxOptions = self._packageConfigs.upxOptions
        self._hookOptions = self._packageConfigs.hookOptions
        self._windowsOptions = self._packageConfigs.windowsOptions
        self._macosOptions = self._packageConfigs.macosOptions

        self._packageConfigStates = PackageConfigStates(self._packageConfigs)

        self._eventHook = QEventHook.instance()

        self._state = Binder()
        self._state.currentWorkDir = os.getcwd()

        self._startPackUI = StartPackUI(self)

        self.setupUi(self)
        self.setupMenu()

        localCentralize(self)

        self.detectExistPackageConfigs()

    def setupUi(self, _):
        super().setupUi(_)

        self.setupCurrentWorkDirUI()
        self.setupPyInstallerUI()
        self.setupScriptsUI()
        # commonOptions
        self.setupProductNameUI()
        self.setupDistPathUI()
        self.setupWorkPathUI()
        self.setupSpecPathUI()
        self.setupAppIconUI()
        self.setupSplashUI()
        self.setupEncryptionKeyUI()
        self.setupProductModeUI()
        self.setupLogLevelUI()
        self.setupDebugOptionUI()
        self.setupCleanBeforePackUI()
        self.setupNoConfirmUI()
        self.setupStripSymbolTableUI()
        self.setupASCIIOnlyUI()
        self.setupStartPackButton()
        self.setupSearchPathsUI()

    def setupMenu(self):
        # 载入配置文件
        def onLoadPackageConfigs():
            configFile = openFileDialog(self, self.tr("Select Configs"), None, "Config File(*.json;*.*)")
            if configFile is not None:
                self.loadPackageConfigs(configFile)

        # 保存配置文件
        def onSavePackageConfigs():
            packageConfigsPath = saveFileDialog(self, self.tr("Save Package Configs"),
                                                join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE))
            if packageConfigsPath is not None:
                try:
                    self._packageConfigs.save(packageConfigsPath)
                except Exception as e:
                    error(self, self.tr("Warning"), self.tr("Cannot save package config file") + f"({e})")
                else:
                    pass

        self.actionLoadConfigs.triggered.connect(onLoadPackageConfigs)
        self.actionSaveConfigs.triggered.connect(onSavePackageConfigs)
        self.actionStartPack.triggered.connect(self.openStartPackUI)

    def setupCurrentWorkDirUI(self):
        """
        设置当前工作目录UI
        """

        def onPathChange(path):
            try:
                os.chdir(path)
            except Exception as e:
                warn(self, self.tr("Warning"), self.tr("Cannot change current work dir to") + path + f"({e})")
            else:
                self._state.currentWorkDir = path

        def onSelectCurrentDir():
            path = openDirDialog(self, self.tr("Change Working Dir"))
            if path is not None:
                onPathChange(path)

        self.changeCurrentWorkDirButton.clicked.connect(onSelectCurrentDir)
        self.currentWorkDirEdit.setText(lambda: self._state.currentWorkDir * 1)
        self.currentWorkDirEdit.textChanged.connect(onPathChange)
        self.updateToolTip(self.tr("Current working directory"), self.currentWorkDirEdit, self.currentWorkDirLabel)

    def setupPyInstallerUI(self):
        """
        设置PyInstaller UI
        """

        def onSelectPyInstallerPath():
            pyinstallerPath = openFileDialog(self, self.tr("Select pyinstaller executable"), None,
                                             self.tr("pyinstaller executable(*.*)"))
            if pyinstallerPath is None:
                return
            self._packageConfigStates.setPyInstallerPath(pyinstallerPath, updateConfigs=True)

        self.selectPyInstallerButton.clicked.connect(onSelectPyInstallerPath)
        self.pyinstallerEdit.setText(lambda: self._packageConfigStates.pyinstaller * 1)
        self.pyinstallerEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setPyInstallerPath(text, updateConfigs=True)
        )
        self.updateToolTip(self.tr("Path to pyinstaller executable"), self.pyinstallerEdit, self.pyinstallerLabel)

    def setupScriptsUI(self):
        """
        设置待打包脚本列表UI
        """
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置scriptsListWidget
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置项目选择模式：ExtendedSelection，用ctrl键选择多项
        self.scriptsListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # 处理选区变化事件
        def onSelectionChanged():
            if len(self.scriptsListWidget.selectedItems()) > 0:
                self.removeScriptButton.setEnabled(True)
            else:
                self.removeScriptButton.setEnabled(False)

        self.scriptsListWidget.itemSelectionChanged.connect(onSelectionChanged)

        # 将scriptsListWidget显示的项目与self._packageConfigStates.scripts变量进行双向绑定
        def updateItems():
            self.scriptsListWidget.clear()
            return self._packageConfigStates.scripts

        self.scriptsListWidget.addItems(updateItems)

        self.scriptsLabel.setToolTip(self.tr("scriptname: name of script files to be processed"))

        # TODO: 为列表控件添加右键菜单，添加清空列表、打开选中文件功能等
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置addScriptButton
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置按钮单击事件
        def onAddScript():
            scriptFiles = openFilesDialog(self, self.tr(u"Add Script"), None,
                                          self.tr("Python Scripts(*.py *.pyw)"))
            if scriptFiles is not None:
                self._packageConfigStates.addScripts(scriptFiles)

        self.addScriptButton.clicked.connect(onAddScript)

        # 实现文件拖放功能
        # FIXME： 经实验，发现在QListWidget上只能触发DragEnter事件，无法触发Drop事件，这很可能是一个Bug。
        #  退而求其次，只能在addScriptButton实现文件的拖放功能了。
        def onDrop(event):
            event: QDropEvent
            urls = event.mimeData().urls()
            if len(urls) == 0:
                return
            scripts = [
                url.toLocalFile()
                for url in urls if
                isfile(url.toLocalFile()) and (url.toLocalFile().endswith(".py") or url.toLocalFile().endswith(".pyw"))
            ]
            self._packageConfigStates.addScripts(scripts)

        self.addScriptButton.setAcceptDrops(True)
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.DragEnter,
                                 lambda event: event.acceptProposedAction())
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.Drop, onDrop)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置removeScriptButton
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 设置按钮单击事件
        def onRemoveScript():
            selectedScripts = [w.text() for w in self.scriptsListWidget.selectedItems()]
            if len(selectedScripts) > 0:
                if ask(self, self.tr("Remove Scripts"), self.tr("Sure to remove scripts")):
                    self._packageConfigStates.removeScripts(selectedScripts)

        self.removeScriptButton.setEnabled(False)
        self.removeScriptButton.clicked.connect(onRemoveScript)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

    def setupProductNameUI(self):
        self.updateToolTip(self._commonOptions.productName.description,
                           self.productNameEdit, self.productNameLabel)
        self.productNameEdit.setText(lambda: self._packageConfigStates.productName * 1)
        self.productNameEdit.textChanged.connect(lambda text:
                                                 self._packageConfigStates.setProductName(text, updateConfigs=True))

    def setupDistPathUI(self):
        """
        设置目录路径选项UI
        """
        # 设置distPathEdit
        self.distPathEdit.setText(lambda: self._packageConfigStates.distPath * 1)
        self.distPathEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setDistPath(text, updateConfigs=True)
        )
        # 设置defaultDistPathButton
        self.defaultDistPathButton.clicked.connect(
            lambda: self._packageConfigStates.setDistPath(None, updateConfigs=True)
        )

        # 设置selectDistPathButton
        def onSelectDistPath():
            distPath = openDirDialog(self, self.tr("Select Dist Path"))
            if distPath != "" and distPath is not None:
                self._packageConfigStates.setDistPath(distPath, updateConfigs=True)

        self.selectDistPathButton.clicked.connect(onSelectDistPath)
        self.updateToolTip(self._commonOptions.distPath.description, self.distPathLabel, self.distPathEdit)

    def setupWorkPathUI(self):
        """
        设置工作路径（构建路径）UI
        """
        # 设置workPathEdit
        self.workPathEdit.setText(lambda: self._packageConfigStates.workPath * 1)
        self.workPathEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setWorkPath(text, updateConfigs=True)
        )
        # 设置defaultWorkPathButton
        self.defaultWorkPathButton.clicked.connect(
            lambda: self._packageConfigStates.setWorkPath(None, updateConfigs=True)
        )

        # 设置selectWorkPathButton
        def onSelectWorkPath():
            workPath = openDirDialog(self, self.tr("Select Work Path"))
            if workPath != "" and workPath is not None:
                self._packageConfigStates.setWorkPath(workPath, updateConfigs=True)

        self.selectWorkPathButton.clicked.connect(onSelectWorkPath)
        self.updateToolTip(self._commonOptions.workPath.description, self.workPathLabel, self.workPathEdit)

    def setupSpecPathUI(self):
        """
        设置Spec文件路径UI
        """

        def onSelectSpecPath():
            specPath = openDirDialog(self, self.tr("Select Spec File Path"))
            if specPath is not None:
                self._packageConfigStates.setSpecPath(specPath, updateConfigs=True)

        self.selectSpecPathButton.clicked.connect(onSelectSpecPath)
        self.specPathEdit.setText(lambda: self._packageConfigStates.specPath * 1)
        self.specPathEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setSpecPath(text, updateConfigs=True)
        )
        self.defaultSpecPathButton.clicked.connect(
            lambda: self._packageConfigStates.setSpecPath(None, updateConfigs=True)
        )
        self.updateToolTip(self._commonOptions.specPath.description, self.specPathEdit, self.specPathLabel)

    def setupAppIconUI(self):
        def onSelectIcon():
            iconPath = openFileDialog(self, self.tr("Select App Icon"), None, self.tr("Icon Files(*.ico;*.icns)"))
            if iconPath is not None:
                self._packageConfigStates.setAppIcon(iconPath, updateConfigs=True)

        self.selectAppIconButton.clicked.connect(onSelectIcon)
        self.defaultAppIconButton.clicked.connect(
            lambda: self._packageConfigStates.setAppIcon(None, updateConfigs=True)
        )
        # 双向绑定
        self.appIconEdit.setText(lambda: self._packageConfigStates.appIcon * 1)
        self.appIconEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setAppIcon(text, updateConfigs=True))
        self.updateToolTip(self._commonOptions.icon.description, self.appIconEdit, self.appIconLabel)

    def setupSplashUI(self):
        def onSelectSplashPath():
            splashPath = openFileDialog(
                self, self.tr("Select Splash"), None, self.tr("Image File(*.jpg;*.jepg;*.png)"))
            if splashPath is not None:
                self._packageConfigStates.setSplash(splashPath, updateConfigs=True)

        self.selectSplashButton.clicked.connect(onSelectSplashPath)
        self.defaultSplashButton.clicked.connect(lambda: self._packageConfigStates.setSplash(None, updateConfigs=True))
        # 双向绑定
        self.splashEdit.setText(lambda: self._packageConfigStates.splash * 1)
        self.splashEdit.textChanged.connect(lambda text: self._packageConfigStates.setSplash(text, updateConfigs=True))
        self.updateToolTip(self._commonOptions.splash.description, self.splashLabel, self.splashEdit)

    def setupEncryptionKeyUI(self):
        # 双向绑定
        self.encryptionKeyEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.encryptionKeyEdit.setText(lambda: self._packageConfigStates.encryptionKey * 1)
        self.encryptionKeyEdit.textChanged.connect(
            lambda text: self._packageConfigStates.setEncryptionKey(text, updateConfigs=True))

        self.defaultEncryptionKeyButton.clicked.connect(
            lambda: self._packageConfigStates.setEncryptionKey(None, updateConfigs=True))

        self.generateEncryptionKeyButton.clicked.connect(
            lambda: self._packageConfigStates.setEncryptionKey(uuid.uuid4().hex, updateConfigs=True)
        )

        self.updateToolTip(self._commonOptions.encryptionKey.description,
                           self.encryptionKeyEdit, self.encryptionKeyLabel)

    def setupProductModeUI(self):
        self.updateToolTip(self._commonOptions.productMode.description, self.productModeCombo, self.productModelLabel)
        self.productModeCombo.addItems(self._commonOptions.productMode.argumentChoices)
        # 双向绑定
        self.productModeCombo.setCurrentText(lambda: self._packageConfigStates.productMode * 1)
        self.productModeCombo.currentTextChanged.connect(
            lambda text: self._packageConfigStates.setProductMode(text, updateConfigs=True)
        )
        self.defaultProductModeButton.clicked.connect(
            lambda: self._packageConfigStates.setProductMode(None, updateConfigs=True)
        )

    def setupLogLevelUI(self):
        self.updateToolTip(self._commonOptions.logLevel.description, self.logLevelLabel, self.logLevelCombo)
        self.logLevelCombo.addItems(self._commonOptions.logLevel.argumentChoices)
        # 双向绑定
        self.logLevelCombo.setCurrentText(lambda: self._packageConfigStates.logLevel * 1)
        self.logLevelCombo.currentTextChanged.connect(
            lambda text: self._packageConfigStates.setLogLevel(text, updateConfigs=True)
        )
        self.defaultLogLevelButton.clicked.connect(
            lambda: self._packageConfigStates.setLogLevel(None, updateConfigs=True))

    def setupDebugOptionUI(self):
        self.updateToolTip(self._commonOptions.debugOption.description, self.debugOptionCombo, self.debugOptionLabel)
        self.debugOptionCombo.addItems(self._commonOptions.debugOption.argumentChoices)
        # 双向绑定
        self.debugOptionCombo.setCurrentText(
            lambda: self._packageConfigStates.debugOption * 1
        )
        self.debugOptionCombo.currentTextChanged.connect(
            lambda text: self._packageConfigStates.setDebugOption(text, updateConfigs=True)
        )
        self.defaultDebugOptionButton.clicked.connect(
            lambda: self._packageConfigStates.setDebugOption(None, updateConfigs=True))

    def setupCleanBeforePackUI(self):
        self.updateToolTip(self._commonOptions.cleanBeforePack.description, self.cleanBeforePackCheckBox)
        # 双向绑定
        self.cleanBeforePackCheckBox.setChecked(lambda: self._packageConfigStates.cleanBeforePack * 1)
        self.cleanBeforePackCheckBox.clicked.connect(
            lambda: self._packageConfigStates.setCleanBeforePack(self.cleanBeforePackCheckBox.isChecked(),
                                                                 updateConfigs=True)
        )

    def setupNoConfirmUI(self):
        self.updateToolTip(self._commonOptions.noConfirm.description, self.noConfirmCheckBox)
        # 双向绑定
        self.noConfirmCheckBox.setChecked(lambda: self._packageConfigStates.onConfirm * 1)
        self.noConfirmCheckBox.clicked.connect(
            lambda: self._packageConfigStates.setNoConfirm(self.noConfirmCheckBox.isChecked(), updateConfigs=True)
        )

    def setupStripSymbolTableUI(self):
        self.updateToolTip(self._commonOptions.stripSymbolTable.description, self.stripSymbolsCheckBox)
        # 双向绑定
        self.stripSymbolsCheckBox.setChecked(lambda: self._packageConfigStates.stripSymbolTable * 1)
        self.stripSymbolsCheckBox.clicked.connect(
            lambda: self._packageConfigStates.setStripSymbolTable(self.stripSymbolsCheckBox.isChecked(),
                                                                  updateConfigs=True)
        )

    def setupASCIIOnlyUI(self):
        self.updateToolTip(self._commonOptions.asciiOnly.description, self.asciiOnlyCheckBox)
        # 双向绑定
        self.asciiOnlyCheckBox.setChecked(lambda: self._packageConfigStates.asciiOnly * 1)
        self.asciiOnlyCheckBox.clicked.connect(
            lambda: self._packageConfigStates.setASCIIOnly(self.asciiOnlyCheckBox.isChecked(), updateConfigs=True)
        )

    def setupStartPackButton(self):
        self.startPackButton.clicked.connect(self.openStartPackUI)

    def setupSearchPathsUI(self):
        self.updateToolTip(self._commonOptions.searchPaths.description,
                           self.searchPathsLabel, self.searchPathsListWidget)

        # 双向绑定
        def onUpdateItems():
            self.searchPathsListWidget.clear()
            return self._packageConfigStates.searchPaths

        def onAddSearchPath():
            searchPaths = openDirsDialog(self, self.tr("Add Search Path"))
            if searchPaths is not None:
                try:
                    self._packageConfigStates.addSearchPaths(searchPaths, updateConfigs=True)
                except Exception as e:
                    error(self, self.tr("Error"), self.tr("Failed to add search path") + f"(error：{e})")

        self.searchPathsListWidget.addItems(onUpdateItems)
        self.addSearchPathButton.clicked.connect(onAddSearchPath)

        # 实现移除路径功能
        def onSelectionChange():
            if len(self.searchPathsListWidget.selectedItems()) > 0:
                self.removeSearchPathButton.setEnabled(True)
            else:
                self.removeSearchPathButton.setEnabled(False)

        def onRemove():
            selected = [w.text() for w in self.searchPathsListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Search Paths"), self.tr("Sure to remove search paths")):
                    self._packageConfigStates.removeSearchPaths(selected)
        self.removeSearchPathButton.setEnabled(False)
        self.removeSearchPathButton.clicked.connect(onRemove)
        self.searchPathsListWidget.itemSelectionChanged.connect(onSelectionChange)
        self.searchPathsListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def updateToolTip(self, tooltip, *widgets):
        if tooltip != "" and tooltip is not None:
            tooltip = self.tr(tooltip)
            for widget in widgets:
                widget.setToolTip(tooltip)

    def loadPackageConfigs(self, configFile):
        try:
            newConfigs = PackageConfigs.load(configFile, ignoreErrors=False)
        except Exception as e:
            warn(self, self.tr("Warning"), self.tr("Cannot read package config file") + f"(error: {e})")
        else:
            self._packageConfigs = None
            self._packageConfigs = newConfigs
            self._commonOptions = self._packageConfigs.commonOptions
            self._upxOptions = self._packageConfigs.upxOptions
            self._hookOptions = self._packageConfigs.hookOptions
            self._windowsOptions = self._packageConfigs.windowsOptions
            self._macosOptions = self._packageConfigs.macosOptions
            self._packageConfigStates.changeConfigs(self._packageConfigs)

    def detectExistPackageConfigs(self):
        configPath = join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE)
        if exists(configPath):
            if ask(self, self.tr("Load Package Config"),
                   self.tr("package.json found in current path, load it?")):
                self.loadPackageConfigs(configPath)

    def openStartPackUI(self):
        if self._startPackUI.isHidden():
            self._startPackUI.display(self._packageConfigs.toPakCommand(),
                                      self._state.currentWorkDir)
