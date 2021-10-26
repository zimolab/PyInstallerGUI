# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzhdIYF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .directory_edit import DirectoryEdit
from .file_edit import FileEdit
from .file_listwidget import FileListWidget
from .directory_listwidget import DirectoryListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 933)
        MainWindow.setAcceptDrops(True)
        self.actionStartPack = QAction(MainWindow)
        self.actionStartPack.setObjectName(u"actionStartPack")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSaveConfigs = QAction(MainWindow)
        self.actionSaveConfigs.setObjectName(u"actionSaveConfigs")
        self.actionLoadConfigs = QAction(MainWindow)
        self.actionLoadConfigs.setObjectName(u"actionLoadConfigs")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionNewConfigs = QAction(MainWindow)
        self.actionNewConfigs.setObjectName(u"actionNewConfigs")
        self.actionGotoPyinstallerWebsite = QAction(MainWindow)
        self.actionGotoPyinstallerWebsite.setObjectName(u"actionGotoPyinstallerWebsite")
        self.actionGotoPyInstallerDoc = QAction(MainWindow)
        self.actionGotoPyInstallerDoc.setObjectName(u"actionGotoPyInstallerDoc")
        self.actionStartGenSpceFile = QAction(MainWindow)
        self.actionStartGenSpceFile.setObjectName(u"actionStartGenSpceFile")
        self.actionChangeFont = QAction(MainWindow)
        self.actionChangeFont.setObjectName(u"actionChangeFont")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.mainTabWidget = QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.commonTab = QWidget()
        self.commonTab.setObjectName(u"commonTab")
        self.verticalLayout_2 = QVBoxLayout(self.commonTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cwdLabel = QLabel(self.commonTab)
        self.cwdLabel.setObjectName(u"cwdLabel")

        self.gridLayout_2.addWidget(self.cwdLabel, 0, 0, 1, 1)

        self.changeCWDButton = QPushButton(self.commonTab)
        self.changeCWDButton.setObjectName(u"changeCWDButton")

        self.gridLayout_2.addWidget(self.changeCWDButton, 0, 2, 1, 1)

        self.pyinstallerLabel = QLabel(self.commonTab)
        self.pyinstallerLabel.setObjectName(u"pyinstallerLabel")

        self.gridLayout_2.addWidget(self.pyinstallerLabel, 1, 0, 1, 1)

        self.pyinstallerEdit = FileEdit(self.commonTab)
        self.pyinstallerEdit.setObjectName(u"pyinstallerEdit")
        self.pyinstallerEdit.setDragEnabled(True)

        self.gridLayout_2.addWidget(self.pyinstallerEdit, 1, 1, 1, 1)

        self.cwdEdit = DirectoryEdit(self.commonTab)
        self.cwdEdit.setObjectName(u"cwdEdit")
        self.cwdEdit.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.cwdEdit, 0, 1, 1, 1)

        self.selectPyInstallerButton = QPushButton(self.commonTab)
        self.selectPyInstallerButton.setObjectName(u"selectPyInstallerButton")

        self.gridLayout_2.addWidget(self.selectPyInstallerButton, 1, 2, 1, 1)

        self.pyimakespecLabel = QLabel(self.commonTab)
        self.pyimakespecLabel.setObjectName(u"pyimakespecLabel")

        self.gridLayout_2.addWidget(self.pyimakespecLabel, 2, 0, 1, 1)

        self.pyimakespecEdit = QLineEdit(self.commonTab)
        self.pyimakespecEdit.setObjectName(u"pyimakespecEdit")

        self.gridLayout_2.addWidget(self.pyimakespecEdit, 2, 1, 1, 1)

        self.selectPyimakespecButton = QPushButton(self.commonTab)
        self.selectPyimakespecButton.setObjectName(u"selectPyimakespecButton")

        self.gridLayout_2.addWidget(self.selectPyimakespecButton, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.scriptsListWidgetLayout = QVBoxLayout()
        self.scriptsListWidgetLayout.setObjectName(u"scriptsListWidgetLayout")
        self.scriptsLabel = QLabel(self.commonTab)
        self.scriptsLabel.setObjectName(u"scriptsLabel")

        self.scriptsListWidgetLayout.addWidget(self.scriptsLabel)

        self.scriptsListWidget = FileListWidget(self.commonTab)
        self.scriptsListWidget.setObjectName(u"scriptsListWidget")
        self.scriptsListWidget.setMouseTracking(False)
        self.scriptsListWidget.setAcceptDrops(True)
        self.scriptsListWidget.setDragEnabled(True)
        self.scriptsListWidget.setDragDropOverwriteMode(True)
        self.scriptsListWidget.setDragDropMode(QAbstractItemView.NoDragDrop)

        self.scriptsListWidgetLayout.addWidget(self.scriptsListWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addScriptButton = QPushButton(self.commonTab)
        self.addScriptButton.setObjectName(u"addScriptButton")

        self.horizontalLayout_2.addWidget(self.addScriptButton)

        self.removeScriptButton = QPushButton(self.commonTab)
        self.removeScriptButton.setObjectName(u"removeScriptButton")

        self.horizontalLayout_2.addWidget(self.removeScriptButton)


        self.scriptsListWidgetLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.scriptsListWidgetLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 5, -1, -1)
        self.specPathLabel = QLabel(self.commonTab)
        self.specPathLabel.setObjectName(u"specPathLabel")

        self.gridLayout.addWidget(self.specPathLabel, 3, 0, 1, 1)

        self.defaultDebugOptionButton = QPushButton(self.commonTab)
        self.defaultDebugOptionButton.setObjectName(u"defaultDebugOptionButton")

        self.gridLayout.addWidget(self.defaultDebugOptionButton, 10, 2, 1, 1)

        self.productNameLabel = QLabel(self.commonTab)
        self.productNameLabel.setObjectName(u"productNameLabel")

        self.gridLayout.addWidget(self.productNameLabel, 0, 0, 1, 1)

        self.defaultLogLevelButton = QPushButton(self.commonTab)
        self.defaultLogLevelButton.setObjectName(u"defaultLogLevelButton")

        self.gridLayout.addWidget(self.defaultLogLevelButton, 9, 2, 1, 1)

        self.distPathLabel = QLabel(self.commonTab)
        self.distPathLabel.setObjectName(u"distPathLabel")

        self.gridLayout.addWidget(self.distPathLabel, 1, 0, 1, 1)

        self.encryptionKeyEdit = QLineEdit(self.commonTab)
        self.encryptionKeyEdit.setObjectName(u"encryptionKeyEdit")

        self.gridLayout.addWidget(self.encryptionKeyEdit, 6, 1, 1, 1)

        self.stripSymbolsCheckBox = QCheckBox(self.commonTab)
        self.stripSymbolsCheckBox.setObjectName(u"stripSymbolsCheckBox")
        self.stripSymbolsCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.stripSymbolsCheckBox, 14, 1, 1, 1)

        self.appIconEdit = QLineEdit(self.commonTab)
        self.appIconEdit.setObjectName(u"appIconEdit")

        self.gridLayout.addWidget(self.appIconEdit, 4, 1, 1, 1)

        self.debugOptionCombo = QComboBox(self.commonTab)
        self.debugOptionCombo.setObjectName(u"debugOptionCombo")

        self.gridLayout.addWidget(self.debugOptionCombo, 10, 1, 1, 1)

        self.windowModeCombo = QComboBox(self.commonTab)
        self.windowModeCombo.setObjectName(u"windowModeCombo")

        self.gridLayout.addWidget(self.windowModeCombo, 7, 1, 1, 1)

        self.productNameEdit = QLineEdit(self.commonTab)
        self.productNameEdit.setObjectName(u"productNameEdit")

        self.gridLayout.addWidget(self.productNameEdit, 0, 1, 1, 1)

        self.defaultWindowModeButton = QPushButton(self.commonTab)
        self.defaultWindowModeButton.setObjectName(u"defaultWindowModeButton")

        self.gridLayout.addWidget(self.defaultWindowModeButton, 7, 2, 1, 1)

        self.encryptionKeyLabel = QLabel(self.commonTab)
        self.encryptionKeyLabel.setObjectName(u"encryptionKeyLabel")

        self.gridLayout.addWidget(self.encryptionKeyLabel, 6, 0, 1, 1)

        self.specPathEdit = QLineEdit(self.commonTab)
        self.specPathEdit.setObjectName(u"specPathEdit")

        self.gridLayout.addWidget(self.specPathEdit, 3, 1, 1, 1)

        self.selectAppIconButton = QPushButton(self.commonTab)
        self.selectAppIconButton.setObjectName(u"selectAppIconButton")

        self.gridLayout.addWidget(self.selectAppIconButton, 4, 3, 1, 1)

        self.defaultSplashButton = QPushButton(self.commonTab)
        self.defaultSplashButton.setObjectName(u"defaultSplashButton")

        self.gridLayout.addWidget(self.defaultSplashButton, 5, 2, 1, 1)

        self.defaultWorkPathButton = QPushButton(self.commonTab)
        self.defaultWorkPathButton.setObjectName(u"defaultWorkPathButton")

        self.gridLayout.addWidget(self.defaultWorkPathButton, 2, 2, 1, 1)

        self.asciiOnlyCheckBox = QCheckBox(self.commonTab)
        self.asciiOnlyCheckBox.setObjectName(u"asciiOnlyCheckBox")
        self.asciiOnlyCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.asciiOnlyCheckBox, 15, 1, 1, 1)

        self.workPathLabel = QLabel(self.commonTab)
        self.workPathLabel.setObjectName(u"workPathLabel")

        self.gridLayout.addWidget(self.workPathLabel, 2, 0, 1, 1)

        self.selectSpecPathButton = QPushButton(self.commonTab)
        self.selectSpecPathButton.setObjectName(u"selectSpecPathButton")

        self.gridLayout.addWidget(self.selectSpecPathButton, 3, 3, 1, 1)

        self.logLevelLabel = QLabel(self.commonTab)
        self.logLevelLabel.setObjectName(u"logLevelLabel")

        self.gridLayout.addWidget(self.logLevelLabel, 9, 0, 1, 1)

        self.productModelLabel = QLabel(self.commonTab)
        self.productModelLabel.setObjectName(u"productModelLabel")

        self.gridLayout.addWidget(self.productModelLabel, 8, 0, 1, 1)

        self.debugOptionLabel = QLabel(self.commonTab)
        self.debugOptionLabel.setObjectName(u"debugOptionLabel")

        self.gridLayout.addWidget(self.debugOptionLabel, 10, 0, 1, 1)

        self.selectDistPathButton = QPushButton(self.commonTab)
        self.selectDistPathButton.setObjectName(u"selectDistPathButton")

        self.gridLayout.addWidget(self.selectDistPathButton, 1, 3, 1, 1)

        self.selectWorkPathButton = QPushButton(self.commonTab)
        self.selectWorkPathButton.setObjectName(u"selectWorkPathButton")

        self.gridLayout.addWidget(self.selectWorkPathButton, 2, 3, 1, 1)

        self.defaultAppIconButton = QPushButton(self.commonTab)
        self.defaultAppIconButton.setObjectName(u"defaultAppIconButton")

        self.gridLayout.addWidget(self.defaultAppIconButton, 4, 2, 1, 1)

        self.defaultProductModeButton = QPushButton(self.commonTab)
        self.defaultProductModeButton.setObjectName(u"defaultProductModeButton")

        self.gridLayout.addWidget(self.defaultProductModeButton, 8, 2, 1, 1)

        self.productModeCombo = QComboBox(self.commonTab)
        self.productModeCombo.setObjectName(u"productModeCombo")

        self.gridLayout.addWidget(self.productModeCombo, 8, 1, 1, 1)

        self.splashEdit = QLineEdit(self.commonTab)
        self.splashEdit.setObjectName(u"splashEdit")

        self.gridLayout.addWidget(self.splashEdit, 5, 1, 1, 1)

        self.defaultSpecPathButton = QPushButton(self.commonTab)
        self.defaultSpecPathButton.setObjectName(u"defaultSpecPathButton")

        self.gridLayout.addWidget(self.defaultSpecPathButton, 3, 2, 1, 1)

        self.defaultEncryptionKeyButton = QPushButton(self.commonTab)
        self.defaultEncryptionKeyButton.setObjectName(u"defaultEncryptionKeyButton")

        self.gridLayout.addWidget(self.defaultEncryptionKeyButton, 6, 2, 1, 1)

        self.generateEncryptionKeyButton = QPushButton(self.commonTab)
        self.generateEncryptionKeyButton.setObjectName(u"generateEncryptionKeyButton")

        self.gridLayout.addWidget(self.generateEncryptionKeyButton, 6, 3, 1, 1)

        self.logLevelCombo = QComboBox(self.commonTab)
        self.logLevelCombo.setObjectName(u"logLevelCombo")

        self.gridLayout.addWidget(self.logLevelCombo, 9, 1, 1, 1)

        self.noConfirmCheckBox = QCheckBox(self.commonTab)
        self.noConfirmCheckBox.setObjectName(u"noConfirmCheckBox")
        self.noConfirmCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.noConfirmCheckBox, 13, 1, 1, 1)

        self.distPathEdit = DirectoryEdit(self.commonTab)
        self.distPathEdit.setObjectName(u"distPathEdit")

        self.gridLayout.addWidget(self.distPathEdit, 1, 1, 1, 1)

        self.appIconLabel = QLabel(self.commonTab)
        self.appIconLabel.setObjectName(u"appIconLabel")

        self.gridLayout.addWidget(self.appIconLabel, 4, 0, 1, 1)

        self.selectSplashButton = QPushButton(self.commonTab)
        self.selectSplashButton.setObjectName(u"selectSplashButton")

        self.gridLayout.addWidget(self.selectSplashButton, 5, 3, 1, 1)

        self.cleanBeforePackCheckBox = QCheckBox(self.commonTab)
        self.cleanBeforePackCheckBox.setObjectName(u"cleanBeforePackCheckBox")
        self.cleanBeforePackCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.cleanBeforePackCheckBox, 12, 1, 1, 1)

        self.workPathEdit = QLineEdit(self.commonTab)
        self.workPathEdit.setObjectName(u"workPathEdit")

        self.gridLayout.addWidget(self.workPathEdit, 2, 1, 1, 1)

        self.splashLabel = QLabel(self.commonTab)
        self.splashLabel.setObjectName(u"splashLabel")

        self.gridLayout.addWidget(self.splashLabel, 5, 0, 1, 1)

        self.startPackButton = QPushButton(self.commonTab)
        self.startPackButton.setObjectName(u"startPackButton")

        self.gridLayout.addWidget(self.startPackButton, 16, 0, 1, 4)

        self.defaultDistPathButton = QPushButton(self.commonTab)
        self.defaultDistPathButton.setObjectName(u"defaultDistPathButton")

        self.gridLayout.addWidget(self.defaultDistPathButton, 1, 2, 1, 1)

        self.windowModeLabel = QLabel(self.commonTab)
        self.windowModeLabel.setObjectName(u"windowModeLabel")

        self.gridLayout.addWidget(self.windowModeLabel, 7, 0, 1, 1)

        self.defaultProductNameButton = QPushButton(self.commonTab)
        self.defaultProductNameButton.setObjectName(u"defaultProductNameButton")

        self.gridLayout.addWidget(self.defaultProductNameButton, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.mainTabWidget.addTab(self.commonTab, "")
        self.pathsTab = QWidget()
        self.pathsTab.setObjectName(u"pathsTab")
        self.verticalLayout = QVBoxLayout(self.pathsTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.searchPathsLabel = QLabel(self.pathsTab)
        self.searchPathsLabel.setObjectName(u"searchPathsLabel")

        self.verticalLayout_3.addWidget(self.searchPathsLabel)

        self.searchPathsListWidget = DirectoryListWidget(self.pathsTab)
        self.searchPathsListWidget.setObjectName(u"searchPathsListWidget")

        self.verticalLayout_3.addWidget(self.searchPathsListWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addSearchPathButton = QPushButton(self.pathsTab)
        self.addSearchPathButton.setObjectName(u"addSearchPathButton")

        self.horizontalLayout_3.addWidget(self.addSearchPathButton)

        self.removeSearchPathButton = QPushButton(self.pathsTab)
        self.removeSearchPathButton.setObjectName(u"removeSearchPathButton")

        self.horizontalLayout_3.addWidget(self.removeSearchPathButton)

        self.clearSearchPathButton = QPushButton(self.pathsTab)
        self.clearSearchPathButton.setObjectName(u"clearSearchPathButton")

        self.horizontalLayout_3.addWidget(self.clearSearchPathButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.mainTabWidget.addTab(self.pathsTab, "")
        self.extraDataTab = QWidget()
        self.extraDataTab.setObjectName(u"extraDataTab")
        self.verticalLayout_7 = QVBoxLayout(self.extraDataTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.extraDataLabel = QLabel(self.extraDataTab)
        self.extraDataLabel.setObjectName(u"extraDataLabel")

        self.verticalLayout_7.addWidget(self.extraDataLabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.extraDataListWidget = QListWidget(self.extraDataTab)
        self.extraDataListWidget.setObjectName(u"extraDataListWidget")

        self.verticalLayout_5.addWidget(self.extraDataListWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addExtraDataButton = QPushButton(self.extraDataTab)
        self.addExtraDataButton.setObjectName(u"addExtraDataButton")

        self.horizontalLayout_4.addWidget(self.addExtraDataButton)

        self.removeExtraDataButton = QPushButton(self.extraDataTab)
        self.removeExtraDataButton.setObjectName(u"removeExtraDataButton")

        self.horizontalLayout_4.addWidget(self.removeExtraDataButton)

        self.clearExtraData = QPushButton(self.extraDataTab)
        self.clearExtraData.setObjectName(u"clearExtraData")

        self.horizontalLayout_4.addWidget(self.clearExtraData)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.extraDataTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.extraBinariesLabel = QLabel(self.extraDataTab)
        self.extraBinariesLabel.setObjectName(u"extraBinariesLabel")

        self.verticalLayout_7.addWidget(self.extraBinariesLabel)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.extraBinariesListWidget = QListWidget(self.extraDataTab)
        self.extraBinariesListWidget.setObjectName(u"extraBinariesListWidget")

        self.verticalLayout_6.addWidget(self.extraBinariesListWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addExtraBinariesButton = QPushButton(self.extraDataTab)
        self.addExtraBinariesButton.setObjectName(u"addExtraBinariesButton")

        self.horizontalLayout_5.addWidget(self.addExtraBinariesButton)

        self.removeExtraBinariesButton = QPushButton(self.extraDataTab)
        self.removeExtraBinariesButton.setObjectName(u"removeExtraBinariesButton")

        self.horizontalLayout_5.addWidget(self.removeExtraBinariesButton)

        self.clearExtraBinariesButton = QPushButton(self.extraDataTab)
        self.clearExtraBinariesButton.setObjectName(u"clearExtraBinariesButton")

        self.horizontalLayout_5.addWidget(self.clearExtraBinariesButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.mainTabWidget.addTab(self.extraDataTab, "")
        self.modulesTab = QWidget()
        self.modulesTab.setObjectName(u"modulesTab")
        self.verticalLayout_16 = QVBoxLayout(self.modulesTab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.excludeModulesLabel = QLabel(self.modulesTab)
        self.excludeModulesLabel.setObjectName(u"excludeModulesLabel")

        self.verticalLayout_21.addWidget(self.excludeModulesLabel)

        self.excludeModulesListWidget = QListWidget(self.modulesTab)
        self.excludeModulesListWidget.setObjectName(u"excludeModulesListWidget")

        self.verticalLayout_21.addWidget(self.excludeModulesListWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addExcludeModulesButton = QPushButton(self.modulesTab)
        self.addExcludeModulesButton.setObjectName(u"addExcludeModulesButton")

        self.horizontalLayout_6.addWidget(self.addExcludeModulesButton)

        self.removeExcludeModulesButton = QPushButton(self.modulesTab)
        self.removeExcludeModulesButton.setObjectName(u"removeExcludeModulesButton")

        self.horizontalLayout_6.addWidget(self.removeExcludeModulesButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_21)

        self.line_4 = QFrame(self.modulesTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.hiddenImportLabel = QLabel(self.modulesTab)
        self.hiddenImportLabel.setObjectName(u"hiddenImportLabel")

        self.verticalLayout_8.addWidget(self.hiddenImportLabel)

        self.hiddenImportsListWidget = QListWidget(self.modulesTab)
        self.hiddenImportsListWidget.setObjectName(u"hiddenImportsListWidget")

        self.verticalLayout_8.addWidget(self.hiddenImportsListWidget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addHiddenImportButton = QPushButton(self.modulesTab)
        self.addHiddenImportButton.setObjectName(u"addHiddenImportButton")

        self.horizontalLayout_7.addWidget(self.addHiddenImportButton)

        self.removeHiddenImportButton = QPushButton(self.modulesTab)
        self.removeHiddenImportButton.setObjectName(u"removeHiddenImportButton")

        self.horizontalLayout_7.addWidget(self.removeHiddenImportButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_8)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.line_2 = QFrame(self.modulesTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.collectSubmodulesLabel = QLabel(self.modulesTab)
        self.collectSubmodulesLabel.setObjectName(u"collectSubmodulesLabel")

        self.verticalLayout_22.addWidget(self.collectSubmodulesLabel)

        self.collectSubmodulesListWidget = QListWidget(self.modulesTab)
        self.collectSubmodulesListWidget.setObjectName(u"collectSubmodulesListWidget")

        self.verticalLayout_22.addWidget(self.collectSubmodulesListWidget)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.addCollectSubmoduleButton = QPushButton(self.modulesTab)
        self.addCollectSubmoduleButton.setObjectName(u"addCollectSubmoduleButton")

        self.horizontalLayout_14.addWidget(self.addCollectSubmoduleButton)

        self.removeCollectSubmoduleButton = QPushButton(self.modulesTab)
        self.removeCollectSubmoduleButton.setObjectName(u"removeCollectSubmoduleButton")

        self.horizontalLayout_14.addWidget(self.removeCollectSubmoduleButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_22)

        self.line_5 = QFrame(self.modulesTab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.collectDataLabel = QLabel(self.modulesTab)
        self.collectDataLabel.setObjectName(u"collectDataLabel")

        self.verticalLayout_9.addWidget(self.collectDataLabel)

        self.collectDataListWidget = QListWidget(self.modulesTab)
        self.collectDataListWidget.setObjectName(u"collectDataListWidget")

        self.verticalLayout_9.addWidget(self.collectDataListWidget)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.addCollectDataButton = QPushButton(self.modulesTab)
        self.addCollectDataButton.setObjectName(u"addCollectDataButton")

        self.horizontalLayout_15.addWidget(self.addCollectDataButton)

        self.removeCollectDataButton = QPushButton(self.modulesTab)
        self.removeCollectDataButton.setObjectName(u"removeCollectDataButton")

        self.horizontalLayout_15.addWidget(self.removeCollectDataButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.collectBinariesLabel = QLabel(self.modulesTab)
        self.collectBinariesLabel.setObjectName(u"collectBinariesLabel")

        self.verticalLayout_24.addWidget(self.collectBinariesLabel)

        self.collectBinariesListWidget = QListWidget(self.modulesTab)
        self.collectBinariesListWidget.setObjectName(u"collectBinariesListWidget")

        self.verticalLayout_24.addWidget(self.collectBinariesListWidget)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.addCollectBinariesButton = QPushButton(self.modulesTab)
        self.addCollectBinariesButton.setObjectName(u"addCollectBinariesButton")

        self.horizontalLayout_20.addWidget(self.addCollectBinariesButton)

        self.removeCollectBinariesButton = QPushButton(self.modulesTab)
        self.removeCollectBinariesButton.setObjectName(u"removeCollectBinariesButton")

        self.horizontalLayout_20.addWidget(self.removeCollectBinariesButton)


        self.verticalLayout_24.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_19.addLayout(self.verticalLayout_24)

        self.line_7 = QFrame(self.modulesTab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_7)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.collectAllLabel = QLabel(self.modulesTab)
        self.collectAllLabel.setObjectName(u"collectAllLabel")

        self.verticalLayout_15.addWidget(self.collectAllLabel)

        self.collectAllListWidget = QListWidget(self.modulesTab)
        self.collectAllListWidget.setObjectName(u"collectAllListWidget")

        self.verticalLayout_15.addWidget(self.collectAllListWidget)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.addCollectAllButton = QPushButton(self.modulesTab)
        self.addCollectAllButton.setObjectName(u"addCollectAllButton")

        self.horizontalLayout_21.addWidget(self.addCollectAllButton)

        self.removeCollectAllButton = QPushButton(self.modulesTab)
        self.removeCollectAllButton.setObjectName(u"removeCollectAllButton")

        self.horizontalLayout_21.addWidget(self.removeCollectAllButton)


        self.verticalLayout_15.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_19.addLayout(self.verticalLayout_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.line_8 = QFrame(self.modulesTab)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.copyMetadaLabel = QLabel(self.modulesTab)
        self.copyMetadaLabel.setObjectName(u"copyMetadaLabel")

        self.verticalLayout_23.addWidget(self.copyMetadaLabel)

        self.copyMetadaListWidget = QListWidget(self.modulesTab)
        self.copyMetadaListWidget.setObjectName(u"copyMetadaListWidget")

        self.verticalLayout_23.addWidget(self.copyMetadaListWidget)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.addCopyMetadaButton = QPushButton(self.modulesTab)
        self.addCopyMetadaButton.setObjectName(u"addCopyMetadaButton")

        self.horizontalLayout_17.addWidget(self.addCopyMetadaButton)

        self.removeCopyMetadaButton = QPushButton(self.modulesTab)
        self.removeCopyMetadaButton.setObjectName(u"removeCopyMetadaButton")

        self.horizontalLayout_17.addWidget(self.removeCopyMetadaButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)

        self.line_6 = QFrame(self.modulesTab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_6)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.deepcopyMetadaLabel = QLabel(self.modulesTab)
        self.deepcopyMetadaLabel.setObjectName(u"deepcopyMetadaLabel")

        self.verticalLayout_14.addWidget(self.deepcopyMetadaLabel)

        self.deepcopyMetadaListWidget = QListWidget(self.modulesTab)
        self.deepcopyMetadaListWidget.setObjectName(u"deepcopyMetadaListWidget")

        self.verticalLayout_14.addWidget(self.deepcopyMetadaListWidget)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.addDeepcopyMetadaButton = QPushButton(self.modulesTab)
        self.addDeepcopyMetadaButton.setObjectName(u"addDeepcopyMetadaButton")

        self.horizontalLayout_18.addWidget(self.addDeepcopyMetadaButton)

        self.removeDeepcopyMetadaButton = QPushButton(self.modulesTab)
        self.removeDeepcopyMetadaButton.setObjectName(u"removeDeepcopyMetadaButton")

        self.horizontalLayout_18.addWidget(self.removeDeepcopyMetadaButton)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_16.addLayout(self.verticalLayout_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.mainTabWidget.addTab(self.modulesTab, "")
        self.upxTab = QWidget()
        self.upxTab.setObjectName(u"upxTab")
        self.verticalLayout_18 = QVBoxLayout(self.upxTab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.noUPXCheckBox = QCheckBox(self.upxTab)
        self.noUPXCheckBox.setObjectName(u"noUPXCheckBox")

        self.verticalLayout_18.addWidget(self.noUPXCheckBox)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.upxPathLabel = QLabel(self.upxTab)
        self.upxPathLabel.setObjectName(u"upxPathLabel")

        self.horizontalLayout_22.addWidget(self.upxPathLabel)

        self.upxPathEdit = QLineEdit(self.upxTab)
        self.upxPathEdit.setObjectName(u"upxPathEdit")

        self.horizontalLayout_22.addWidget(self.upxPathEdit)

        self.selectUPXPathButton = QPushButton(self.upxTab)
        self.selectUPXPathButton.setObjectName(u"selectUPXPathButton")

        self.horizontalLayout_22.addWidget(self.selectUPXPathButton)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.upxExcludesLabel = QLabel(self.upxTab)
        self.upxExcludesLabel.setObjectName(u"upxExcludesLabel")

        self.verticalLayout_17.addWidget(self.upxExcludesLabel)

        self.upxExcludesListWidget = QListWidget(self.upxTab)
        self.upxExcludesListWidget.setObjectName(u"upxExcludesListWidget")

        self.verticalLayout_17.addWidget(self.upxExcludesListWidget)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.addUPXExcludesButton = QPushButton(self.upxTab)
        self.addUPXExcludesButton.setObjectName(u"addUPXExcludesButton")

        self.horizontalLayout_23.addWidget(self.addUPXExcludesButton)

        self.removeUPXExcludesButton = QPushButton(self.upxTab)
        self.removeUPXExcludesButton.setObjectName(u"removeUPXExcludesButton")
        self.removeUPXExcludesButton.setFlat(False)

        self.horizontalLayout_23.addWidget(self.removeUPXExcludesButton)


        self.verticalLayout_17.addLayout(self.horizontalLayout_23)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer)

        self.mainTabWidget.addTab(self.upxTab, "")
        self.platformTab = QWidget()
        self.platformTab.setObjectName(u"platformTab")
        self.horizontalLayout_24 = QHBoxLayout(self.platformTab)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tabWidget_2 = QTabWidget(self.platformTab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.South)
        self.windowsOptionTab = QWidget()
        self.windowsOptionTab.setObjectName(u"windowsOptionTab")
        self.verticalLayout_10 = QVBoxLayout(self.windowsOptionTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.versionFileLabel = QLabel(self.windowsOptionTab)
        self.versionFileLabel.setObjectName(u"versionFileLabel")

        self.gridLayout_4.addWidget(self.versionFileLabel, 1, 0, 1, 1)

        self.resourceLabel = QLabel(self.windowsOptionTab)
        self.resourceLabel.setObjectName(u"resourceLabel")

        self.gridLayout_4.addWidget(self.resourceLabel, 3, 0, 1, 1)

        self.uacUIAccessCheckBox = QCheckBox(self.windowsOptionTab)
        self.uacUIAccessCheckBox.setObjectName(u"uacUIAccessCheckBox")

        self.gridLayout_4.addWidget(self.uacUIAccessCheckBox, 5, 1, 1, 1)

        self.selectManifestFileButton = QPushButton(self.windowsOptionTab)
        self.selectManifestFileButton.setObjectName(u"selectManifestFileButton")

        self.gridLayout_4.addWidget(self.selectManifestFileButton, 2, 2, 1, 1)

        self.resourceEdit = QLineEdit(self.windowsOptionTab)
        self.resourceEdit.setObjectName(u"resourceEdit")

        self.gridLayout_4.addWidget(self.resourceEdit, 3, 1, 1, 1)

        self.versionFileEdit = QLineEdit(self.windowsOptionTab)
        self.versionFileEdit.setObjectName(u"versionFileEdit")

        self.gridLayout_4.addWidget(self.versionFileEdit, 1, 1, 1, 1)

        self.manifestFileLabel = QLabel(self.windowsOptionTab)
        self.manifestFileLabel.setObjectName(u"manifestFileLabel")

        self.gridLayout_4.addWidget(self.manifestFileLabel, 2, 0, 1, 1)

        self.selectVersionFileButton = QPushButton(self.windowsOptionTab)
        self.selectVersionFileButton.setObjectName(u"selectVersionFileButton")

        self.gridLayout_4.addWidget(self.selectVersionFileButton, 1, 2, 1, 1)

        self.uacAdminCheckBox = QCheckBox(self.windowsOptionTab)
        self.uacAdminCheckBox.setObjectName(u"uacAdminCheckBox")

        self.gridLayout_4.addWidget(self.uacAdminCheckBox, 4, 1, 1, 1)

        self.selectResourceButton = QPushButton(self.windowsOptionTab)
        self.selectResourceButton.setObjectName(u"selectResourceButton")

        self.gridLayout_4.addWidget(self.selectResourceButton, 3, 2, 1, 1)

        self.manifestFileEdit = QLineEdit(self.windowsOptionTab)
        self.manifestFileEdit.setObjectName(u"manifestFileEdit")

        self.gridLayout_4.addWidget(self.manifestFileEdit, 2, 1, 1, 1)

        self.noPreferRedirectsCheckBox = QCheckBox(self.windowsOptionTab)
        self.noPreferRedirectsCheckBox.setObjectName(u"noPreferRedirectsCheckBox")

        self.gridLayout_4.addWidget(self.noPreferRedirectsCheckBox, 7, 1, 1, 1)

        self.privateAssembliesCheckBox = QCheckBox(self.windowsOptionTab)
        self.privateAssembliesCheckBox.setObjectName(u"privateAssembliesCheckBox")

        self.gridLayout_4.addWidget(self.privateAssembliesCheckBox, 6, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.tabWidget_2.addTab(self.windowsOptionTab, "")
        self.macosxOptionTab = QWidget()
        self.macosxOptionTab.setObjectName(u"macosxOptionTab")
        self.verticalLayout_12 = QVBoxLayout(self.macosxOptionTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.entitlementsFileLabel = QLabel(self.macosxOptionTab)
        self.entitlementsFileLabel.setObjectName(u"entitlementsFileLabel")

        self.gridLayout_5.addWidget(self.entitlementsFileLabel, 0, 0, 1, 1)

        self.entitlementsFileEdit = QLineEdit(self.macosxOptionTab)
        self.entitlementsFileEdit.setObjectName(u"entitlementsFileEdit")

        self.gridLayout_5.addWidget(self.entitlementsFileEdit, 0, 1, 1, 1)

        self.targetArchitectureLabel = QLabel(self.macosxOptionTab)
        self.targetArchitectureLabel.setObjectName(u"targetArchitectureLabel")

        self.gridLayout_5.addWidget(self.targetArchitectureLabel, 1, 0, 1, 1)

        self.targetArchitectureCombo = QComboBox(self.macosxOptionTab)
        self.targetArchitectureCombo.setObjectName(u"targetArchitectureCombo")

        self.gridLayout_5.addWidget(self.targetArchitectureCombo, 1, 1, 1, 1)

        self.bundleIdentifierLabel = QLabel(self.macosxOptionTab)
        self.bundleIdentifierLabel.setObjectName(u"bundleIdentifierLabel")

        self.gridLayout_5.addWidget(self.bundleIdentifierLabel, 2, 0, 1, 1)

        self.bundleIdentifierEdit = QLineEdit(self.macosxOptionTab)
        self.bundleIdentifierEdit.setObjectName(u"bundleIdentifierEdit")

        self.gridLayout_5.addWidget(self.bundleIdentifierEdit, 2, 1, 1, 1)

        self.codesignIdentityLabel = QLabel(self.macosxOptionTab)
        self.codesignIdentityLabel.setObjectName(u"codesignIdentityLabel")

        self.gridLayout_5.addWidget(self.codesignIdentityLabel, 3, 0, 1, 1)

        self.codesignIdentityEdit = QLineEdit(self.macosxOptionTab)
        self.codesignIdentityEdit.setObjectName(u"codesignIdentityEdit")

        self.gridLayout_5.addWidget(self.codesignIdentityEdit, 3, 1, 1, 1)

        self.selectEntitlementsFileButton = QPushButton(self.macosxOptionTab)
        self.selectEntitlementsFileButton.setObjectName(u"selectEntitlementsFileButton")

        self.gridLayout_5.addWidget(self.selectEntitlementsFileButton, 0, 2, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.tabWidget_2.addTab(self.macosxOptionTab, "")

        self.horizontalLayout_24.addWidget(self.tabWidget_2)

        self.mainTabWidget.addTab(self.platformTab, "")
        self.miscTab = QWidget()
        self.miscTab.setObjectName(u"miscTab")
        self.verticalLayout_27 = QVBoxLayout(self.miscTab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.hooksLabel = QLabel(self.miscTab)
        self.hooksLabel.setObjectName(u"hooksLabel")

        self.verticalLayout_19.addWidget(self.hooksLabel)

        self.hooksListWidget = QListWidget(self.miscTab)
        self.hooksListWidget.setObjectName(u"hooksListWidget")

        self.verticalLayout_19.addWidget(self.hooksListWidget)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.addHooksButton = QPushButton(self.miscTab)
        self.addHooksButton.setObjectName(u"addHooksButton")

        self.horizontalLayout_25.addWidget(self.addHooksButton)

        self.removeHooksButton = QPushButton(self.miscTab)
        self.removeHooksButton.setObjectName(u"removeHooksButton")

        self.horizontalLayout_25.addWidget(self.removeHooksButton)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)


        self.verticalLayout_27.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.rtHooksLabel = QLabel(self.miscTab)
        self.rtHooksLabel.setObjectName(u"rtHooksLabel")

        self.verticalLayout_20.addWidget(self.rtHooksLabel)

        self.rtHooksListWidget = QListWidget(self.miscTab)
        self.rtHooksListWidget.setObjectName(u"rtHooksListWidget")

        self.verticalLayout_20.addWidget(self.rtHooksListWidget)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.addRTHooksButton = QPushButton(self.miscTab)
        self.addRTHooksButton.setObjectName(u"addRTHooksButton")

        self.horizontalLayout_26.addWidget(self.addRTHooksButton)

        self.removeRTHooksButton = QPushButton(self.miscTab)
        self.removeRTHooksButton.setObjectName(u"removeRTHooksButton")

        self.horizontalLayout_26.addWidget(self.removeRTHooksButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)


        self.verticalLayout_27.addLayout(self.verticalLayout_20)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.rtTmpDirLabel = QLabel(self.miscTab)
        self.rtTmpDirLabel.setObjectName(u"rtTmpDirLabel")

        self.verticalLayout_25.addWidget(self.rtTmpDirLabel)

        self.rtTmpDirlistWidget = QListWidget(self.miscTab)
        self.rtTmpDirlistWidget.setObjectName(u"rtTmpDirlistWidget")

        self.verticalLayout_25.addWidget(self.rtTmpDirlistWidget)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.addRTTmpDirButton = QPushButton(self.miscTab)
        self.addRTTmpDirButton.setObjectName(u"addRTTmpDirButton")

        self.horizontalLayout_27.addWidget(self.addRTTmpDirButton)

        self.removeRTTmpDirButton = QPushButton(self.miscTab)
        self.removeRTTmpDirButton.setObjectName(u"removeRTTmpDirButton")

        self.horizontalLayout_27.addWidget(self.removeRTTmpDirButton)


        self.verticalLayout_25.addLayout(self.horizontalLayout_27)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.blIgnoreSignalsLabel = QLabel(self.miscTab)
        self.blIgnoreSignalsLabel.setObjectName(u"blIgnoreSignalsLabel")

        self.verticalLayout_26.addWidget(self.blIgnoreSignalsLabel)

        self.blIgnoreSignalsListWidget = QListWidget(self.miscTab)
        self.blIgnoreSignalsListWidget.setObjectName(u"blIgnoreSignalsListWidget")

        self.verticalLayout_26.addWidget(self.blIgnoreSignalsListWidget)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.addBLIgnoreSignalsButton = QPushButton(self.miscTab)
        self.addBLIgnoreSignalsButton.setObjectName(u"addBLIgnoreSignalsButton")

        self.horizontalLayout_28.addWidget(self.addBLIgnoreSignalsButton)

        self.removeBLIgnoreSignalsButton = QPushButton(self.miscTab)
        self.removeBLIgnoreSignalsButton.setObjectName(u"removeBLIgnoreSignalsButton")

        self.horizontalLayout_28.addWidget(self.removeBLIgnoreSignalsButton)


        self.verticalLayout_26.addLayout(self.horizontalLayout_28)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.mainTabWidget.addTab(self.miscTab, "")
        self.metadataTab = QWidget()
        self.metadataTab.setObjectName(u"metadataTab")
        self.verticalLayout_4 = QVBoxLayout(self.metadataTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.nameLabel = QLabel(self.metadataTab)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout_3.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.authorEdit = QLineEdit(self.metadataTab)
        self.authorEdit.setObjectName(u"authorEdit")

        self.gridLayout_3.addWidget(self.authorEdit, 1, 1, 1, 1)

        self.authorLabel = QLabel(self.metadataTab)
        self.authorLabel.setObjectName(u"authorLabel")

        self.gridLayout_3.addWidget(self.authorLabel, 1, 0, 1, 1)

        self.versionEdit = QLineEdit(self.metadataTab)
        self.versionEdit.setObjectName(u"versionEdit")

        self.gridLayout_3.addWidget(self.versionEdit, 2, 1, 1, 1)

        self.nameEdit = QLineEdit(self.metadataTab)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout_3.addWidget(self.nameEdit, 0, 1, 1, 1)

        self.versionLabel = QLabel(self.metadataTab)
        self.versionLabel.setObjectName(u"versionLabel")

        self.gridLayout_3.addWidget(self.versionLabel, 2, 0, 1, 1)

        self.descriptionLabel = QLabel(self.metadataTab)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.gridLayout_3.addWidget(self.descriptionLabel, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.descriptionEdit = QTextEdit(self.metadataTab)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.gridLayout_3.addWidget(self.descriptionEdit, 3, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.mainTabWidget.addTab(self.metadataTab, "")

        self.horizontalLayout_9.addWidget(self.mainTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 709, 26))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.commandMenu = QMenu(self.menubar)
        self.commandMenu.setObjectName(u"commandMenu")
        self.helpMenu = QMenu(self.menubar)
        self.helpMenu.setObjectName(u"helpMenu")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.commandMenu.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionNewConfigs)
        self.fileMenu.addAction(self.actionSaveConfigs)
        self.fileMenu.addAction(self.actionLoadConfigs)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionExit)
        self.commandMenu.addAction(self.actionStartPack)
        self.commandMenu.addAction(self.actionStartGenSpceFile)
        self.helpMenu.addAction(self.actionAbout)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.actionGotoPyinstallerWebsite)
        self.helpMenu.addAction(self.actionGotoPyInstallerDoc)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.actionHelp)
        self.menuSetting.addAction(self.actionChangeFont)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        self.mainTabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyInstaller GUI", None))
        self.actionStartPack.setText(QCoreApplication.translate("MainWindow", u"Start Pack", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSaveConfigs.setText(QCoreApplication.translate("MainWindow", u"Sava Configs", None))
#if QT_CONFIG(shortcut)
        self.actionSaveConfigs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionLoadConfigs.setText(QCoreApplication.translate("MainWindow", u"Load Configs", None))
#if QT_CONFIG(shortcut)
        self.actionLoadConfigs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionNewConfigs.setText(QCoreApplication.translate("MainWindow", u"New Configs", None))
#if QT_CONFIG(shortcut)
        self.actionNewConfigs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionGotoPyinstallerWebsite.setText(QCoreApplication.translate("MainWindow", u"PyInstaller Website", None))
        self.actionGotoPyInstallerDoc.setText(QCoreApplication.translate("MainWindow", u"PyInstaller Documentation", None))
        self.actionStartGenSpceFile.setText(QCoreApplication.translate("MainWindow", u"Generate Spce File", None))
        self.actionChangeFont.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.cwdLabel.setText(QCoreApplication.translate("MainWindow", u"cwd", None))
        self.changeCWDButton.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pyinstallerLabel.setText(QCoreApplication.translate("MainWindow", u"Pynstaller Path", None))
        self.selectPyInstallerButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pyimakespecLabel.setText(QCoreApplication.translate("MainWindow", u"pyi-makespec", None))
        self.selectPyimakespecButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.scriptsLabel.setText(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.addScriptButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeScriptButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.specPathLabel.setText(QCoreApplication.translate("MainWindow", u"Spec Path", None))
        self.defaultDebugOptionButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.productNameLabel.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.defaultLogLevelButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.distPathLabel.setText(QCoreApplication.translate("MainWindow", u"Dist Path", None))
        self.stripSymbolsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Strip symbol-table", None))
        self.defaultWindowModeButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.encryptionKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Encryption Key", None))
        self.selectAppIconButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.defaultSplashButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.defaultWorkPathButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.asciiOnlyCheckBox.setText(QCoreApplication.translate("MainWindow", u"ASCII only\uff08no unicode\uff09", None))
        self.workPathLabel.setText(QCoreApplication.translate("MainWindow", u"Work Path", None))
        self.selectSpecPathButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.logLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Log Level", None))
        self.productModelLabel.setText(QCoreApplication.translate("MainWindow", u"Product Mode", None))
        self.debugOptionLabel.setText(QCoreApplication.translate("MainWindow", u"Debug Option", None))
        self.selectDistPathButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.selectWorkPathButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.defaultAppIconButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.defaultProductModeButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.defaultSpecPathButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.defaultEncryptionKeyButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.generateEncryptionKeyButton.setText(QCoreApplication.translate("MainWindow", u"Auto Gen", None))
        self.noConfirmCheckBox.setText(QCoreApplication.translate("MainWindow", u"Don't Confirm", None))
        self.appIconLabel.setText(QCoreApplication.translate("MainWindow", u"App Icon", None))
        self.selectSplashButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.cleanBeforePackCheckBox.setText(QCoreApplication.translate("MainWindow", u"Clean before build", None))
        self.splashLabel.setText(QCoreApplication.translate("MainWindow", u"Splash", None))
        self.startPackButton.setText(QCoreApplication.translate("MainWindow", u"Pack", None))
        self.defaultDistPathButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.windowModeLabel.setText(QCoreApplication.translate("MainWindow", u"Window Mode", None))
        self.defaultProductNameButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.commonTab), QCoreApplication.translate("MainWindow", u"Common", None))
        self.searchPathsLabel.setText(QCoreApplication.translate("MainWindow", u"Search Paths", None))
        self.addSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.pathsTab), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.extraDataLabel.setText(QCoreApplication.translate("MainWindow", u"Extra Data", None))
        self.addExtraDataButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeExtraDataButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearExtraData.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.extraBinariesLabel.setText(QCoreApplication.translate("MainWindow", u"Extra Binaries", None))
        self.addExtraBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeExtraBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearExtraBinariesButton.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.extraDataTab), QCoreApplication.translate("MainWindow", u"Extra Data", None))
        self.excludeModulesLabel.setText(QCoreApplication.translate("MainWindow", u"Exclude Modules", None))
        self.addExcludeModulesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeExcludeModulesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.hiddenImportLabel.setText(QCoreApplication.translate("MainWindow", u"Hidden Imports", None))
        self.addHiddenImportButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeHiddenImportButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.collectSubmodulesLabel.setText(QCoreApplication.translate("MainWindow", u"Collect all submodules from:", None))
        self.addCollectSubmoduleButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeCollectSubmoduleButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.collectDataLabel.setText(QCoreApplication.translate("MainWindow", u"Collect all data from:", None))
        self.addCollectDataButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeCollectDataButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.collectBinariesLabel.setText(QCoreApplication.translate("MainWindow", u"Collect all binaries from:", None))
        self.addCollectBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeCollectBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.collectAllLabel.setText(QCoreApplication.translate("MainWindow", u"Collect all(submodules,data, bin...) from:", None))
        self.addCollectAllButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeCollectAllButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.copyMetadaLabel.setText(QCoreApplication.translate("MainWindow", u"Copy metadata for:", None))
        self.addCopyMetadaButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeCopyMetadaButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.deepcopyMetadaLabel.setText(QCoreApplication.translate("MainWindow", u"Copy metadata for(recursively):", None))
        self.addDeepcopyMetadaButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeDeepcopyMetadaButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.modulesTab), QCoreApplication.translate("MainWindow", u"Modules/Packages", None))
        self.noUPXCheckBox.setText(QCoreApplication.translate("MainWindow", u"Disable UPX", None))
        self.upxPathLabel.setText(QCoreApplication.translate("MainWindow", u"UPX path", None))
        self.selectUPXPathButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.upxExcludesLabel.setText(QCoreApplication.translate("MainWindow", u"Exludes", None))
        self.addUPXExcludesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeUPXExcludesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.upxTab), QCoreApplication.translate("MainWindow", u"UPX", None))
        self.versionFileLabel.setText(QCoreApplication.translate("MainWindow", u"Version File", None))
        self.resourceLabel.setText(QCoreApplication.translate("MainWindow", u"Resource", None))
        self.uacUIAccessCheckBox.setText(QCoreApplication.translate("MainWindow", u"uac-uiaccess", None))
        self.selectManifestFileButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.manifestFileLabel.setText(QCoreApplication.translate("MainWindow", u"Manifest File", None))
        self.selectVersionFileButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.uacAdminCheckBox.setText(QCoreApplication.translate("MainWindow", u"uac-admin", None))
        self.selectResourceButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.noPreferRedirectsCheckBox.setText(QCoreApplication.translate("MainWindow", u"win-no-prefer-redirects", None))
        self.privateAssembliesCheckBox.setText(QCoreApplication.translate("MainWindow", u"win-private-assemblies", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.windowsOptionTab), QCoreApplication.translate("MainWindow", u"Windows", None))
        self.entitlementsFileLabel.setText(QCoreApplication.translate("MainWindow", u"Entitlements File", None))
        self.targetArchitectureLabel.setText(QCoreApplication.translate("MainWindow", u"Target Architecture", None))
        self.bundleIdentifierLabel.setText(QCoreApplication.translate("MainWindow", u"Bundle Identifier", None))
        self.codesignIdentityLabel.setText(QCoreApplication.translate("MainWindow", u"Codesign Identity", None))
        self.selectEntitlementsFileButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.macosxOptionTab), QCoreApplication.translate("MainWindow", u"Mac OS X", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.platformTab), QCoreApplication.translate("MainWindow", u"Platform Specific", None))
        self.hooksLabel.setText(QCoreApplication.translate("MainWindow", u"Additional hooks", None))
        self.addHooksButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeHooksButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.rtHooksLabel.setText(QCoreApplication.translate("MainWindow", u"Runtime hooks", None))
        self.addRTHooksButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeRTHooksButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.rtTmpDirLabel.setText(QCoreApplication.translate("MainWindow", u"Runtime tmp dir", None))
        self.addRTTmpDirButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeRTTmpDirButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.blIgnoreSignalsLabel.setText(QCoreApplication.translate("MainWindow", u"Bootloader ignore signals", None))
        self.addBLIgnoreSignalsButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeBLIgnoreSignalsButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.miscTab), QCoreApplication.translate("MainWindow", u"MISC", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"author", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.metadataTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.commandMenu.setTitle(QCoreApplication.translate("MainWindow", u"Command", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

