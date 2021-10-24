# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainhkcwis.ui'
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
        MainWindow.resize(709, 915)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        self.actionLoadPreset = QAction(MainWindow)
        self.actionLoadPreset.setObjectName(u"actionLoadPreset")
        self.actionSavePreset = QAction(MainWindow)
        self.actionSavePreset.setObjectName(u"actionSavePreset")
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
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionNewConfigs = QAction(MainWindow)
        self.actionNewConfigs.setObjectName(u"actionNewConfigs")
        self.actionGotoPyinstallerWebsite = QAction(MainWindow)
        self.actionGotoPyinstallerWebsite.setObjectName(u"actionGotoPyinstallerWebsite")
        self.actionGotoPyInstallerDoc = QAction(MainWindow)
        self.actionGotoPyInstallerDoc.setObjectName(u"actionGotoPyInstallerDoc")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.commonTab = QWidget()
        self.commonTab.setObjectName(u"commonTab")
        self.verticalLayout_2 = QVBoxLayout(self.commonTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cwdLabel = QLabel(self.commonTab)
        self.cwdLabel.setObjectName(u"cwdLabel")

        self.gridLayout_2.addWidget(self.cwdLabel, 0, 0, 1, 1)

        self.cwdEdit = DirectoryEdit(self.commonTab)
        self.cwdEdit.setObjectName(u"cwdEdit")
        self.cwdEdit.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.cwdEdit, 0, 1, 1, 1)

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

        self.selectPyInstallerButton = QPushButton(self.commonTab)
        self.selectPyInstallerButton.setObjectName(u"selectPyInstallerButton")

        self.gridLayout_2.addWidget(self.selectPyInstallerButton, 1, 2, 1, 1)


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


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.commonTab, "")
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

        self.tabWidget.addTab(self.pathsTab, "")
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


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.extraDataTab, "")
        self.modulesTab = QWidget()
        self.modulesTab.setObjectName(u"modulesTab")
        self.verticalLayout_16 = QVBoxLayout(self.modulesTab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_15 = QLabel(self.modulesTab)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_21.addWidget(self.label_15)

        self.listView = QListView(self.modulesTab)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_21.addWidget(self.listView)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_3 = QPushButton(self.modulesTab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.modulesTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_21)

        self.line_4 = QFrame(self.modulesTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.modulesTab)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.listView_2 = QListView(self.modulesTab)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_8.addWidget(self.listView_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_4 = QPushButton(self.modulesTab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.modulesTab)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_7.addWidget(self.pushButton_5)


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
        self.label_17 = QLabel(self.modulesTab)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_22.addWidget(self.label_17)

        self.listView_10 = QListView(self.modulesTab)
        self.listView_10.setObjectName(u"listView_10")

        self.verticalLayout_22.addWidget(self.listView_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_20 = QPushButton(self.modulesTab)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_14.addWidget(self.pushButton_20)

        self.pushButton_19 = QPushButton(self.modulesTab)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_14.addWidget(self.pushButton_19)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_22)

        self.line_5 = QFrame(self.modulesTab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.modulesTab)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)

        self.listView_11 = QListView(self.modulesTab)
        self.listView_11.setObjectName(u"listView_11")

        self.verticalLayout_9.addWidget(self.listView_11)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_22 = QPushButton(self.modulesTab)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_15.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.modulesTab)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_15.addWidget(self.pushButton_23)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_19 = QLabel(self.modulesTab)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_24.addWidget(self.label_19)

        self.listView_14 = QListView(self.modulesTab)
        self.listView_14.setObjectName(u"listView_14")

        self.verticalLayout_24.addWidget(self.listView_14)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_31 = QPushButton(self.modulesTab)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.horizontalLayout_20.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.modulesTab)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.horizontalLayout_20.addWidget(self.pushButton_32)


        self.verticalLayout_24.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_19.addLayout(self.verticalLayout_24)

        self.line_7 = QFrame(self.modulesTab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_7)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_20 = QLabel(self.modulesTab)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_15.addWidget(self.label_20)

        self.listView_15 = QListView(self.modulesTab)
        self.listView_15.setObjectName(u"listView_15")

        self.verticalLayout_15.addWidget(self.listView_15)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_34 = QPushButton(self.modulesTab)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.horizontalLayout_21.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.modulesTab)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.horizontalLayout_21.addWidget(self.pushButton_35)


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
        self.label_21 = QLabel(self.modulesTab)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_23.addWidget(self.label_21)

        self.listView_12 = QListView(self.modulesTab)
        self.listView_12.setObjectName(u"listView_12")

        self.verticalLayout_23.addWidget(self.listView_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_25 = QPushButton(self.modulesTab)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_17.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.modulesTab)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.horizontalLayout_17.addWidget(self.pushButton_26)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)

        self.line_6 = QFrame(self.modulesTab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_6)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_22 = QLabel(self.modulesTab)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_14.addWidget(self.label_22)

        self.listView_13 = QListView(self.modulesTab)
        self.listView_13.setObjectName(u"listView_13")

        self.verticalLayout_14.addWidget(self.listView_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_28 = QPushButton(self.modulesTab)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_18.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.modulesTab)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_18.addWidget(self.pushButton_29)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_16.addLayout(self.verticalLayout_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.tabWidget.addTab(self.modulesTab, "")
        self.upxTab = QWidget()
        self.upxTab.setObjectName(u"upxTab")
        self.verticalLayout_18 = QVBoxLayout(self.upxTab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.checkBox_2 = QCheckBox(self.upxTab)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_18.addWidget(self.checkBox_2)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_24 = QLabel(self.upxTab)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_22.addWidget(self.label_24)

        self.lineEdit = QLineEdit(self.upxTab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_22.addWidget(self.lineEdit)

        self.pushButton_10 = QPushButton(self.upxTab)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_22.addWidget(self.pushButton_10)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_25 = QLabel(self.upxTab)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_17.addWidget(self.label_25)

        self.listView_16 = QListView(self.upxTab)
        self.listView_16.setObjectName(u"listView_16")

        self.verticalLayout_17.addWidget(self.listView_16)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton = QPushButton(self.upxTab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_23.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.upxTab)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_23.addWidget(self.pushButton_6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_23)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.upxTab, "")
        self.platformTab = QWidget()
        self.platformTab.setObjectName(u"platformTab")
        self.horizontalLayout_24 = QHBoxLayout(self.platformTab)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tabWidget_2 = QTabWidget(self.platformTab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.South)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget_2.addTab(self.tab_9, "")

        self.horizontalLayout_24.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.platformTab, "")
        self.miscTab = QWidget()
        self.miscTab.setObjectName(u"miscTab")
        self.verticalLayout_27 = QVBoxLayout(self.miscTab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_26 = QLabel(self.miscTab)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_19.addWidget(self.label_26)

        self.listView_17 = QListView(self.miscTab)
        self.listView_17.setObjectName(u"listView_17")

        self.verticalLayout_19.addWidget(self.listView_17)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_21 = QPushButton(self.miscTab)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_25.addWidget(self.pushButton_21)

        self.pushButton_24 = QPushButton(self.miscTab)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_25.addWidget(self.pushButton_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)


        self.verticalLayout_27.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_27 = QLabel(self.miscTab)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_20.addWidget(self.label_27)

        self.listView_18 = QListView(self.miscTab)
        self.listView_18.setObjectName(u"listView_18")

        self.verticalLayout_20.addWidget(self.listView_18)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_27 = QPushButton(self.miscTab)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_26.addWidget(self.pushButton_27)

        self.pushButton_30 = QPushButton(self.miscTab)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_26.addWidget(self.pushButton_30)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)


        self.verticalLayout_27.addLayout(self.verticalLayout_20)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_28 = QLabel(self.miscTab)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_25.addWidget(self.label_28)

        self.listView_19 = QListView(self.miscTab)
        self.listView_19.setObjectName(u"listView_19")

        self.verticalLayout_25.addWidget(self.listView_19)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_33 = QPushButton(self.miscTab)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.horizontalLayout_27.addWidget(self.pushButton_33)

        self.pushButton_36 = QPushButton(self.miscTab)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_27.addWidget(self.pushButton_36)


        self.verticalLayout_25.addLayout(self.horizontalLayout_27)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_29 = QLabel(self.miscTab)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_26.addWidget(self.label_29)

        self.listView_20 = QListView(self.miscTab)
        self.listView_20.setObjectName(u"listView_20")

        self.verticalLayout_26.addWidget(self.listView_20)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_37 = QPushButton(self.miscTab)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_28.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.miscTab)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.horizontalLayout_28.addWidget(self.pushButton_38)


        self.verticalLayout_26.addLayout(self.horizontalLayout_28)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.tabWidget.addTab(self.miscTab, "")
        self.metaTab = QWidget()
        self.metaTab.setObjectName(u"metaTab")
        self.verticalLayout_4 = QVBoxLayout(self.metaTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.nameLabel = QLabel(self.metaTab)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout_3.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.metaTab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label = QLabel(self.metaTab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.metaTab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_2 = QLabel(self.metaTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.metaTab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_3 = QLabel(self.metaTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.metaTab)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 3, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.metaTab, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 709, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionNewConfigs)
        self.menu.addAction(self.actionSaveConfigs)
        self.menu.addAction(self.actionLoadConfigs)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionStartPack)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionSettings)
        self.menu_3.addAction(self.actionAbout)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionGotoPyinstallerWebsite)
        self.menu_3.addAction(self.actionGotoPyInstallerDoc)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyInstaller GUI", None))
        self.actionLoadPreset.setText(QCoreApplication.translate("MainWindow", u"load preset", None))
        self.actionSavePreset.setText(QCoreApplication.translate("MainWindow", u"save preset", None))
        self.actionStartPack.setText(QCoreApplication.translate("MainWindow", u"Start Pack", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSaveConfigs.setText(QCoreApplication.translate("MainWindow", u"Sava Configs", None))
        self.actionLoadConfigs.setText(QCoreApplication.translate("MainWindow", u"Load Configs", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionNewConfigs.setText(QCoreApplication.translate("MainWindow", u"New Configs", None))
        self.actionGotoPyinstallerWebsite.setText(QCoreApplication.translate("MainWindow", u"PyInstaller Website", None))
        self.actionGotoPyInstallerDoc.setText(QCoreApplication.translate("MainWindow", u"PyInstaller Documentation", None))
        self.cwdLabel.setText(QCoreApplication.translate("MainWindow", u"Working Dir    ", None))
        self.changeCWDButton.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pyinstallerLabel.setText(QCoreApplication.translate("MainWindow", u"Pynstaller Path", None))
        self.pyinstallerEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set path of pyinstaller here", None))
        self.selectPyInstallerButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.commonTab), QCoreApplication.translate("MainWindow", u"Common", None))
        self.searchPathsLabel.setText(QCoreApplication.translate("MainWindow", u"Search Paths", None))
        self.addSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearSearchPathButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pathsTab), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.extraDataLabel.setText(QCoreApplication.translate("MainWindow", u"Extra Data Paths", None))
        self.addExtraDataButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeExtraDataButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.extraBinariesLabel.setText(QCoreApplication.translate("MainWindow", u"Extra Binaries Paths", None))
        self.addExtraBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeExtraBinariesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extraDataTab), QCoreApplication.translate("MainWindow", u"Extra Data", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Exclude Moudlues", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hidden Imports", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Collect all submodules from:", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Collect all data from:", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Collect all binaries from:", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Collect all(submodules,data, bin...)from:", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Copy metadata for:", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Copy metadata for(recursively):", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modulesTab), QCoreApplication.translate("MainWindow", u"Modules/Packages", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Disable UPX", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"UPX path", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Exludes", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.upxTab), QCoreApplication.translate("MainWindow", u"UPX", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Windows", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Mac OS X", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Linux", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.platformTab), QCoreApplication.translate("MainWindow", u"Platform Specific", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Additional hooks", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Runtime hooks", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Runtime tmp dir", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Bootloader ignore signals", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.miscTab), QCoreApplication.translate("MainWindow", u"MISC", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"name:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"author", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.metaTab), QCoreApplication.translate("MainWindow", u"Meta", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"Pack", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

