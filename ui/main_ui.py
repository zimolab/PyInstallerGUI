# -*- coding:utf-8 -*-
"""
主ui界面，使用pyside2实现
"""
import os
import uuid
import webbrowser
from os.path import isfile, exists, join, abspath

from PySide2 import QtCore
from PySide2.QtGui import QDropEvent, Qt
from PySide2.QtWidgets import QMainWindow, QAbstractItemView, QLineEdit
from QBinder import QEventHook, Binder

from core.package_config import PackageConfig
from ui.add_extras_ui import AddExtrasDialog
from ui.constants import FILTER_PY_SOURCE_FILE, FILTER_IMAGE_FILE, FILTER_ICON_FILE, FILTER_CONFIG_FILE, \
    PYINSTALLER_WEBSITE_URL, PYINSTALLER_DOC_STABLE_URL
from ui.design.ui_main import Ui_MainWindow
from ui.modify_path_ui import ModifyPathDialog
from ui.start_pack_ui import StartPackDialog
# noinspection PyTypeChecker
from ui.utils import ask, warn, openFileDialog, openFilesDialog, saveFileDialog, openDirDialog, error, \
    localCentralize, openDirsDialog

DEFAULT_PACKAGE_CONFIG_FILE = "package.json"


# noinspection PyTypeChecker
class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)

        self._configs = PackageConfig()
        self._commonOptions = self._configs.commonOptions
        self._upxOptions = self._configs.upxOptions
        self._hookOptions = self._configs.hookOptions
        self._windowsOptions = self._configs.windowsOptions
        self._macOSXOptions = self._configs.macOSXOptions

        self._eventHook = QEventHook.instance()

        self._state = Binder()
        self._state.cwd = abspath(os.getcwd())

        self._startPackDialog = StartPackDialog(self)
        self._addExtrasDialog = AddExtrasDialog(self)
        self._modifyPathDialog = ModifyPathDialog(self)

        self.setupUi()
        self.setupMenu()

        localCentralize(self)

        self.detectExistPackageConfigs()

    def bindConfigs(self):
        self._configs.bind("pyinstaller", self.pyinstallerEdit)
        self._configs.bind("scripts", self.scriptsListWidget)
        self._configs.bind("name", self.nameEdit)
        self._configs.bind("author", self.authorEdit)
        self._configs.bind("version", self.versionEdit)
        self._configs.bind("description", self.descriptionEdit)

        self._configs.commonOptions.productName.bind(self.productNameEdit)
        self._configs.commonOptions.distPath.bind(self.distPathEdit)
        self._configs.commonOptions.workPath.bind(self.workPathEdit)
        self._configs.commonOptions.specPath.bind(self.specPathEdit)
        self._configs.commonOptions.icon.bind(self.appIconEdit)
        self._configs.commonOptions.splash.bind(self.splashEdit)
        self._configs.commonOptions.encryptionKey.bind(self.encryptionKeyEdit)
        self._configs.commonOptions.windowMode.bind(self.windowModeCombo)
        self._configs.commonOptions.productMode.bind(self.productModeCombo)
        self._configs.commonOptions.logLevel.bind(self.logLevelCombo)
        self._configs.commonOptions.debugOption.bind(self.debugOptionCombo)
        self._configs.commonOptions.cleanBeforePack.bind(self.cleanBeforePackCheckBox)
        self._configs.commonOptions.noConfirm.bind(self.noConfirmCheckBox)
        self._configs.commonOptions.stripSymbolTable.bind(self.stripSymbolsCheckBox)
        self._configs.commonOptions.asciiOnly.bind(self.asciiOnlyCheckBox)
        self._configs.commonOptions.searchPaths.bind(self.searchPathsListWidget)
        self._configs.commonOptions.extraData.bind(self.extraDataListWidget)
        self._configs.commonOptions.extraBinaries.bind(self.extraBinariesListWidget)

        self._configs.upxOptions.noUPX.bind(self.noUPXCheckBox)
        self._configs.upxOptions.upxPath.bind(self.upxPathEdit)
        self._configs.upxOptions.excludeFiles.bind(self.upxExcludesListWidget)

        self._configs.windowsOptions.versionFile.bind(self.versionFileEdit)
        self._configs.windowsOptions.manifestFile.bind(self.manifestFileEdit)
        self._configs.windowsOptions.resource.bind(self.resourceEdit)
        self._configs.windowsOptions.uacAdmin.bind(self.uacAdminCheckBox)
        self._configs.windowsOptions.uacUIAccess.bind(self.uacUIAccessCheckBox)
        self._configs.windowsOptions.privateAssemblies.bind(self.privateAssembliesCheckBox)
        self._configs.windowsOptions.noPreferRedirects.bind(self.noPreferRedirectsCheckBox)

        self._configs.macOSXOptions.targetArchitecture.bind(self.targetArchitectureCombo)
        self._configs.macOSXOptions.codesignIdentity.bind(self.codesignIdentityEdit)
        self._configs.macOSXOptions.bundleIdentifier.bind(self.bundleIdentifierEdit)
        self._configs.macOSXOptions.entitlementsFile.bind(self.entitlementsFileEdit)

    def setupUi(self, _=None):
        super().setupUi(self)

        self.bindConfigs()

        self.setupCWDUI()
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
        self.setupWindowModeUI()
        self.setupProductModeUI()
        self.setupLogLevelUI()
        self.setupDebugOptionUI()
        self.setupCleanBeforePackUI()
        self.setupNoConfirmUI()
        self.setupStripSymbolTableUI()
        self.setupASCIIOnlyUI()
        self.setupStartPackButton()
        self.setupSearchPathsUI()
        self.setupAddExtraDataUI()
        self.setupAddExtraBinariesUI()

        self.setupUPXUI()
        self.setupWindowsOptionsUI()

    def setupMenu(self):
        # 载入配置文件
        def onLoadPackageConfigs():
            path = openFileDialog(self, self.tr("Select Configs"), None, FILTER_CONFIG_FILE)
            if path is not None:
                self.loadPackageConfigs(path)

        # 保存配置文件
        def onSavePackageConfigs():
            path = saveFileDialog(self, self.tr("Save Package Configs"),
                                  join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE))
            if path is not None:
                try:
                    self._configs.saveToFile(path)
                except Exception as e:
                    error(self, self.tr("Warning"), self.tr("Cannot save package config file!") + f"({e})")

        def onCreateNewConfigs():
            if ask(self, self.tr("New Configs"), self.tr("Current configs will be lost. Sure to create a new config?")):
                self._configs.reset()

        self.actionLoadConfigs.triggered.connect(onLoadPackageConfigs)
        self.actionSaveConfigs.triggered.connect(onSavePackageConfigs)
        self.actionStartPack.triggered.connect(self.openStartPackDialog)
        self.actionNewConfigs.triggered.connect(onCreateNewConfigs)
        self.actionGotoPyinstallerWebsite.triggered.connect(lambda: webbrowser.open(PYINSTALLER_WEBSITE_URL))
        self.actionGotoPyInstallerDoc.triggered.connect(lambda: webbrowser.open(PYINSTALLER_DOC_STABLE_URL))

    def setupCWDUI(self):
        def onPathChange(path):
            try:
                os.chdir(path)
            except Exception as e:
                warn(self, self.tr("Warning"), self.tr("Cannot change current work dir to") + path + f"({e})")
            else:
                self._state.cwd = path

        def onSelectCurrentDir():
            path = openDirDialog(self, "Change Working Dir")
            if path is not None:
                onPathChange(path)

        self.changeCWDButton.clicked.connect(onSelectCurrentDir)
        self.cwdEdit.setText(lambda: self._state.cwd * 1)
        self.cwdEdit.textChanged.connect(onPathChange)
        self.updateToolTip("Current working directory", self.cwdEdit, self.cwdLabel)

    def setupPyInstallerUI(self):
        def onSelectPyInstallerPath():
            pyinstallerPath = openFileDialog(self, self.tr("Select pyinstaller executable"), None,
                                             self.tr("pyinstaller executable(*.*)"))
            if pyinstallerPath is None:
                return
            self._configs.pyinstaller = pyinstallerPath

        self.selectPyInstallerButton.clicked.connect(onSelectPyInstallerPath)
        self.updateToolTip(self.tr("Path to pyinstaller executable"), self.pyinstallerEdit, self.pyinstallerLabel)

    def setupScriptsUI(self):
        self.scriptsListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.scriptsListWidget.itemSelectionChanged.connect(
            lambda: self.removeScriptButton.setEnabled(len(self.scriptsListWidget.selectedItems()) > 0))
        self.updateToolTip("scriptname: name of script files to be processed", self.scriptsLabel,
                           self.scriptsListWidget)

        # TODO: 为列表控件添加右键菜单，添加清空列表、打开选中文件功能等

        # 添加脚本按钮
        def onAddScript():
            scripts = openFilesDialog(self, self.tr(u"Add Script"), None,
                                      self.tr(FILTER_PY_SOURCE_FILE))
            if scripts is not None:
                self._configs.addScripts(*scripts)

        self.addScriptButton.clicked.connect(onAddScript)

        # 实现文件拖放功能
        # FIXME： 经实验，发现在QListWidget上只能触发DragEnter事件，无法触发Drop事件，这很可能是一个Bug。退而求其次，只能在addScriptButton实现文件的拖放功能了。
        def onDrop(event):
            urls = event.mimeData().urls()
            if len(urls) == 0:
                return
            scripts = [
                url.toLocalFile()
                for url in urls if
                isfile(url.toLocalFile()) and (url.toLocalFile().endswith(".py") or url.toLocalFile().endswith(".pyw"))
            ]
            self._configs.addScripts(*scripts)

        self.addScriptButton.setAcceptDrops(True)
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.DragEnter,
                                 lambda event: event.acceptProposedAction())
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.Drop, onDrop)

        # 移除脚本按钮
        def onRemoveScript():
            selected = [w.text() for w in self.scriptsListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Scripts"), self.tr("Sure to remove scripts")):
                    self._configs.removeScripts(*selected)

        self.removeScriptButton.setEnabled(False)
        self.removeScriptButton.clicked.connect(onRemoveScript)

        # 双击修改列表项
        self.scriptsListWidget.itemDoubleClicked.connect(
            lambda item: self._modifyPathDialog.display(
                ModifyPathDialog.MODIFY_SCRIPT_PATH,
                item.text(),
                self._configs.scripts.index(item.text()))
        )
        self._modifyPathDialog.scriptPathModified.connect(self._configs.updateScriptAt)

    def setupProductNameUI(self):
        self.updateToolTip(self._commonOptions.productName.description,
                           self.productNameEdit, self.productNameLabel)

    def setupDistPathUI(self):
        # 设置defaultDistPathButton
        self.defaultDistPathButton.clicked.connect(self._commonOptions.distPath.unset)

        # 设置selectDistPathButton
        def onSelectDistPath():
            path = openDirDialog(self, self.tr("Select Dist Path"))
            if path != "" and path is not None:
                self._commonOptions.distPath.argument = path

        self.selectDistPathButton.clicked.connect(onSelectDistPath)
        self.updateToolTip(self._commonOptions.distPath.description, self.distPathLabel, self.distPathEdit)

    def setupWorkPathUI(self):
        # 设置defaultWorkPathButton
        self.defaultWorkPathButton.clicked.connect(self._commonOptions.workPath.unset)

        # 设置selectWorkPathButton
        def onSelectWorkPath():
            path = openDirDialog(self, self.tr("Select Work Path"))
            if path != "" and path is not None:
                self._commonOptions.workPath.argument = path

        self.selectWorkPathButton.clicked.connect(onSelectWorkPath)
        self.updateToolTip(self._commonOptions.workPath.description, self.workPathLabel, self.workPathEdit)

    def setupSpecPathUI(self):
        def onSelectSpecPath():
            path = openDirDialog(self, self.tr("Select Spec File Path"))
            if path is not None:
                self._commonOptions.specPath.argument = path

        self.selectSpecPathButton.clicked.connect(onSelectSpecPath)
        self.defaultSpecPathButton.clicked.connect(self._commonOptions.specPath.unset)
        self.updateToolTip(self._commonOptions.specPath.description, self.specPathEdit, self.specPathLabel)

    def setupAppIconUI(self):
        self.defaultAppIconButton.clicked.connect(self._commonOptions.icon.unset)

        def onSelectIcon():
            path = openFileDialog(self, self.tr("Select App Icon"), None, self.tr(FILTER_ICON_FILE))
            if path is not None:
                self._commonOptions.icon.argument = path

        self.selectAppIconButton.clicked.connect(onSelectIcon)
        self.updateToolTip(self._commonOptions.icon.description, self.appIconEdit, self.appIconLabel)

    def setupSplashUI(self):
        self.defaultSplashButton.clicked.connect(self._commonOptions.splash.unset)

        def onSelectSplashPath():
            path = openFileDialog(
                self, self.tr("Select Splash"), None, self.tr(FILTER_IMAGE_FILE))
            if path is not None:
                self._commonOptions.splash.argument = path

        self.selectSplashButton.clicked.connect(onSelectSplashPath)
        self.updateToolTip(self._commonOptions.splash.description, self.splashLabel, self.splashEdit)

    def setupEncryptionKeyUI(self):
        self.defaultEncryptionKeyButton.clicked.connect(self._commonOptions.encryptionKey.unset)

        self.generateEncryptionKeyButton.clicked.connect(
            lambda: self._commonOptions.encryptionKey.set(uuid.uuid4().hex))

        self.updateToolTip(self._commonOptions.encryptionKey.description,
                           self.encryptionKeyEdit, self.encryptionKeyLabel)

    def setupWindowModeUI(self):
        self.updateToolTip(self._commonOptions.windowMode.description, self.windowModeCombo, self.windowModeLabel)
        self.defaultWindowModeButton.clicked.connect(self._commonOptions.windowMode.unset)

    def setupProductModeUI(self):
        self.updateToolTip(self._commonOptions.productMode.description, self.productModeCombo, self.productModelLabel)
        self.defaultProductModeButton.clicked.connect(self._commonOptions.productMode.unset)

    def setupLogLevelUI(self):
        self.updateToolTip(self._commonOptions.logLevel.description, self.logLevelLabel, self.logLevelCombo)
        self.defaultLogLevelButton.clicked.connect(self._commonOptions.logLevel.unset)

    def setupDebugOptionUI(self):
        self.updateToolTip(self._commonOptions.debugOption.description, self.debugOptionCombo, self.debugOptionLabel)
        self.defaultDebugOptionButton.clicked.connect(self._commonOptions.debugOption.unset)

    def setupCleanBeforePackUI(self):
        self.updateToolTip(self._commonOptions.cleanBeforePack.description, self.cleanBeforePackCheckBox)

    def setupNoConfirmUI(self):
        self.updateToolTip(self._commonOptions.noConfirm.description, self.noConfirmCheckBox)

    def setupStripSymbolTableUI(self):
        self.updateToolTip(self._commonOptions.stripSymbolTable.description, self.stripSymbolsCheckBox)

    def setupASCIIOnlyUI(self):
        self.updateToolTip(self._commonOptions.asciiOnly.description, self.asciiOnlyCheckBox)

    def setupStartPackButton(self):
        self.startPackButton.clicked.connect(self.openStartPackDialog)

    def setupSearchPathsUI(self):
        self.updateToolTip(self._commonOptions.searchPaths.description,
                           self.searchPathsLabel, self.searchPathsListWidget)

        # 添加搜索路径
        def onAddSearchPath():
            paths = openDirsDialog(self, self.tr("Add Search Paths"))
            if paths is not None:
                try:
                    self._commonOptions.searchPaths.addAll(True, *paths)
                except Exception as e:
                    error(self, self.tr("Error"), self.tr("Failed to add search path") + f"(error：{e})")

        self.addSearchPathButton.clicked.connect(onAddSearchPath)

        # 移除搜索路径
        def onRemoveSearchPath():
            selected = [w.text() for w in self.searchPathsListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Search Paths"), self.tr("Sure to remove search paths?")):
                    self._commonOptions.searchPaths.remove(*selected)

        self.removeSearchPathButton.setEnabled(False)
        self.removeSearchPathButton.clicked.connect(onRemoveSearchPath)
        self.searchPathsListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.searchPathsListWidget.itemSelectionChanged.connect(
            lambda: self.removeSearchPathButton.setEnabled(len(self.searchPathsListWidget.selectedItems()) > 0)
        )

        # 清除搜索路径
        self.clearSearchPathButton.clicked.connect(
            lambda: self._commonOptions.searchPaths.clear()
        )

        # 双击修改列表项
        self.searchPathsListWidget.itemDoubleClicked.connect(
            lambda item: self._modifyPathDialog.display(
                ModifyPathDialog.MODIFY_SEARCH_PATH,
                item.text(),
                self._commonOptions.searchPaths.indexOf(item.text())
            )
        )
        self._modifyPathDialog.searchPathModified.connect(self._commonOptions.searchPaths.set)

    def setupAddExtraDataUI(self):
        self.updateToolTip(self._commonOptions.extraData.description,
                           self.extraDataLabel,
                           self.extraDataListWidget)

        self.addExtraDataButton.clicked.connect(
            lambda: self._addExtrasDialog.isHidden() and self._addExtrasDialog.display(AddExtrasDialog.ADD_EXTRA_DATA))
        self._addExtrasDialog.extraDataAdded.connect(self._commonOptions.extraData.add)

        # 移除数据
        def onRemoveExtraData():
            selected = [w.text() for w in self.extraDataListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Extra Data"), self.tr("Sure to remove extra data?")):
                    self._commonOptions.extraData.remove(*selected)

        self.removeExtraDataButton.setEnabled(False)
        self.extraDataListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.extraDataListWidget.itemSelectionChanged.connect(
            lambda: self.removeExtraDataButton.setEnabled(
                len(self.extraDataListWidget.selectedItems()) > 0
            )
        )
        self.removeExtraDataButton.clicked.connect(onRemoveExtraData)

        # 文件拖放功能
        def onDrop(event):
            event: QDropEvent
            urls = event.mimeData().urls()
            sources = [url.toLocalFile() for url in urls]
            data = [self._addExtrasDialog.join(source, self._addExtrasDialog.relativePath(source)) for source in
                    sources]
            self._commonOptions.extraData.addAll(True, *data)

        self.addExtraDataButton.setAcceptDrops(True)
        self._eventHook.add_hook(self.addExtraDataButton,
                                 QtCore.QEvent.DragEnter,
                                 lambda event: event.acceptProposedAction())
        self._eventHook.add_hook(self.addExtraDataButton, QtCore.QEvent.Drop, onDrop)

        # 双击修改列表项
        self.extraDataListWidget.itemDoubleClicked.connect(
            lambda item: self._addExtrasDialog.display(
                AddExtrasDialog.MODIFY_EXTRA_DATA, item.text(),
                self._commonOptions.extraData.indexOf(item.text())
            )
        )
        self._addExtrasDialog.extraDataChanged.connect(self._commonOptions.extraData.set)

    def setupAddExtraBinariesUI(self):
        self.updateToolTip(self._commonOptions.extraBinaries.description,
                           self.extraBinariesLabel, self.extraBinariesListWidget)
        self.addExtraBinariesButton.clicked.connect(
            lambda: self._addExtrasDialog.isHidden() and self._addExtrasDialog.display(AddExtrasDialog.ADD_EXTRA_BIN))
        self._addExtrasDialog.extraBinaryAdded.connect(self._commonOptions.extraBinaries.add)

        # 移除数据
        def onRemoveExtraBinaries():
            selected = [w.text() for w in self.extraBinariesListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Extra Data"), self.tr("Sure to remove extra data?")):
                    self._commonOptions.extraBinaries.remove(*selected)

        self.removeExtraBinariesButton.setEnabled(False)
        self.extraBinariesListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.extraBinariesListWidget.itemSelectionChanged.connect(
            lambda: self.removeExtraBinariesButton.setEnabled(len(self.extraBinariesListWidget.selectedItems()) > 0))
        self.removeExtraBinariesButton.clicked.connect(onRemoveExtraBinaries)

        # 双击修改列表项
        self.extraBinariesListWidget.itemDoubleClicked.connect(
            lambda item: self._addExtrasDialog.display(
                AddExtrasDialog.MODIFY_EXTRA_BIN, item.text(),
                self._commonOptions.extraBinaries.indexOf(item.text())
            )
        )
        self._addExtrasDialog.extraBinaryChanged.connect(self._commonOptions.extraBinaries.set)

        # 文件拖放功能
        def onDrop(event):
            event: QDropEvent
            urls = event.mimeData().urls()
            sources = [url.toLocalFile() for url in urls]
            data = [self._addExtrasDialog.join(source, self._addExtrasDialog.relativePath(source)) for source in
                    sources if isfile(source)]
            self._commonOptions.extraBinaries.addAll(True, *data)
        self.addExtraBinariesButton.setAcceptDrops(True)
        self._eventHook.add_hook(self.addExtraBinariesButton, QtCore.QEvent.DragEnter,
                                 lambda event: event.acceptProposedAction())
        self._eventHook.add_hook(self.addExtraBinariesButton, QtCore.QEvent.Drop, onDrop)

    def setupUPXUI(self):
        pass

    def setupWindowsOptionsUI(self):
        pass

    def setupMacOSXOptionsUI(self):
        pass

    def updateToolTip(self, tooltip, *widgets):
        if tooltip != "" and tooltip is not None:
            tooltip = self.tr(tooltip)
            for widget in widgets:
                widget.setToolTip(tooltip)

    def loadPackageConfigs(self, path):
        try:
            self._configs.load(path, reset=True, ignoreErrors=False)
        except Exception as e:
            warn(self, self.tr("Warning"),
                 self.tr("Some errors occurred when loading configs from file!") + f"(error: {e})")

    def detectExistPackageConfigs(self):
        path = join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE)
        if exists(path):
            if ask(self, self.tr("Load Package Config"),
                   self.tr("package.json found in current path, load it?")):
                self.loadPackageConfigs(path)

    def openStartPackDialog(self):
        if self._configs.pyinstaller is None or self._configs.pyinstaller == "":
            warn(self, self.tr("Warning"), self.tr("Path of pyinstaller is empty!"))
            return
        if len(self._configs.scripts) == 0:
            warn(self, self.tr("Warning"), self.tr("Need at least one script to pack!"))
            return
        if self._startPackDialog.isHidden():
            self._startPackDialog.display(self._configs.toCommandLine(),
                                          self._state.cwd)

    def openAddExtraBinariesDialog(self):
        if self._addExtrasDialog.isHidden():
            self._addExtrasDialog.display(AddExtrasDialog.ADD_EXTRA_BIN)
