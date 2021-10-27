# -*- coding:utf-8 -*-
"""
主ui界面，使用pyside2实现
"""
import os
import uuid
import webbrowser
from os.path import isfile, exists, join, abspath
from pathlib import Path
from typing import Union

from PySide2 import QtCore
from PySide2.QtGui import QDropEvent
from PySide2.QtWidgets import QMainWindow, QAbstractItemView, QLineEdit, QPushButton, QLabel, QCheckBox, QRadioButton, \
    QComboBox, QListWidget, QApplication, QStyleFactory, QAction, QActionGroup
from QBinder import QEventHook, Binder

from core.constants import DEFAULT_PYINSTALLER_PATH, DEFAULT_PYIMAKESPEC_PATH
from core.options import BindingOption, BindingFlag, BindingMultipleOption
from core.package_config import PackageConfig
from ui.add_extras_ui import AddExtrasDialog
from ui.add_items_ui import AddItemsDialog
from ui.base.constants import FILTER_PY_SOURCE_FILE, FILTER_IMAGE_FILE, FILTER_ICON_FILE, FILTER_CONFIG_FILE, \
    PYINSTALLER_WEBSITE_URL, PYINSTALLER_DOC_STABLE_URL, FILTER_ALL_FILE, FILTER_MANIFEST_FILE, FILTER_RESOURCE_FILE, \
    FILTER_ENTITLEMENTS_FILE
from ui.base.ui_main import Ui_MainWindow
from ui.modify_path_ui import ModifyPathDialog
from ui.start_cmd_ui import StartCommandDialog
# noinspection PyTypeChecker
from ui.upx_excludes_ui import UPXExcludesDialog
from utils import ask, warn, openFileDialog, openFilesDialog, saveFileDialog, openDirDialog, error, \
    localCentralize, openDirsDialog, filterDirs, joinSrcAndDest, relativePath, getTextInput, getFont, toBaseNames, \
    filterFiles

DEFAULT_PACKAGE_CONFIG_FILE = "package.json"


# noinspection PyTypeChecker
class MainUI(QMainWindow, Ui_MainWindow):
    SELECT_FILE = 0
    SELECT_FILES = 1
    SELECT_DIR = 2
    SELECT_DIRS = 3
    SELECT_BOTH = 4

    def __init__(self):
        super().__init__(None)
        # 创建配置对象
        self._configs = PackageConfig()
        self._commonOptions = self._configs.commonOptions
        self._upxOptions = self._configs.upxOptions
        self._hookOptions = self._configs.hookOptions
        self._windowsOptions = self._configs.windowsOptions
        self._macOSXOptions = self._configs.macOSXOptions
        # 获取EventHook
        self._eventHook = QEventHook.instance()
        # 创建响应式对象
        self._state = Binder()
        self._state.cwd = abspath(os.getcwd())
        # 创建对话框或其他窗口
        self._startCommandDialog = StartCommandDialog(self)
        self._addExtrasDialog = AddExtrasDialog(self)
        self._modifyPathDialog = ModifyPathDialog(self)
        self._addItemsDialog = AddItemsDialog(self)
        self._upxExcludesDialog = UPXExcludesDialog(self)
        # 设置UI
        self.setupUi()
        # 设置菜单
        self.setupMenu()
        # 自动探测当前目录下是否存在配置文件，并询问是否打开
        self.detectExistPackageConfigs()

    def setupUi(self, _=None):
        super().setupUi(self)
        # 居中显示窗口
        localCentralize(self)
        # 设置非Options部分的UI
        self.setupNonOptionsUI()
        # 设置Options部分的UI
        # -常规选项部分的UI
        self.setupCommonOptionsUI()
        # -UPX选项的UI
        self.setupUPXOptionsUI()
        # -Hooks选项的UI
        self.setupHookOptionsUI()
        # -windows平台专属选项的UI
        self.setupWindowsOptionsUI()
        # -macOSX平台专属选项的UI
        self.setupMacOSXOptionsUI()

    def setupMenu(self):
        """设置菜单"""
        self.actionLoadConfigs.triggered.connect(self.onLoadPackageConfigs)
        self.actionSaveConfigs.triggered.connect(self.onSavePackageConfigs)
        self.actionStartPack.triggered.connect(self.startPack)
        self.actionNewConfigs.triggered.connect(self.onCreateNewConfigs)
        self.actionGotoPyinstallerWebsite.triggered.connect(lambda: webbrowser.open(PYINSTALLER_WEBSITE_URL))
        self.actionGotoPyInstallerDoc.triggered.connect(lambda: webbrowser.open(PYINSTALLER_DOC_STABLE_URL))
        self.actionStartGenSpceFile.triggered.connect(self.startGenerateSpecFile)
        self.actionChangeFont.triggered.connect(self.onChangeFont)
        self.setupStylesMenu()

    def setupStylesMenu(self):
        """添加界面风格菜单"""

        def onActionTriggered(action: QAction):
            key = action.data()
            try:
                style = QStyleFactory.create(key)
            except:
                warn(self, self.tr("Warning"), self.tr(f"Cannot set style of '{key}'"))
                action.setChecked(False)
            else:
                QApplication.instance().setStyle(style)

        styleNames = QStyleFactory.keys()
        group = QActionGroup(self)
        group.setExclusive(True)
        group.triggered.connect(onActionTriggered)
        for styleName in styleNames:
            styleAction = QAction(self)
            styleAction.setText(styleName)
            styleAction.setCheckable(True)
            group.addAction(styleAction)
            styleAction.setData(styleName)

        self.menuStyles.addActions(group.actions())

    def setupScriptsUI(self):
        self.setTooltip("scriptname: name of script files to be processed", self.scriptsLabel, self.scriptsListWidget)
        # 绑定数据
        self._configs.bind("scripts", self.scriptsListWidget)

        def onAddScript():
            scripts = openFilesDialog(self, self.tr(u"Add Script"), None, self.tr(FILTER_PY_SOURCE_FILE))
            if scripts is not None:
                self._configs.addScripts(*scripts)
        # 添加脚本
        self.addScriptButton.clicked.connect(onAddScript)

        def onRemoveScripts():
            selected = [w.text() for w in self.scriptsListWidget.selectedItems()]
            if len(selected) > 0:
                if ask(self, self.tr("Remove Scripts"), self.tr("Remove scripts?")):
                    self._configs.removeScripts(*selected)
        # 移除脚本
        self.removeScriptButton.setEnabled(False)
        self.removeScriptButton.clicked.connect(onRemoveScripts)
        self.scriptsListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.scriptsListWidget.itemSelectionChanged.connect(
            lambda: self.removeScriptButton.setEnabled(len(self.scriptsListWidget.selectedItems()) > 0))

        def onClearScripts():
            if ask(self, self.tr("Remove Scripts"), self.tr("Clear scripts?")):
                self._configs.clearScripts()
        # 清除全部脚本
        self.clearScriptsButton.clicked.connect(onClearScripts)

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
        # 文件拖放，实现在按钮上
        self.addScriptButton.setAcceptDrops(True)
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.DragEnter,
                                 lambda event: event.acceptProposedAction())
        self._eventHook.add_hook(self.addScriptButton, QtCore.QEvent.Drop, onDrop)

        self.scriptsListWidget.itemDoubleClicked.connect(
            lambda item: self._modifyPathDialog.display(
                ModifyPathDialog.MODIFY_SCRIPT_PATH,
                item.text(),
                self._configs.scripts.index(item.text()))
        )
        # 双击修改
        self._modifyPathDialog.scriptPathModified.connect(self._configs.updateScriptAt)

    def setupNonOptionsUI(self):
        # cwd
        def onChangeCWD(path):
            if path is None:
                return
            try:
                os.chdir(path)
            except Exception as e:
                warn(self, self.tr("Warning"), self.tr("Cannot change current working dir to") + path + f"({e})")
            else:
                self._state.cwd = path

        self.changeCWDButton.clicked.connect(
            lambda: onChangeCWD(openDirDialog(self, self.tr("Change Working Directory"))))
        self.cwdEdit.contextMenu.setEnabled(False)
        self.cwdEdit.setText(lambda: self._state.cwd * 1)
        self.cwdEdit.textChanged.connect(onChangeCWD)
        self.setTooltip(self.tr("current working directory"), self.cwdEdit, self.cwdLabel)

        # pyinstaller & pyimakespec
        def restoreDefault(edit):
            if edit == self.pyinstallerEdit:
                self._configs.pyinstaller = DEFAULT_PYINSTALLER_PATH
            elif edit == self.pyimakespecEdit:
                self._configs.pyimakespec = DEFAULT_PYIMAKESPEC_PATH
            else:
                raise ValueError("unknown edit")

        # pyinstaller
        def onChangePyInstallerPath():
            path = openFileDialog(self, self.tr("Select pyinstaller executable"), None,
                                  self.tr("pyinstaller executable(*.*)"))
            if path is None:
                return
            self._configs.pyinstaller = path
        # 绑定数据
        self._configs.bind("pyinstaller", self.pyinstallerEdit)
        self.pyinstallerEdit.actionRestoreDefaultHandler = restoreDefault
        self.selectPyInstallerButton.clicked.connect(onChangePyInstallerPath)
        self.setTooltip(self.tr("Path to pyinstaller executable"), self.pyinstallerEdit, self.pyinstallerLabel)

        # pyimakespec
        def onChangePyimakespecPath():
            path = openFileDialog(self, self.tr("Select pyi-makespec executable"), None,
                                  self.tr("pyi-makespec executable(*.*)"))
            if path is None:
                return
            self._configs.pyimakespec = path
        # 绑定数据
        self._configs.bind("pyimakespec", self.pyimakespecEdit)
        self.pyimakespecEdit.actionRestoreDefaultHandler = restoreDefault
        self.selectPyimakespecButton.clicked.connect(onChangePyimakespecPath)
        self.setTooltip(self.tr("Path to pyi-makespec executable"), self.pyimakespecEdit, self.pyimakespecLabel)
        # scripts
        self.setupScriptsUI()
        # name
        self._configs.bind("name", self.nameEdit)
        # author
        self._configs.bind("author", self.authorEdit)
        # version
        self._configs.bind("version", self.versionEdit)
        # description
        self._configs.bind("description", self.descriptionEdit)
        # 开始打包按钮
        self.startPackButton.clicked.connect(self.startPack)

    def setupCommonOptionsUI(self):
        # productName
        self.autosetTextInputUI(option=self._commonOptions.productName, label=self.productNameLabel,
                                edit=self.productNameEdit, defaultButton=self.defaultProductNameButton)
        # distPath
        self.autosetPathSelectionUI(option=self._commonOptions.distPath, label=self.distPathLabel,
                                    edit=self.distPathEdit, selectButton=self.selectDistPathButton,
                                    defaultButton=self.defaultDistPathButton, selectionMode=self.SELECT_DIR)
        # workPath
        self.autosetPathSelectionUI(option=self._commonOptions.workPath, label=self.workPathLabel,
                                    edit=self.workPathEdit, selectButton=self.selectWorkPathButton,
                                    defaultButton=self.defaultWorkPathButton, selectionMode=self.SELECT_DIR)
        # specPath
        self.autosetPathSelectionUI(option=self._commonOptions.specPath, label=self.specPathLabel,
                                    edit=self.specPathEdit, selectButton=self.selectSpecPathButton,
                                    defaultButton=self.defaultSpecPathButton, selectionMode=self.SELECT_DIR)
        # icon
        self.autosetPathSelectionUI(option=self._commonOptions.icon, label=self.appIconLabel, edit=self.appIconEdit,
                                    selectButton=self.selectAppIconButton, defaultButton=self.defaultAppIconButton,
                                    selectionMode=self.SELECT_FILE, filters=FILTER_ICON_FILE)
        # splash
        self.autosetPathSelectionUI(option=self._commonOptions.splash, label=self.splashLabel, edit=self.splashEdit,
                                    selectButton=self.selectSplashButton, defaultButton=self.defaultSplashButton,
                                    selectionMode=self.SELECT_FILE, filters=FILTER_IMAGE_FILE)
        # key
        self.autosetTextInputUI(option=self._commonOptions.key, label=self.encryptionKeyLabel,
                                edit=self.encryptionKeyEdit, defaultButton=self.defaultEncryptionKeyButton)
        self.generateEncryptionKeyButton.clicked.connect(
            lambda: self._commonOptions.key.set(uuid.uuid4().hex))
        # windowMode
        self.autosetChoiceUI(self._commonOptions.windowMode, self.windowModeLabel, self.windowModeCombo,
                             self.defaultWindowModeButton)
        # productMode
        self.autosetChoiceUI(self._commonOptions.productMode, self.productModelLabel, self.productModeCombo,
                             self.defaultProductModeButton)
        # logLevel
        self.autosetChoiceUI(self._commonOptions.logLevel, self.logLevelLabel, self.logLevelCombo,
                             self.defaultLogLevelButton)
        # debug
        self.autosetChoiceUI(self._commonOptions.debug, self.debugOptionLabel, self.debugOptionCombo,
                             self.defaultDebugOptionButton)
        # cleanBeforePack
        self.autosetFlagUI(flag=self._commonOptions.clean, flagBox=self.cleanBeforePackCheckBox)
        # noConfirm
        self.autosetFlagUI(flag=self._commonOptions.noConfirm, flagBox=self.noConfirmCheckBox)
        # strip
        self.autosetFlagUI(flag=self._commonOptions.strip, flagBox=self.stripSymbolsCheckBox)
        # asciiOnly
        self.autosetFlagUI(flag=self._commonOptions.asciiOnly, flagBox=self.asciiOnlyCheckBox)
        # bootloaderIgnoreSignals
        self.autosetFlagUI(flag=self._commonOptions.bootloaderIgnoreSignals, flagBox=self.ignoreSignalsCheckBox)
        # disableWindowedTraceback
        self.autosetFlagUI(flag=self._commonOptions.disableWindowedTraceback,
                           flagBox=self.disableWindowedTracebackCheckBox)

        # paths & runtimeTmpDir
        def onAddSearchPaths(paths, option: BindingMultipleOption):
            if paths is None:
                paths = openDirsDialog(self, self.tr("Add Directory"))
            else:
                paths = filterDirs(paths)
            if paths is None or len(paths) == 0:
                return
            option.addAll(True, *paths)

        def onModifySearchPath(path, index, option):
            self._modifyPathDialog.display(ModifyPathDialog.MODIFY_SEARCH_PATH, path, index)

        self.autosetMultiItemsUI(option=self._commonOptions.paths, label=self.searchPathsLabel,
                                 listWidget=self.searchPathsListWidget, addButton=self.addSearchPathButton,
                                 removeButton=self.removeSearchPathButton, clearButton=self.clearSearchPathButton,
                                 onAdd=onAddSearchPaths,
                                 onModify=onModifySearchPath)
        self._modifyPathDialog.searchPathModified.connect(self._commonOptions.paths.set)

        # addData & addBinary
        def onAddExtras(paths, option: BindingMultipleOption):
            if paths is None:
                if option.name == self._commonOptions.addBinary.name:
                    self._addExtrasDialog.display(AddExtrasDialog.ADD_EXTRA_BIN)
                elif option.name == self._commonOptions.addData.name:
                    self._addExtrasDialog.display(AddExtrasDialog.ADD_EXTRA_DATA)
                else:
                    pass
                return
            elif isinstance(paths, str):
                paths = [paths]
            else:
                if option.name == self._commonOptions.addData.name:
                    paths = [joinSrcAndDest(path, relativePath(path)) for path in paths]
                elif option.name == self._commonOptions.addBinary.name:
                    paths = [joinSrcAndDest(path, relativePath(path)) for path in paths if isfile(path)]
                else:
                    return
            option.addAll(True, *paths)

        def onModifyExtras(path, index, option):
            if option.name == self._commonOptions.addData.name:
                self._addExtrasDialog.display(AddExtrasDialog.MODIFY_EXTRA_DATA, path, index)
            elif option.name == self._commonOptions.addBinary.name:
                self._addExtrasDialog.display(AddExtrasDialog.MODIFY_EXTRA_BIN, path, index)
            else:
                pass

        # extraData
        self.autosetMultiItemsUI(option=self._commonOptions.addData, label=self.extraDataLabel,
                                 listWidget=self.extraDataListWidget, addButton=self.addExtraDataButton,
                                 removeButton=self.removeExtraDataButton, clearButton=self.clearExtraData,
                                 onAdd=onAddExtras, onModify=onModifyExtras)
        self._addExtrasDialog.extraDataAdded.connect(lambda path: onAddExtras(path, self._commonOptions.addData))
        self._addExtrasDialog.extraDataChanged.connect(self._commonOptions.addData.set)
        # extraBinaries
        self.autosetMultiItemsUI(option=self._commonOptions.addBinary, label=self.extraBinariesLabel,
                                 listWidget=self.extraBinariesListWidget, addButton=self.addExtraBinariesButton,
                                 removeButton=self.removeExtraBinariesButton, clearButton=self.clearExtraBinariesButton,
                                 onAdd=onAddExtras, onModify=onModifyExtras)
        self._addExtrasDialog.extraBinaryAdded.connect(
            lambda path: onAddExtras(path, self._commonOptions.addBinary))
        self._addExtrasDialog.extraBinaryChanged.connect(self._commonOptions.addBinary.set)

        # excludeModule & hiddenImports & collectSubmodules & collectData & collectBinaries & collectAll &
        # copyMetadata & recursiveCopyMetadata
        def onAddItem(_, option: BindingMultipleOption):
            if option.name == self._commonOptions.excludeModule.name:
                self._addItemsDialog.display(AddItemsDialog.ADD_EXCLUDE_MODULES, option)
            elif option.name == self._commonOptions.hiddenImports.name:
                self._addItemsDialog.display(AddItemsDialog.ADD_HIDDEN_IMPORTS, option)
            elif option.name == self._commonOptions.collectSubmodules.name:
                self._addItemsDialog.display(AddItemsDialog.COLLECT_ALL_SUBMODULES, option)
            elif option.name == self._commonOptions.collectData.name:
                self._addItemsDialog.display(AddItemsDialog.COLLECT_ALL_DATA, option)
            elif option.name == self._commonOptions.collectBinaries.name:
                self._addItemsDialog.display(AddItemsDialog.COLLECT_ALL_BINARIES, option)
            elif option.name == self._commonOptions.collectAll.name:
                self._addItemsDialog.display(AddItemsDialog.COLLECT_ALL, option)
            elif option.name == self._commonOptions.copyMetadata.name:
                self._addItemsDialog.display(AddItemsDialog.COPY_METADATA, option)
            elif option.name == self._commonOptions.recursiveCopyMetadata.name:
                self._addItemsDialog.display(AddItemsDialog.DEEP_COPY_METADATA, option)
            else:
                raise ValueError("unknown action")

        def onModifyItem(item, index, option: BindingMultipleOption):
            modified = getTextInput(self, self.tr("Modify"), self.tr("To be modified:"), item)
            if modified is not None:
                option.set(index, modified, True)

        def onItemsAdded(option, items):
            option.addAll(True, *items)

        self._addItemsDialog.itemsAdded.connect(onItemsAdded)

        # excludeModules
        self.autosetMultiItemsUI(option=self._commonOptions.excludeModule, label=self.excludeModulesLabel,
                                 listWidget=self.excludeModulesListWidget, addButton=self.addExcludeModulesButton,
                                 removeButton=self.removeExcludeModulesButton,
                                 clearButton=self.clearExcludeModulesButton,
                                 onAdd=onAddItem, enableDrop=False, onModify=onModifyItem)
        # hiddenImports
        self.autosetMultiItemsUI(option=self._commonOptions.hiddenImports, label=self.hiddenImportLabel,
                                 listWidget=self.hiddenImportsListWidget, addButton=self.addHiddenImportButton,
                                 removeButton=self.removeHiddenImportButton,
                                 clearButton=self.clearHiddenImportsButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # collectSubmodules
        self.autosetMultiItemsUI(option=self._commonOptions.collectSubmodules, label=self.collectSubmodulesLabel,
                                 listWidget=self.collectSubmodulesListWidget, addButton=self.addCollectSubmodulesButton,
                                 removeButton=self.removeCollectSubmodulesButton,
                                 clearButton=self.clearCollectSubmodulesButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # collectData
        self.autosetMultiItemsUI(option=self._commonOptions.collectData, label=self.collectDataLabel,
                                 listWidget=self.collectDataListWidget, addButton=self.addCollectDataButton,
                                 removeButton=self.removeCollectDataButton,
                                 clearButton=self.clearCollectDataButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)
        # collectBinaries
        self.autosetMultiItemsUI(option=self._commonOptions.collectBinaries, label=self.collectBinariesLabel,
                                 listWidget=self.collectBinariesListWidget, addButton=self.addCollectBinariesButton,
                                 removeButton=self.removeCollectBinariesButton,
                                 clearButton=self.clearCollectBinariesButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # collectAll
        self.autosetMultiItemsUI(option=self._commonOptions.collectAll, label=self.collectAllLabel,
                                 listWidget=self.collectAllListWidget, addButton=self.addCollectAllButton,
                                 removeButton=self.removeCollectAllButton,
                                 clearButton=self.clearCollectAllButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # copyMetadata
        self.autosetMultiItemsUI(option=self._commonOptions.copyMetadata, label=self.copyMetadataLabel,
                                 listWidget=self.copyMetadataListWidget, addButton=self.addCopyMetadataButton,
                                 removeButton=self.removeCopyMetadataButton,
                                 clearButton=self.clearCopyMetadataButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # deepcopyMetadata
        self.autosetMultiItemsUI(option=self._commonOptions.recursiveCopyMetadata, label=self.deepcopyMetadataLabel,
                                 listWidget=self.deepcopyMetadataListWidget, addButton=self.addDeepcopyMetadataButton,
                                 removeButton=self.removeDeepcopyMetadataButton,
                                 clearButton=self.clearDeepcopyMetadataButton,
                                 onAdd=onAddItem, enableDrop=False,
                                 onModify=onModifyItem)

        # runtimeTmpDir
        self.autosetPathSelectionUI(option=self._commonOptions.runtimeTmpDir, label=self.rtTmpDirLabel,
                                    edit=self.rtTmpDirEdit, selectButton=self.selectRTTmpDirButton,
                                    defaultButton=self.defaultRTTmpDirButton, selectionMode=self.SELECT_DIR,
                                    startPath=str(Path.home()))

    def setupUPXOptionsUI(self):
        """设置UPX选项界面"""
        # noUPX
        self.autosetFlagUI(flag=self._upxOptions.noUPX, flagBox=self.noUPXCheckBox)
        # upxDir
        self.autosetPathSelectionUI(option=self._upxOptions.upxDir, label=self.upxPathLabel, edit=self.upxPathEdit,
                                    selectButton=self.selectUPXPathButton, defaultButton=self.defaultUPXPathButton,
                                    selectionMode=self.SELECT_DIR)

        # upxExclude
        def onAdd(paths, option: BindingMultipleOption):
            if paths is None:
                self._upxExcludesDialog.display(option)
            else:
                excludes = toBaseNames(paths, filters=isfile)
                option.addAll(True, *excludes)

        def onModify(path, index, option: BindingMultipleOption):
            modified = getTextInput(self, self.tr("Modify UPX Exclude"), self.tr("Exclude Filename："), path)
            if modified is not None:
                option.set(index, modified, True)
        # upxExclude
        self.autosetMultiItemsUI(option=self._upxOptions.upxExclude, label=self.upxExcludesLabel,
                                 listWidget=self.upxExcludesListWidget, addButton=self.addUPXExcludesButton,
                                 removeButton=self.removeUPXExcludesButton, clearButton=self.clearUPXExcludesButton,
                                 onAdd=onAdd, onModify=onModify)
        self._upxExcludesDialog.upxExcludesAdded.connect(lambda excludes, option: option.addAll(True, *excludes))

    def setupWindowsOptionsUI(self):
        # versionFile
        self.autosetPathSelectionUI(option=self._windowsOptions.versionFile, label=self.versionFileLabel,
                                    edit=self.versionFileEdit, selectButton=self.selectVersionFileButton,
                                    defaultButton=self.defaultVersionFileButton, selectionMode=self.SELECT_FILE)
        # manifest
        self.autosetPathSelectionUI(option=self._windowsOptions.manifest, label=self.manifestFileLabel,
                                    edit=self.manifestFileEdit, selectButton=self.selectManifestFileButton,
                                    defaultButton=self.defaultManifestFileButton, selectionMode=self.SELECT_FILE,
                                    filters=FILTER_MANIFEST_FILE)
        # resource
        self.autosetPathSelectionUI(option=self._windowsOptions.resource, label=self.resourceLabel,
                                    edit=self.resourceEdit, selectButton=self.selectResourceButton,
                                    defaultButton=self.defaultResourceButton, selectionMode=self.SELECT_FILE,
                                    filters=FILTER_RESOURCE_FILE)
        # uacAdmin
        self.autosetFlagUI(flag=self._windowsOptions.uacAdmin, flagBox=self.uacAdminCheckBox)
        # uacUIAccess
        self.autosetFlagUI(flag=self._windowsOptions.uacUIAccess, flagBox=self.uacUIAccessCheckBox)
        # winPrivateAssemblies
        self.autosetFlagUI(flag=self._windowsOptions.winPrivateAssemblies, flagBox=self.privateAssembliesCheckBox)
        # winNoPreferRedirects
        self.autosetFlagUI(flag=self._windowsOptions.winNoPreferRedirects, flagBox=self.noPreferRedirectsCheckBox)

    def setupMacOSXOptionsUI(self):
        # entitlementsFile
        self.autosetPathSelectionUI(option=self._macOSXOptions.entitlementsFile, label=self.entitlementsFileLabel,
                                    edit=self.entitlementsFileEdit, selectButton=self.selectEntitlementsFileButton,
                                    defaultButton=self.defaultEntitlementsFileButton, selectionMode=self.SELECT_FILE,
                                    filters=FILTER_ENTITLEMENTS_FILE)
        # targetArchitecture
        self.autosetChoiceUI(option=self._macOSXOptions.targetArchitecture, label=self.targetArchitectureLabel,
                             choicesBox=self.targetArchitectureCombo,
                             defaultButton=self.defaultTargetArchitectureButton)
        # osxBundleIdentifier
        self.autosetTextInputUI(option=self._macOSXOptions.osxBundleIdentifier, label=self.bundleIdentifierLabel,
                                edit=self.bundleIdentifierEdit, defaultButton=self.defaultBundleIdentifierButton)
        # codesignIdentity
        self.autosetTextInputUI(option=self._macOSXOptions.codesignIdentity, label=self.codesignIdentityLabel,
                                edit=self.codesignIdentityEdit, defaultButton=self.defaultCodesignIdentityButton)

    def setupHookOptionsUI(self):
        def onAdd(paths, option: BindingMultipleOption):
            if paths is None:
                if option.name == self._hookOptions.additionalHooksDir.name:
                    paths = openDirsDialog(self, self.tr("Add Additional Hooks Directories"))
                else:
                    paths = openFilesDialog(self, self.tr("Add Runtime Hooks"), filters=FILTER_PY_SOURCE_FILE)
                if paths is None:
                    return
            else:
                if option.name == self._hookOptions.additionalHooksDir.name:
                    paths = filterDirs(paths)
                else:
                    paths = filterFiles(paths, ".py", ".pyw")
                if paths is None or len(paths) == 0:
                    return
            option.addAll(True, *paths)

        def onModify(path, index, option: BindingMultipleOption):
            if option.name == self._hookOptions.additionalHooksDir.name:
                self._modifyPathDialog.display(ModifyPathDialog.MODIFY_ADDITIONAL_HOOKS_DIR, path, index)
            else:
                self._modifyPathDialog.display(ModifyPathDialog.MODIFY_RUNTIME_HOOKS, path, index)
        # additionalHooksDir
        self.autosetMultiItemsUI(option=self._hookOptions.additionalHooksDir, label=self.hookDirsLabel,
                                 listWidget=self.hookDirsListWidget, addButton=self.addHookDirsButton,
                                 removeButton=self.removeHookDirsButton, clearButton=self.clearHookDirsButton,
                                 onAdd=onAdd, onModify=onModify)
        self._modifyPathDialog.additionalHooksDirModified.connect(
            lambda index, modified: self._hookOptions.additionalHooksDir.set(index, modified, True))
        # runtimeHook
        self.autosetMultiItemsUI(option=self._hookOptions.runtimeHook, label=self.rtHooksLabel,
                                 listWidget=self.rtHooksListWidget, addButton=self.addRTHooksButton,
                                 removeButton=self.removeRTHooksButton, clearButton=self.clearRTHooksButton,
                                 onAdd=onAdd, onModify=onModify)
        self._modifyPathDialog.runtimeHooksModified.connect(
            lambda index, modified: self._hookOptions.runtimeHook.set(index, modified, True))

    def autosetPathSelectionUI(self, option: BindingOption, label: QLabel, edit: QLineEdit, selectButton: QPushButton,
                               defaultButton: QPushButton, selectionMode, filters=None, startPath=None):
        if startPath is None:
            startPath = os.getcwd()

        if selectionMode != self.SELECT_FILE and selectionMode != self.SELECT_DIR:
            raise ValueError(f"unsupported selectionMode of {selectionMode}")

        if selectionMode == self.SELECT_FILE or selectionMode == self.SELECT_FILES:
            if filters is None:
                filters = FILTER_ALL_FILE
        self.setTooltip(option.description, edit, label)
        option.bind(edit)
        if defaultButton is not None:
            defaultButton.clicked.connect(option.unset)

        def onSelectPath():
            if selectionMode == self.SELECT_FILE:
                selected = openFileDialog(self, self.tr("Select File"), path=startPath, filters=filters)
            else:
                selected = openDirDialog(self, self.tr("Select Directory"), path=startPath)

            if selected is not None:
                option.set(selected)

        selectButton.clicked.connect(onSelectPath)

    def autosetFlagUI(self, flag: BindingFlag, flagBox: Union[QCheckBox, QRadioButton], defaultButton=None):
        self.setTooltip(flag.description, flagBox)
        flag.bind(flagBox)

        if defaultButton is not None:
            defaultButton.clicked.connect(flag.unset)

    def autosetChoiceUI(self, option: BindingOption, label: QLabel, choicesBox: QComboBox, defaultButton=None):
        if option.choices is None:
            raise ValueError("option without choices")

        self.setTooltip(option.description, label, choicesBox)
        option.bind(choicesBox)

        if defaultButton is not None:
            defaultButton.clicked.connect(option.unset)

    def autosetTextInputUI(self, option: BindingOption, label: QLabel, edit: QLineEdit, defaultButton=None):
        self.setTooltip(option.description, label, edit)
        option.bind(edit)
        if defaultButton is not None:
            defaultButton.clicked.connect(option.unset)

    def autosetMultiItemsUI(self, option: BindingMultipleOption, label: QLabel, listWidget: QListWidget,
                            addButton: QPushButton = None, removeButton: QPushButton = None,
                            clearButton: QPushButton = None, onAdd=None, onModify=None, enableDrop=True):
        self.setTooltip(option.description, label, listWidget)
        # 绑定数据
        option.bind(listWidget)

        # 移除数据
        if removeButton is not None:
            def onRemoveItems():
                selected = [w.text() for w in listWidget.selectedItems()]
                if len(selected) > 0:
                    if ask(self, self.tr("Remove"), self.tr("Are you sure to remove these items?")):
                        option.remove(*selected)

            removeButton.setEnabled(len(listWidget.selectedItems()) > 0)
            listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
            listWidget.itemSelectionChanged.connect(
                lambda: removeButton.setEnabled(len(listWidget.selectedItems()) > 0))
            removeButton.clicked.connect(onRemoveItems)

        # 清除全部数据
        if clearButton is not None:
            def onClear():
                if ask(self, self.tr("Clear Items"), self.tr("CLEAR ALL ITEMS?")):
                    option.clear()

            clearButton.clicked.connect(onClear)

        # 双击修改列表项
        if onModify is not None:
            listWidget.itemDoubleClicked.connect(
                lambda item: onModify(item.text(), option.indexOf(item.text()), option))

        # 添加数据与文件拖放
        if onAdd is not None and addButton is not None:
            # 添加数据
            addButton.clicked.connect(lambda: onAdd(None, option))
            # 文件拖放
            if enableDrop:
                def onDrop(event):
                    event: QDropEvent
                    urls = event.mimeData().urls()
                    paths = [url.toLocalFile() for url in urls]
                    onAdd(paths, option)

                # FIXME: 经过尝试，发现直接在QListWidget实现文件拖放功能存在一些问题，因此将文件拖放功能实现在按钮上
                addButton.setAcceptDrops(True)
                self._eventHook.add_hook(addButton, QtCore.QEvent.DragEnter, lambda event: event.acceptProposedAction())
                self._eventHook.add_hook(addButton, QtCore.QEvent.Drop, onDrop)

    def setTooltip(self, tooltip, *widgets):
        """为控件设置tool tip"""
        if tooltip != "" and tooltip is not None:
            tooltip = self.tr(tooltip)
            for widget in widgets:
                widget.setToolTip(tooltip)

    def loadPackageConfigs(self, path):
        """读取配置文件"""
        try:
            self._configs.load(path, reset=True, ignoreErrors=False)
        except Exception as e:
            warn(self, self.tr("Warning"),
                 self.tr("Some errors occurred when loading configs from file!") + f"(error: {e})")

    def detectExistPackageConfigs(self):
        """检查当前路径下是否存在配置文件，并询问是否打开"""
        path = join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE)
        if exists(path):
            if ask(self, self.tr("Load Package Config"),
                   self.tr("package.json found in current path, load it?")):
                self.loadPackageConfigs(path)

    def startPack(self):
        self.openStartCommandDialog(self._configs.pyinstaller, StartCommandDialog.START_PACK)

    def startGenerateSpecFile(self):
        self.openStartCommandDialog(self._configs.pyimakespec, StartCommandDialog.START_GEN_SPEC_FILE)

    def openStartCommandDialog(self, cmd, action):
        if cmd is None or cmd == "":
            warn(self, self.tr("Warning"), self.tr("cmd executable is empty!"))
            return
        if len(self._configs.scripts) == 0:
            warn(self, self.tr("Warning"), self.tr("Need at least one script!"))
            return
        self._startCommandDialog.display(action, self._configs.toCommandLine(cmd),
                                         self._state.cwd)

    def onLoadPackageConfigs(self):
        """载入配置文件"""
        path = openFileDialog(self, self.tr("Select Configs"), None, FILTER_CONFIG_FILE)
        if path is not None:
            self.loadPackageConfigs(path)

    def onSavePackageConfigs(self):
        """保持配置文件"""
        path = saveFileDialog(self, self.tr("Save Package Configs"),
                              join(os.getcwd(), DEFAULT_PACKAGE_CONFIG_FILE))
        if path is not None:
            try:
                self._configs.saveToFile(path)
            except Exception as e:
                error(self, self.tr("Warning"), self.tr("Cannot save package config file!") + f"({e})")

    def onCreateNewConfigs(self):
        """创建新的配置对象"""
        if ask(self, self.tr("New Configs"), self.tr("Current configs will be lost. Sure to create a new config?")):
            self._configs.reset()

    def onChangeFont(self):
        app = QApplication.instance()
        currentFont = app.font()
        font = getFont(self, initial=currentFont)
        if font is not None:
            app.setFont(font)
