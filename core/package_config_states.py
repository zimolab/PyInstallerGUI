from QBinder import BinderTemplate, Model

from core.package_configs import PackageConfigs
from core.option import OPTION_BY_DEFAULT


def mapBoolFlag(flag):
    if flag is None or flag == OPTION_BY_DEFAULT or flag == "":
        return False
    if isinstance(flag, bool):
        return flag
    else:
        if isinstance(flag, str):
            if flag.lower() == "true":
                return True
            else:
                return False
        else:
            return False


class PackageConfigStates(BinderTemplate):
    """
    这个类的目标是将PackageConfigs类中定义的选项（Option）与UI界面的状态关联起来。
    使PackageConfigs中Option的变化能够引起UI界面的变化，同时，UI界面的输入（状态改变）也能及时地反映到PackageConfigs的选项中（双向绑定）。
    很大程度上借助了QBinder所提供的数据绑定能力。
    """
    pyinstaller = "pyinstaller",
    name = "",
    author = ""
    version = "0.0.1"
    description = ""
    scripts = []

    # commonOptions
    productName = ""
    distPath = ""
    workPath = ""
    specPath = ""
    appIcon = ""
    splash = ""
    encryptionKey = ""
    windowMode = OPTION_BY_DEFAULT
    productMode = OPTION_BY_DEFAULT
    logLevel = OPTION_BY_DEFAULT
    debugOption = OPTION_BY_DEFAULT
    cleanBeforePack = True
    onConfirm = True
    stripSymbolTable = False
    asciiOnly = False
    searchPaths = []
    extraData = []
    extraBinaries = []

    def __init__(self, configs):
        self._configs = None
        self.changeConfigs(configs)

    def changeConfigs(self, newConfigs):
        self._configs = None
        self._configs = newConfigs
        self._updateStates()

    def _updateStates(self):
        self._configs: PackageConfigs
        # 更新非Option状态
        self.setPyInstallerPath(self._configs.pyinstaller, updateConfigs=False)
        self.setName(self._configs.name, updateConfigs=False)
        self.setAuthor(self._configs.author, updateConfigs=False)
        self.setVersion(self._configs.version, updateConfigs=False)
        self.setDescription(self._configs.description, updateConfigs=False)
        self.addScripts(self._configs.scripts, clearBeforeAdd=True, updateConfigs=False)
        # 更新CommonOptions的状态
        self.setProductName(self._configs.commonOptions.productName.argument, updateConfigs=False)
        self.setDistPath(self._configs.commonOptions.distPath.argument, updateConfigs=False)
        self.setWorkPath(self._configs.commonOptions.workPath.argument, updateConfigs=False)
        self.setSpecPath(self._configs.commonOptions.specPath.argument, updateConfigs=False)
        self.setAppIcon(self._configs.commonOptions.icon.argument, updateConfigs=False)
        self.setSplash(self._configs.commonOptions.splash.argument, updateConfigs=False)
        self.setEncryptionKey(self._configs.commonOptions.encryptionKey.argument, updateConfigs=False)
        self.setWindowMode(self._configs.commonOptions.windowMode.argument, updateConfigs=False)
        self.setProductMode(self._configs.commonOptions.productMode.argument, updateConfigs=False)
        self.setLogLevel(self._configs.commonOptions.logLevel.argument, updateConfigs=False)
        self.setDebugOption(self._configs.commonOptions.debugOption.argument, updateConfigs=False)
        self.setCleanBeforePack(self._configs.commonOptions.cleanBeforePack.isSet, updateConfigs=False)
        self.setNoConfirm(self._configs.commonOptions.noConfirm.isSet, updateConfigs=False)
        self.setStripSymbolTable(self._configs.commonOptions.stripSymbolTable.isSet, updateConfigs=False)
        self.setASCIIOnly(self._configs.commonOptions.asciiOnly.isSet, updateConfigs=False)
        self.addSearchPaths(self._configs.commonOptions.searchPaths.argument, clearBeforeAdd=False, updateConfigs=False)
        self.addExtraData(self._configs.commonOptions.extraData.argument, clearBeforeAdd=False, updateConfigs=False)
        self.makeLink(self.extraBinaries, self._configs.commonOptions.extraBinaries)

    def setPyInstallerPath(self, path, updateConfigs=True):
        self.pyinstaller = path
        if updateConfigs:
            self._configs.pyinstaller = self.pyinstaller

    def setName(self, name, updateConfigs=True):
        self.name = name
        if updateConfigs:
            self._configs.name = self.name

    def setAuthor(self, author, updateConfigs=True):
        self.author = author
        if updateConfigs:
            self._configs.author = self.author

    def setVersion(self, version, updateConfigs=True):
        self.version = version
        if updateConfigs:
            self._configs.version = self.version

    def setDescription(self, description, updateConfigs=True):
        self.description = description
        if updateConfigs:
            self._configs.description = self.description

    def addScripts(self, scripts, clearBeforeAdd=False, updateConfigs=True):
        if clearBeforeAdd:
            self.scripts.clear()
            self.scripts.extend(scripts)
            if updateConfigs:
                self._configs.scripts = self.scripts
            return

        for script in scripts:
            if script in self.scripts:
                continue
            self.scripts.append(script)
        if updateConfigs:
            self._configs.scripts = self.scripts

    def removeScripts(self, scripts, updateConfigs=True):
        for s in scripts:
            index = self.scripts.index(s)
            if index >= 0:
                del self.scripts[index]
        if updateConfigs:
            self._configs.scripts = self.scripts

    def setProductName(self, name, updateConfigs=True):
        if name is None:
            name = ""
        self.productName = name
        if updateConfigs:
            self._configs.commonOptions.productName.argument = self.productName

    def setDistPath(self, path=None, updateConfigs=True):
        if path is None:
            path = ""
        self.distPath = path
        if updateConfigs:
            self._configs.commonOptions.distPath.argument = self.distPath

    def setWorkPath(self, path, updateConfigs=True):
        if path is None:
            path = ""
        self.workPath = path
        if updateConfigs:
            self._configs.commonOptions.workPath.argument = self.workPath

    def setSpecPath(self, path, updateConfigs=True):
        if path is None:
            path = ""
        self.specPath = path
        if updateConfigs:
            self._configs.commonOptions.specPath.argument = self.specPath

    def setAppIcon(self, icon, updateConfigs=True):
        if icon is None:
            icon = ""
        self.appIcon = icon
        if updateConfigs:
            self._configs.commonOptions.icon.argument = self.appIcon

    def setSplash(self, splash, updateConfigs=False):
        if splash is None:
            splash = ""
        self.splash = splash
        if updateConfigs:
            self._configs.commonOptions.splash.argument = self.splash

    def setEncryptionKey(self, key, updateConfigs=True):
        if key is None:
            key = ""
        self.encryptionKey = key
        if updateConfigs:
            self._configs.commonOptions.encryptionKey.argument = self.encryptionKey

    def setWindowMode(self, mode, updateConfigs=True):
        if mode is None or mode == "":
            mode = OPTION_BY_DEFAULT
        self.windowMode = mode
        if updateConfigs:
            self._configs.commonOptions.windowMode.argument = self.windowMode

    def setProductMode(self, mode, updateConfigs=True):
        if mode is None or mode == "":
            mode = OPTION_BY_DEFAULT
        self.productMode = mode
        if updateConfigs:
            self._configs.commonOptions.productMode.argument = self.productMode

    def setLogLevel(self, level, updateConfigs=True):
        if level is None or level == "":
            level = OPTION_BY_DEFAULT
        self.logLevel = level
        if updateConfigs:
            self._configs.commonOptions.logLevel.argument = self.logLevel

    def setDebugOption(self, option, updateConfigs=True):
        if option is None or option == "":
            option = OPTION_BY_DEFAULT
        self.debugOption = option
        if updateConfigs:
            self._configs.commonOptions.debugOption.argument = self.debugOption

    def setCleanBeforePack(self, enable, updateConfigs=True):
        self.cleanBeforePack = mapBoolFlag(enable)
        if updateConfigs:
            if self.cleanBeforePack:
                self._configs.commonOptions.cleanBeforePack.set()
            else:
                self._configs.commonOptions.cleanBeforePack.unset()

    def setNoConfirm(self, noConfirm, updateConfigs=True):
        self.onConfirm = mapBoolFlag(noConfirm)
        if updateConfigs:
            if self.onConfirm:
                self._configs.commonOptions.noConfirm.set()
            else:
                self._configs.commonOptions.noConfirm.unset()

    def setStripSymbolTable(self, strip, updateConfigs=True):
        self.stripSymbolTable = mapBoolFlag(strip)
        if updateConfigs:
            if self.stripSymbolTable:
                self._configs.commonOptions.stripSymbolTable.set()
            else:
                self._configs.commonOptions.stripSymbolTable.unset()

    def setASCIIOnly(self, asciiOnly, updateConfigs=True):
        self.asciiOnly = mapBoolFlag(asciiOnly)
        if updateConfigs:
            if self.asciiOnly:
                self._configs.commonOptions.asciiOnly.set()
            else:
                self._configs.commonOptions.asciiOnly.unset()

    def addSearchPaths(self, paths, clearBeforeAdd=False, updateConfigs=True):
        if clearBeforeAdd:
            self.searchPaths.clear()
            self.searchPaths.extend(paths)
            if updateConfigs:
                self._configs.commonOptions.searchPaths.unset()
                self._configs.commonOptions.searchPaths.addAll(*self.searchPaths)
            return

        for path in paths:
            if path in self.searchPaths:
                continue
            self.searchPaths.append(path)

        if updateConfigs:
            self._configs.commonOptions.searchPaths.unset()
            self._configs.commonOptions.searchPaths.addAll(*self.searchPaths)

    def removeSearchPaths(self, paths, updateConfigs=True):
        for path in paths:
            idx = self.searchPaths.index(path)
            if idx >= 0:
                del self.searchPaths[idx]

        if updateConfigs:
            self._configs.commonOptions.searchPaths.unset()
            self._configs.commonOptions.searchPaths.addAll(*self.searchPaths)

    def clearSearchPaths(self, updateConfigs=True):
        self.searchPaths = []
        if updateConfigs:
            self._configs.commonOptions.searchPaths.unset()

    def addExtraData(self, dataPaths, clearBeforeAdd=False, updateConfigs=True):
        if clearBeforeAdd:
            self.extraData.clear()
            self.extraData.extend(dataPaths)
            if updateConfigs:
                self._configs.commonOptions.extraData.unset()
                self._configs.commonOptions.extraData.addAll(*self.extraData)
            return

        for path in dataPaths:
            if path in self.extraData:
                continue
            self.extraData.append(path)

        if updateConfigs:
            self._configs.commonOptions.extraData.unset()
            self._configs.commonOptions.extraData.addAll(*self.extraData)

    def removeExtraData(self, data, updateConfigs=True):
        for path in data:
            idx = self.extraData.index(path)
            if idx >= 0:
                del self.extraData[idx]

        if updateConfigs:
            self._configs.commonOptions.extraData.unset()
            self._configs.commonOptions.extraData.addAll(*self.extraData)

    def updateExtraData(self, index, data, updateConfigs=True):
        if index < 0 or index >= len(self.extraData):
            return
        self.extraData[index] = data
        if updateConfigs:
            self._configs.commonOptions.extraData.unset()
            self._configs.commonOptions.extraData.addAll(*self.extraData)

    def makeLink(self, state, config):
        self.extraBinaries = config.argument
        config.argument = self.extraBinaries
        print(self.extraBinaries, type(self.extraBinaries))