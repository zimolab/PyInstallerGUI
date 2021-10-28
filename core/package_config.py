# -*- coding:utf-8 -*-
"""
NOTE: The description of each option is from official documentation of pyinstaller.
Check https://pyinstaller.readthedocs.io/en/stable/usage.html for more details.
"""
import json
import platform
from os import makedirs
from os.path import dirname

from PySide2.QtWidgets import QLineEdit, QListWidget, QTextEdit
from QBinder import Binder

from core.constants import DEFAULT_PYINSTALLER_PATH, DEFAULT_PYIMAKESPEC_PATH, DEFAULT_VERSION, DEFAULT_DESCRIPTION, \
    DEFAULT_ENCODINGS
from core.options import Options, StringOption, FlagOption, DEFAULT_VALUE_UNSET, MultiOption, \
    BaseBindingOption
from utils import isEmpty, isNull


class PackageConfig(object):
    CMD_PYINSTALLER = 0
    CMD_PYIMAKESPEC = 0

    def __init__(self):
        self._state = Binder()
        self._state.pyinstaller = DEFAULT_PYINSTALLER_PATH
        self._state.pyimakespec = DEFAULT_PYIMAKESPEC_PATH
        self._state.name = ""
        self._state.author = ""
        self._state.version = DEFAULT_VERSION
        self._state.description = DEFAULT_DESCRIPTION
        self._state.scripts = []
        self.commonOptions = self.CommonOptions()
        self.hookOptions = self.HookOptions()
        self.upxOptions = self.UPXOptions()
        self.windowsOptions = self.WindowsOptions()
        self.macOSXOptions = self.MacOSXOptions()

    @property
    def pyinstaller(self):
        return self._state.pyinstaller

    @pyinstaller.setter
    def pyinstaller(self, val):
        self._state.pyinstaller = val

    @property
    def pyimakespec(self):
        return self._state.pyimakespec

    @pyimakespec.setter
    def pyimakespec(self, val):
        self._state.pyimakespec = val

    @property
    def name(self):
        return self._state.name

    @name.setter
    def name(self, val):
        self._state.name = val

    @property
    def author(self):
        return self._state.author

    @author.setter
    def author(self, val):
        self._state.author = val

    @property
    def version(self):
        return self._state.version

    @version.setter
    def version(self, val):
        self._state.version = val

    @property
    def description(self):
        return self._state.description

    @description.setter
    def description(self, val):
        self._state.description = val

    @property
    def scripts(self):
        return self._state.scripts

    def reset(self):
        # non-options
        self._state.pyinstaller = DEFAULT_PYINSTALLER_PATH
        self._state.pyimakespec = DEFAULT_PYIMAKESPEC_PATH
        self._state.name = ""
        self._state.author = ""
        self._state.version = DEFAULT_VERSION
        self._state.description = DEFAULT_DESCRIPTION
        self.clearScripts()
        # options
        options = []
        options.extend(self.commonOptions.getOptions(withNames=False))
        options.extend(self.hookOptions.getOptions(withNames=False))
        options.extend(self.upxOptions.getOptions(withNames=False))
        options.extend(self.windowsOptions.getOptions(withNames=False))
        options.extend(self.macOSXOptions.getOptions(withNames=False))
        for opt in options:
            opt.unset()
        del options[:]
        del options

    def load(self, path, reset=True, ignoreErrors=True):
        if reset:
            self.reset()
        with open(path, "r", encoding=DEFAULT_ENCODINGS) as file:
            jsonData = json.load(file)
            if not isinstance(jsonData, dict):
                if ignoreErrors:
                    return
                else:
                    raise RuntimeError("bad file format")

        self.pyinstaller = self._get(jsonData, "pyinstaller", DEFAULT_PYINSTALLER_PATH)
        self.pyimakespec = self._get(jsonData, "pyi-makespec", DEFAULT_PYIMAKESPEC_PATH)
        self.name = self._get(jsonData, "name", "")
        self.author = self._get(jsonData, "author", "")
        self.version = self._get(jsonData, "version", DEFAULT_VERSION)
        self.description = self._get(jsonData, "description", DEFAULT_DESCRIPTION)
        scripts = self._get(jsonData, "scripts", [])
        if isinstance(scripts, list):
            self.addScripts(*scripts)

        try:
            if "options" in jsonData:
                options = jsonData["options"]
                self.deserializeOptions(options, self.commonOptions)
                if "hooks" in options:
                    self.deserializeOptions(options["hooks"], self.hookOptions)
                if "upx" in options:
                    self.deserializeOptions(options["upx"], self.upxOptions)
                if "windows" in options:
                    self.deserializeOptions(options["windows"], self.windowsOptions)
                if "macOSX" in options:
                    self.deserializeOptions(options["macOSX"], self.macOSXOptions)
        except Exception as e:
            if ignoreErrors:
                return
            else:
                raise e

    def addScripts(self, *scripts):
        for script in scripts:
            if isNull(script):
                return
            if isinstance(script, str) or isinstance(script, bytes):
                script = script.strip()
            if isEmpty(script):
                return
            if script not in self.scripts:
                self._state.scripts.append(script)

    def addScript(self, script):
        if isNull(script):
            return
        if isinstance(script, str) or isinstance(script, bytes):
            script = script.strip()
        if isEmpty(script):
            return
        if script not in self.scripts:
            self._state.scripts.append(script)

    def removeScript(self, script):
        if script in self._state.scripts:
            self._state.scripts.remove(script)

    def removeScripts(self, *scripts):
        for script in scripts:
            self.removeScript(script)

    def removeScriptAt(self, index):
        if index < 0 or index >= len(self._state.scripts):
            return
        self._state.scripts.pop(index)

    def clearScripts(self):
        self._state.scripts.clear()
        del self._state.scripts[:]

    def replaceScriptsWith(self, newScripts):
        self.clearScripts()
        self.addScripts(*newScripts)

    def updateScriptAt(self, index, newScript):
        if isNull(newScript):
            return
        if isinstance(newScript, str) or isinstance(newScript, bytes):
            newScript = newScript.strip()
        if isEmpty(newScript):
            return
        # 防止访问越界
        if index < 0 or index >= len(self._state.scripts):
            return
        # 防止元素重复
        if newScript in self._state.scripts:
            return
        self._state.scripts[index] = newScript

    def bind(self, target, widget):
        if target == "pyinstaller":
            assert isinstance(widget, QLineEdit)

            def onPyinstallerChanged(path):
                self.pyinstaller = path

            widget.setText(lambda: self.pyinstaller * 1)
            widget.textChanged.connect(onPyinstallerChanged)
            self.pyinstaller = self.pyinstaller

        elif target == "pyimakespec":
            assert isinstance(widget, QLineEdit)

            def onPyimakespecChanged(path):
                self.pyimakespec = path

            widget.setText(lambda: self.pyimakespec * 1)
            widget.textChanged.connect(onPyimakespecChanged)
            self.pyimakespec = self.pyimakespec

        elif target == "name":
            assert isinstance(widget, QLineEdit)

            def onNameChanged(name):
                self.name = name

            widget.setText(lambda: self.name * 1)
            widget.textChanged.connect(onNameChanged)
            self.name = self.name

        elif target == "author":
            assert isinstance(widget, QLineEdit)

            def onAuthorChanged(author):
                self.author = author

            widget.setText(lambda: self.author * 1)
            widget.textChanged.connect(onAuthorChanged)
            self.author = self.author

        elif target == "version":
            assert isinstance(widget, QLineEdit)

            def onVersionChanged(version):
                self.version = version

            widget.setText(lambda: self.version * 1)
            widget.textChanged.connect(onVersionChanged)
            self.version = self.version

        elif target == "description":
            assert isinstance(widget, QTextEdit)
            _w = widget

            def onDescriptionChanged():
                self.description = _w.toPlainText()

            widget.setPlainText(lambda: self.description * 1)
            widget.textChanged.connect(onDescriptionChanged)
            self.description = self.description

        elif target == "scripts":
            assert isinstance(widget, QListWidget)
            _w = widget

            def onUpdateItems():
                _w.clear()
                return self._state.scripts

            widget.addItems(onUpdateItems)
            self._state.scripts = self._state.scripts

        else:
            raise RuntimeError(f"unknown target name '{target}'")

    def toJSON(self, excludes=None):
        serialized = {
            "name": self.name,
            "author": self.author,
            "version": self.version,
            "description": self.description,
            "pyinstaller": self.pyinstaller,
            "pyimakespec": self.pyimakespec,
            "scripts": self.scripts,
            "options": {
            }
        }

        commonOptions = self.commonOptions.getOptions(filterUnsetOptions=True, withNames=True)
        self.serializeOptions(serialized["options"], commonOptions, excludes)
        upxOptions = self.upxOptions.getOptions(filterUnsetOptions=True, withNames=True)
        serialized["options"]["upx"] = {}
        self.serializeOptions(serialized["options"]["upx"], upxOptions, excludes)

        hookOptions = self.hookOptions.getOptions(filterUnsetOptions=True, withNames=True)
        serialized["options"]["hooks"] = {}
        self.serializeOptions(serialized["options"]["hooks"], hookOptions, excludes)

        windowsOptions = self.windowsOptions.getOptions(filterUnsetOptions=True, withNames=True)
        serialized["options"]["windows"] = {}
        self.serializeOptions(serialized["options"]["windows"], windowsOptions, excludes)

        macosxOptions = self.macOSXOptions.getOptions(filterUnsetOptions=True, withNames=True)
        serialized["options"]["macOSX"] = {}
        self.serializeOptions(serialized["options"]["macOSX"], macosxOptions, excludes)

        return json.dumps(serialized, indent=4, ensure_ascii=False)

    @classmethod
    def serializeOptions(cls, serialized, options, excludes=None):
        if excludes is None:
            excludes = []
        for name, opt in options:
            if name in excludes:
                continue
            if isinstance(opt, BaseBindingOption):
                serialized[name] = opt.argument
            else:
                raise ValueError(f"unknown options type: {type(options)}")

    @classmethod
    def deserializeOptions(cls, src, target):
        for key in src.keys():
            val = src[key]
            if val == DEFAULT_VALUE_UNSET:
                continue
            if not hasattr(target, key) or key.startswith("_") or isinstance(val, dict):
                continue
            opt = getattr(target, key)
            if not isinstance(opt, BaseBindingOption):
                continue
            if isinstance(opt, MultiOption):
                if isinstance(val, list) and len(val) > 0:
                    opt.addAll(True, *val)
            elif isinstance(opt, StringOption):
                opt.argument = val
            elif isinstance(opt, FlagOption):
                opt.set(val)

    @staticmethod
    def _get(d, key, defaultValue):
        if key in d:
            return d[key]
        return defaultValue

    @classmethod
    def loadFromFile(cls, path, ignoreErrors=True):
        configs = cls()
        with open(path, "r", encoding=DEFAULT_ENCODINGS) as file:
            jsonData = json.load(file)
            if not isinstance(jsonData, dict):
                if ignoreErrors:
                    return configs
                else:
                    raise RuntimeError("bad file format")

        configs.pyinstaller = cls._get(jsonData, "pyinstaller", configs.pyinstaller)
        configs.pyimakespec = cls._get(jsonData, "pyimakespec", configs.pyimakespec)
        configs.name = cls._get(jsonData, "name", configs.name)
        configs.author = cls._get(jsonData, "author", configs.author)
        configs.version = cls._get(jsonData, "version", configs.version)
        configs.description = cls._get(jsonData, "description", configs.description)
        scripts = cls._get(jsonData, "scripts", [])
        if isinstance(scripts, list):
            configs.addScripts(*scripts)

        try:
            if "options" in jsonData:
                options = jsonData["options"]
                cls.deserializeOptions(options, configs.commonOptions)
                if "hooks" in options:
                    cls.deserializeOptions(options["hooks"], configs.hookOptions)
                if "upx" in options:
                    cls.deserializeOptions(options["upx"], configs.upxOptions)
                if "windows" in options:
                    cls.deserializeOptions(options["windows"], configs.windowsOptions)
                if "macOSX" in options:
                    cls.deserializeOptions(options["macOSX"], configs.macOSXOptions)
        except Exception as e:
            if ignoreErrors:
                return configs
            else:
                raise e
        else:
            return configs

    def saveToFile(self, path):
        dirs = dirname(path)
        makedirs(dirs, exist_ok=True)
        with open(path, "wb") as file:
            file.write(self.toJSON().encode(DEFAULT_ENCODINGS))

    def toCommandLine(self, cmd, useCurrentPlatformConfigs=True):
        return f"{cmd} {self.toOptionsLine(useCurrentPlatformConfigs)}"

    def toOptionsLine(self, useCurrentPlatformConfigs=True):
        argList = self.toOptionsList(useCurrentPlatformConfigs)
        cmd = f"{' '.join(argList)} {' '.join(self.scripts)}"
        return cmd

    def toOptionsList(self, useCurrentPlatformConfigs=True):
        argList = []
        argList.extend(self.commonOptions.toStringList())
        argList.extend(self.hookOptions.toStringList())
        argList.extend(self.upxOptions.toStringList())

        if useCurrentPlatformConfigs:
            if platform.system().lower() == "windows":
                argList.extend(self.windowsOptions.toStringList())
            if platform.system().lower() == "darwin":
                argList.extend(self.macOSXOptions.toStringList())
        else:
            argList.extend(self.windowsOptions.toStringList())
            argList.extend(self.macOSXOptions.toStringList())

        return argList

    class CommonOptions(Options):
        def __init__(self):
            self.distPath = StringOption(
                name="distpath",
                description="--distpath DIR: "
                            "Where to put the bundled app (default: ./dist)."
            )

            self.workPath = StringOption(
                name="workpath",
                description="--workpath WORKPATH: "
                            "Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)."
            )

            self.specPath = StringOption(
                name="specpath",
                description="--specpath DIR: "
                            "Folder to store the base spec file (default: current directory)."
            )

            self.noConfirm = FlagOption(
                name="noconfirm",
                description="-y, --noconfirm: "
                            "Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for "
                            "confirmation. "
            )

            self.asciiOnly = FlagOption(
                name="ascii",
                description="-a, --ascii: "
                            "Do not include unicode encoding support (default: included if available)."
            )

            self.clean = FlagOption(
                name="clean",
                description="--clean: "
                            "Clean PyInstaller cache and remove temporary files before building."
            )

            self.logLevel = StringOption(
                name="log-level",
                choices=(
                    DEFAULT_VALUE_UNSET,
                    "TRACE",
                    "DEBUG",
                    "INFO",
                    "WARN",
                    "ERROR",
                    "CRITICAL"),
                description="--log-level LEVEL: "
                            "Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, "
                            "WARN, ERROR, CRITICAL (default: INFO). "
            )

            self.productMode = StringOption(
                name="",
                choices=(DEFAULT_VALUE_UNSET, "onefile", "onedir"),
                connector="",
                description="-D, --onedir or -F, --onefile: "
                            "Create a one-folder bundle containing an executable (default) or "
                            "Create a one-file bundled executable."
            )

            self.windowMode = StringOption(
                name="",
                choices=(DEFAULT_VALUE_UNSET, "windowed", "console"),
                connector="",
                description="-w, --windowed, --noconsole or -c, --console, --nowindowed: "
                            "(-w, --windowed, --noconsole)Windows and Mac OS X: do not provide a console window for "
                            "standard i/o. On Mac OS X this also triggers building an OS X .app bundle. On Windows "
                            "this option will be set if the first script is a ‘.pyw’ file. This option is ignored in "
                            "*NIX systems. (-c, --console, --nowindowed) Open a console window for standard i/o ("
                            "default). On Windows this option will have no effect if the first script is a ‘.pyw’ "
                            "file. ",
            )

            self.productName = StringOption(
                name="name",
                description="-n NAME, --name NAME: "
                            "Name to assign to the bundled app and spec file (default: first script’s basename)."
            )

            self.addData = MultiOption(
                name="add-data",
                description="--add-data <SRC;DEST or SRC:DEST>: "
                            "Additional non-binary files or folders to be added to the executable. The path separator "
                            "is platform specific, os.pathsep (which is ; on Windows and : on most unix systems) is "
                            "used. ",
                wrapArgument=True
            )

            self.addBinary = MultiOption(
                name="add-binary",
                description="--add-binary <SRC;DEST or SRC:DEST>: "
                            "Additional binary files to be added to the executable. ",
                wrapArgument=True
            )

            self.paths = MultiOption(
                name="paths",
                description="-p DIR, --paths DIR: "
                            "A path to search for imports (like using PYTHONPATH). Multiple paths are allowed, "
                            "separated by ':', or use this option multiple times. "
            )

            self.hiddenImports = MultiOption(
                name="hidden-import",
                description="--hidden-import MODULENAME, --hiddenimport MODULENAME: "
                            "Name an import not visible in the code of the script(s). "
            )

            self.collectSubmodules = MultiOption(
                name="collect-submodules",
                description="--collect-submodules MODULENAME: "
                            "Collect all submodules from the specified package or module."
            )

            self.collectData = MultiOption(
                name="collect-data",
                description="--collect-data MODULENAME, --collect-datas MODULENAME: "
                            "Collect all data from the specified package or module."
            )

            self.collectBinaries = MultiOption(
                name="collect-binaries",
                description="--collect-binaries MODULENAME: "
                            "Collect all binaries from the specified package or module."
            )

            self.collectAll = MultiOption(
                name="collect-all",
                description="-collect-all MODULENAME: "
                            "Collect all submodules, data files, and binaries from the specified package or module."
            )

            self.copyMetadata = MultiOption(
                name="copy-metadata",
                description="--copy-metadata PACKAGENAME: "
                            "Copy metadata for the specified package. "
            )

            self.recursiveCopyMetadata = MultiOption(
                name="recursive-copy-metadata",
                description="--recursive-copy-metadata PACKAGENAME: "
                            "Copy metadata for the specified package and all its dependencies."
            )

            self.excludeModule = MultiOption(
                name="exclude-module",
                description="--exclude-module EXCLUDES: "
                            "Optional module or package (the Python name, not the path name) that will be ignored (as "
                            "though it was not found). "
            )

            self.key = StringOption(
                name="key",
                description="--key KEY: "
                            "The key used to encrypt Python bytecode."
            )

            self.splash = StringOption(
                name="splash",
                description="--splash IMAGE_FILE: "
                            "(EXPERIMENTAL) Add an splash screen with the image IMAGE_FILE to the application. The "
                            "splash screen can show progress updates while unpacking. "
            )

            self.debug = StringOption(
                name="debug",
                choices=[DEFAULT_VALUE_UNSET, "all", "imports", "bootloader", "noarchive"],
                description="-d {all,imports,bootloader,noarchive}, --debug {all,imports,bootloader,noarchive}: "
                            "Provide assistance with debugging a frozen application. This argument may be provided "
                            "multiple times to select several of the following options. - all: All three of the "
                            "following options. - imports: specify the -v option to the underlying Python "
                            "interpreter, causing it to print a message each time a module is initialized, "
                            "showing the place (filename or built-in module) from which it is loaded. - bootloader: "
                            "tell the bootloader to issue progress messages while initializing and starting the "
                            "bundled app. Used to diagnose problems with missing imports. - noarchive: instead of "
                            "storing all frozen Python source files as an archive inside the resulting executable, "
                            "store them as files in the resulting output directory. "
            )

            self.strip = FlagOption(
                name="strip",
                description="-s, --strip: "
                            "Apply a symbol-table strip to the executable and shared libs (not recommended for "
                            "Windows). "
            )

            self.icon = StringOption(
                name="icon",
                description="--icon <FILE.ico or FILE.exe,ID or FILE.icns or 'NONE'>: "
                            "FILE.ico: apply that icon to a Windows executable. "
                            "FILE.exe,ID, extract the icon with ID from an exe. "
                            "FILE.icns: apply the icon to the .app bundle on Mac OS X. "
                            "Use 'NONE' to not apply any icon, thereby making the OS to show some default "
                            "(default: apply PyInstaller’s icon)"
            )

            self.runtimeTmpDir = StringOption(
                name="runtime-tmpdir",
                description="--runtime-tmpdir PATH: "
                            "Where to extract libraries and support files in onefile-mode. If this option is given, "
                            "the bootloader will ignore any temp-folder location defined by the run-time OS."
                            " The _MEIxxxxxx-folder will be created here. "
                            "Please use this option only if you know what you are doing."
            )

            self.bootloaderIgnoreSignals = FlagOption(
                name="bootloader-ignore-signals",
                description="--bootloader-ignore-signals: "
                            "Tell the bootloader to ignore signals rather than forwarding them to the child process. "
                            "Useful in situations where e.g. a supervisor process signals both the bootloader and "
                            "child (e.g. via a process group) to avoid signalling the child twice. "
            )

            self.disableWindowedTraceback = FlagOption(
                name="disable-windowed-traceback",
                description="--disable-windowed-traceback: "
                            "Disable traceback dump of unhandled exception in windowed (noconsole) mode (Windows and "
                            "macOS only), and instead display a message that this feature is disabled. "
            )

    class HookOptions(Options):
        def __init__(self):
            self.additionalHooksDir = MultiOption(
                name="additional-hooks-dir",
                description="--additional-hooks-dir HOOKSPATH: "
                            "An additional path to search for hooks. "
            )

            self.runtimeHook = MultiOption(
                name="runtime-hook",
                description="--runtime-hook RUNTIME_HOOKS: "
                            "Path to a custom runtime hook file. A runtime hook is code that is bundled with the "
                            "executable and is executed before any other code or module to set up special features of "
                            "the runtime environment. "
            )

    class UPXOptions(Options):
        def __init__(self):
            self.noUPX = FlagOption(
                name="noupx",
                description="--noupx: "
                            "Do not use UPX even if it is available (works differently between Windows and *nix)"
            )
            self.upxDir = StringOption(
                name="upx-dir",
                description="--upx-dir UPX_DIR: "
                            "Path to UPX utility (default: search the execution path)"
            )
            self.upxExclude = MultiOption(
                name="upx-exclude",
                description="--upx-exclude FILE:"
                            "Prevent a binary from being compressed when using upx. This is typically used if upx "
                            "corrupts certain binaries during compression. FILE is the filename of the binary without "
                            "path. "
            )

    class WindowsOptions(Options):
        def __init__(self):
            self.versionFile = StringOption(
                name="version-file",
                description="--version-file FILE: "
                            "add a version resource from FILE to the exe."
            )
            self.manifest = StringOption(
                name="manifest",
                description="-m <FILE or XML>, --manifest <FILE or XML>: "
                            "add manifest FILE or XML to the exe."
            )

            self.resource = StringOption(
                name="resource",
                description="-r RESOURCE, --resource RESOURCE: "
                            "Add or update a resource to a Windows executable. The RESOURCE is one to four items, "
                            "FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE can be a data file or an exe/dll. For data files, "
                            "at least TYPE and NAME must be specified. LANGUAGE defaults to 0 or may be specified as "
                            "wildcard * to update all resources of the given TYPE and NAME. For exe/dll files, "
                            "all resources from FILE will be added/updated to the final executable if TYPE, "
                            "NAME and LANGUAGE are omitted or specified as wildcard * "
            )
            self.uacAdmin = FlagOption(
                name="uac-admin",
                description="--uac-admin: "
                            "Using this option creates a Manifest which will request elevation upon application "
                            "restart. "
            )
            self.uacUIAccess = FlagOption(
                name="uac-uiaccess",
                description="--uac-uiaccess: "
                            "Using this option allows an elevated application to work with Remote Desktop."
            )
            self.winPrivateAssemblies = FlagOption(
                name="win-private-assemblies",
                description="--win-private-assemblies: "
                            "Any Shared Assemblies bundled into the application will be changed into Private "
                            "Assemblies. This means the exact versions of these assemblies will always be used, "
                            "and any newer versions installed on user machines at the system level will be ignored. "
            )

            self.winNoPreferRedirects = FlagOption(
                name="win-no-prefer-redirects",
                description="--win-no-prefer-redirects: "
                            "While searching for Shared or Private Assemblies to bundle into the application, "
                            "PyInstaller will prefer not to follow policies that redirect to newer versions, "
                            "and will try to bundle the exact versions of the assembly. "
            )

    class MacOSXOptions(Options):
        def __init__(self):
            self.osxBundleIdentifier = StringOption(
                name="osx-bundle-identifier",
                description="--osx-bundle-identifier BUNDLE_IDENTIFIER: "
                            "Mac OS X .app bundle identifier is used as the default unique program name for code "
                            "signing purposes. The usual form is a hierarchical name in reverse DNS notation. For "
                            "example: com.mycompany.department.appname (default: first script’s basename) "
            )

            self.targetArchitecture = StringOption(
                name="target-arch",
                choices=[DEFAULT_VALUE_UNSET, "x86_64", "arm64", "universal2"],
                description="--target-architecture ARCH, --target-arch ARCH: "
                            "Target architecture (macOS only; valid values: x86_64, arm64, universal2). Enables "
                            "switching between universal2 and single-arch version of frozen application (provided "
                            "python installation supports the target architecture). If not target architecture is not "
                            "specified, the current running architecture is targeted. "
            )

            self.codesignIdentity = StringOption(
                name="codesign-identity",
                description="--codesign-identity IDENTITY: "
                            "Code signing identity (macOS only). Use the provided identity to sign collected binaries "
                            "and base executable. If signing identity is not provided, ad- hoc signing is "
                            "performed instead. "
            )

            self.entitlementsFile = StringOption(
                name="entitlements-file",
                description="--osx-entitlements-file FILENAME: "
                            "Entitlements file to use when code-signing the collected binaries (macOS only)."
            )
