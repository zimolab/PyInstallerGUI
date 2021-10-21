# -*- coding:utf-8 -*-
import json
import platform
from os import makedirs
from os.path import dirname
from core.option import *
from core.option import OPTION_BY_DEFAULT


class Options(object):
    def toCommandArgList(self):
        optionsSet = self.getOptions(filterUnsetOptions=True)
        return [o.stringify() for o in optionsSet]

    def getOptions(self, filterUnsetOptions=False):
        options = []
        for p in dir(self):
            val = getattr(self, p)
            if isinstance(val, Option):
                if filterUnsetOptions:
                    if val.isSet:
                        options.append(val)
                else:
                    options.append(val)
        return options

    def getOptionsWithName(self, filterUnsetOptions=False):
        options = []
        for p in dir(self):
            val = getattr(self, p)
            if isinstance(val, Option):
                if filterUnsetOptions:
                    if val.isSet:
                        options.append((p, val))
                else:
                    options.append((p, val))
        return options


"""
NOTE: The description of each option comes from official documentation of pyinstaller.
Check https://pyinstaller.readthedocs.io/en/stable/usage.html for more details.
"""


class PackageConfigs(object):
    def __init__(self):
        self.pyinstaller = "pyinstaller"
        self.name = ""
        self.author = ""
        self.version = "0.0.1"
        self.description = ""
        self.scripts = []
        self.commonOptions = self.CommonOptions()
        self.windowsOptions = self.WindowsOptions()
        self.macosOptions = self.MacOSOptions()
        self.upxOptions = self.UPXOptions()
        self.hookOptions = self.HookOptions()

    class CommonOptions(Options):
        def __init__(self):
            self.distPath = Option(
                name="distpath",
                hasArgument=True,
                desc="--distpath DIR: "
                     "Where to put the bundled app (default: ./dist)"
            )

            self.workPath = Option(
                name="workpath",
                hasArgument=True,
                desc="--workpath WORKPATH: "
                     "Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)"
            )

            self.specPath = Option(
                name="specpath",
                hasArgument=True,
                desc="--specpath DIR: "
                     "Folder to store the generated spec file (default: current directory)"
            )

            self.noConfirm = Option(
                name="noconfirm",
                hasArgument=False,
                desc="-y, --noconfirm: "
                     "Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation"
            )

            self.asciiOnly = Option(
                name="ascii",
                hasArgument=False,
                desc="-a, --ascii: "
                     "Do not include unicode encoding support (default: included if available)"
            )

            self.cleanBeforePack = Option(
                name="clean",
                hasArgument=False,
                desc="--clean: "
                     "Clean PyInstaller cache and remove temporary files before building."
            )

            self.logLevel = Option(
                name="log-level",
                hasArgument=True,
                argumentChoices=[
                    OPTION_BY_DEFAULT,
                    "TRACE",
                    "DEBUG",
                    "INFO",
                    "WARN",
                    "ERROR",
                    "CRITICAL"],
                desc="--log-level LEVEL: "
                     "Amount of detail in build-time console messages. "
                     "LEVEL may be one of TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO)."
            )

            self.productMode = Option(
                name="",
                hasArgument=True,
                argumentChoices=[OPTION_BY_DEFAULT, "onefile", "onedir"],
                connector="",
                desc="-D, --onedir or -F, --onefile: "
                     "Create a one-folder bundle containing an executable (default) or "
                     "Create a one-file bundled executable."
            )

            self.productName = Option(
                name="name",
                hasArgument=True,
                desc="-n NAME, --name NAME: "
                     "Name to assign to the bundled app and spec file (default: first script’s basename)"
            )

            self.extraDataPaths = MultipleOption(
                name="add-data",
                desc="--add-data <SRC;DEST or SRC:DEST>: "
                     "Additional non-binary files or folders to be added to the executable. "
                     "The path separator is platform specific, os.pathsep "
                     "(which is ; on Windows and : on most unix systems) is used."
            )

            self.extraBinaryPaths = MultipleOption(
                name="add-binary",
                desc="--add-binary <SRC;DEST or SRC:DEST>: "
                     "Additional binary files to be added to the executable. "
            )

            self.searchPaths = MultipleOption(
                name="paths",
                desc="-p DIR, --paths DIR: "
                     "A path to search for imports (like using PYTHONPATH). "
                     "Multiple paths are allowed, separated by ':', or use this option multiple times."
            )

            self.hiddenImports = MultipleOption(
                name="hidden-import",
                desc="--hidden-import MODULENAME, --hiddenimport MODULENAME: "
                     "Name an import not visible in the code of the script(s). "
            )

            self.collectSubmodules = MultipleOption(
                name="collect-submodules",
                desc="--collect-submodules MODULENAME: "
                     "Collect all submodules from the specified package or module."
            )

            self.collectData = MultipleOption(
                name="collect-data",
                desc="--collect-data MODULENAME, --collect-datas MODULENAME: "
                     "Collect all data from the specified package or module."
            )

            self.collectBinaries = MultipleOption(
                name="collect-binaries",
                desc="--collect-binaries MODULENAME: "
                     "Collect all binaries from the specified package or module."
            )

            self.collectAll = MultipleOption(
                name="collect-all",
                desc="-collect-all MODULENAME: "
                     "Collect all submodules, data files, and binaries from the specified package or module."
            )

            self.copyMeta = MultipleOption(
                name="copy-metadata",
                desc="--copy-metadata PACKAGENAME: "
                     "Copy metadata for the specified package. "
            )

            self.recursiveCopyMetadata = MultipleOption(
                name="recursive-copy-metadata",
                desc="--recursive-copy-metadata PACKAGENAME: "
                     "Copy metadata for the specified package and all its dependencies."
            )

            self.excludeModules = MultipleOption(
                name="exclude-module",
                desc="--exclude-module EXCLUDES: "
                     "Optional module or package (the Python name, not the path name) that will be ignored "
                     "(as though it was not found)"
            )

            self.encryptionKey = Option(
                name="key",
                hasArgument=True,
                desc="--key KEY: "
                     "The key used to encrypt Python bytecode."
            )

            self.splash = Option(
                name="splash",
                hasArgument=True,
                desc="--splash IMAGE_FILE: "
                     "(EXPERIMENTAL) Add an splash screen with the image IMAGE_FILE to the application. "
                     "The splash screen can show progress updates while unpacking."
            )

            self.debugOption = Option(
                name="debug",
                hasArgument=True,
                argumentChoices=[OPTION_BY_DEFAULT, "all", "imports", "bootloader", "noarchive"],
                desc="-d {all,imports,bootloader,noarchive}, --debug {all,imports,bootloader,noarchive}: "
                     "Provide assistance with debugging a frozen application. "
                     "This argument may be provided multiple times to select several of the following options. "
                     "- all: All three of the following options. "
                     "- imports: specify the -v option to the underlying Python interpreter, "
                     "causing it to print a message each time a module is initialized, showing the place (filename or "
                     "built-in module) from which it is loaded. "
                     "- bootloader: tell the bootloader to issue progress messages while initializing and starting "
                     "the bundled app. Used to diagnose problems with missing imports. "
                     "- noarchive: instead of storing all frozen Python source files as an archive inside the "
                     "resulting executable, store them as files in the resulting output directory. "
            )

            self.stripSymbolTable = Option(
                name="strip",
                hasArgument=False,
                desc="-s, --strip: "
                     "Apply a symbol-table strip to the executable and shared libs (not recommended for Windows)"
            )

            self.noConsoleWindow = Option(
                name="noconsole",
                hasArgument=False,
                desc="-w, --windowed, --noconsole: "
                     "Windows and Mac OS X: do not provide a console window for standard i/o."
                     " On Mac OS X this also triggers building an OS X .app bundle. "
                     "On Windows this option will be set if the first script is a ‘.pyw’ file."
                     " This option is ignored in *NIX systems."
            )

            self.icon = Option(
                name="icon",
                hasArgument=True,
                desc="--icon <FILE.ico or FILE.exe,ID or FILE.icns or 'NONE'>: "
                     "FILE.ico: apply that icon to a Windows executable. "
                     "FILE.exe,ID, extract the icon with ID from an exe. "
                     "FILE.icns: apply the icon to the .app bundle on Mac OS X. "
                     "Use 'NONE' to not apply any icon, thereby making the OS to show some default "
                     "(default: apply PyInstaller’s icon)"
            )

            self.runtimeTmpPath = Option(
                name="runtime-tmpdir",
                hasArgument=True,
                desc="--runtime-tmpdir PATH: "
                     "Where to extract libraries and support files in onefile-mode. If this option is given, "
                     "the bootloader will ignore any temp-folder location defined by the run-time OS."
                     " The _MEIxxxxxx-folder will be created here. "
                     "Please use this option only if you know what you are doing."
            )

            self.bootloaderIgnoreSignals = Option(
                name="bootloader-ignore-signals",
                hasArgument=False,
                desc="--bootloader-ignore-signals: "
                     "Tell the bootloader to ignore signals rather than forwarding them to the child process. "
                     "Useful in situations where e.g. a supervisor process signals both the bootloader "
                     "and child (e.g. via a process group) to avoid signalling the child twice."
            )

            self.disableWindowedTraceback = Option(
                name="disable-windowed-traceback",
                hasArgument=False,
                desc="--disable-windowed-traceback: "
                     "Disable traceback dump of unhandled exception in windowed (noconsole) mode"
                     " (Windows and macOS only), and instead display a message that this feature is disabled."
            )

    class HookOptions(Options):
        def __init__(self):
            self.additionalHooksDir = MultipleOption(
                name="additional-hooks-dir",
                desc="--additional-hooks-dir HOOKSPATH: "
                     "An additional path to search for hooks. "
            )

            self.runtimeHooks = MultipleOption(
                name="runtime-hook",
                desc="--runtime-hook RUNTIME_HOOKS: "
                     "Path to a custom runtime hook file. "
                     "A runtime hook is code that is bundled with the executable and is executed before any other code"
                     " or module to set up special features of the runtime environment."
            )

    class UPXOptions(Options):
        def __init__(self):
            self.noUPX = Option(
                name="noupx",
                hasArgument=False,
                desc="--noupx: "
                     "Do not use UPX even if it is available (works differently between Windows and *nix)"
            )
            self.upxPath = Option(
                name="upx-dir",
                hasArgument=True,
                desc="--upx-dir UPX_DIR: "
                     "Path to UPX utility (default: search the execution path)"
            )
            self.excludeFiles = MultipleOption(
                name="upx-exclude",
                desc="--upx-exclude FILE:"
                     "Prevent a binary from being compressed when using upx. "
                     "This is typically used if upx corrupts certain binaries during compression. "
                     "FILE is the filename of the binary without path."
            )

    class WindowsOptions(Options):
        def __init__(self):
            self.versionFile = Option(
                name="version-file",
                hasArgument=True,
                desc="--version-file FILE: "
                     "add a version resource from FILE to the exe."
            )
            self.manifestFile = Option(
                name="manifest",
                hasArgument=True,
                desc="-m <FILE or XML>, --manifest <FILE or XML>: "
                     "add manifest FILE or XML to the exe."
            )
            self.resource = Option(
                name="resource",
                hasArgument=True,
                desc="-r RESOURCE, --resource RESOURCE: "
                     "Add or update a resource to a Windows executable. "
                     "The RESOURCE is one to four items, FILE[,TYPE[,NAME[,LANGUAGE]]]. "
                     "FILE can be a data file or an exe/dll. "
                     "For data files, at least TYPE and NAME must be specified. LANGUAGE defaults to 0 or may be "
                     "specified as wildcard * to update all resources of the given TYPE and NAME. For exe/dll files, "
                     "all resources from FILE will be added/updated to the final executable if TYPE, "
                     "NAME and LANGUAGE are omitted or specified as wildcard * "
            )
            self.uacAdmin = Option(
                name="uac-admin",
                hasArgument=False,
                desc="--uac-admin: "
                     "Using this option creates a Manifest which will request elevation upon application restart."
            )
            self.uacUIAccess = Option(
                name="uac-uiaccess",
                hasArgument=False,
                desc="--uac-uiaccess: "
                     "Using this option allows an elevated application to work with Remote Desktop."
            )
            self.privateAssemblies = Option(
                name="win-private-assemblies",
                hasArgument=False,
                desc="--win-private-assemblies: "
                     "Any Shared Assemblies bundled into the application will be changed into Private Assemblies. "
                     "This means the exact versions of these assemblies will always be used, and any newer versions "
                     "installed on user machines at the system level will be ignored."
            )
            self.noPreferRedirects = Option(
                name="win-no-prefer-redirects",
                hasArgument=False,
                desc="--win-no-prefer-redirects: "
                     "While searching for Shared or Private Assemblies to bundle into the application, "
                     "PyInstaller will prefer not to follow policies that redirect to newer versions, and will try to "
                     "bundle the exact versions of the assembly. "
            )

    class MacOSOptions(Options):
        def __init__(self):
            self.bundleIdentifier = Option(
                name="osx-bundle-identifier",
                hasArgument=True,
                desc="--osx-bundle-identifier BUNDLE_IDENTIFIER: "
                     "Mac OS X .app bundle identifier is used as the default unique program name for code signing "
                     "purposes. The usual form is a hierarchical name in reverse DNS notation. For example: "
                     "com.mycompany.department.appname (default: first script’s basename) "
            )

            self.targetArchitecture = Option(
                name="target-arch",
                hasArgument=True,
                argumentChoices=["x86_64", "arm64", "universal2"],
                desc="--target-architecture ARCH, --target-arch ARCH: "
                     "Target architecture (macOS only; valid values: x86_64, arm64, universal2). Enables switching "
                     "between universal2 and single-arch version of frozen application (provided python installation "
                     "supports the target architecture). If not target architecture is not specified, the current "
                     "running architecture is targeted. "
            )

            self.codesignIdentity = Option(
                name="codesign-identity",
                hasArgument=True,
                desc="--codesign-identity IDENTITY: "
                     "Code signing identity (macOS only). Use the provided identity to sign collected binaries and "
                     "generated executable. If signing identity is not provided, ad- hoc signing is performed instead. "
            )

            self.entitlementsFile = Option(
                name="entitlements-file",
                hasArgument=True,
                desc="--osx-entitlements-file FILENAME: "
                     "Entitlements file to use when code-signing the collected binaries (macOS only)."
            )

    def toJSON(self, setOptionsOnly=True):
        excludes = []
        serialized = {
            "pyinstaller": self.pyinstaller,
            "name": self.name,
            "author": self.author,
            "version": self.version,
            "description": self.description,
            "scripts": self.scripts,
            "options": {
            }
        }

        commonOptions = self.commonOptions.getOptionsWithName(setOptionsOnly)
        self.serializeOptions(serialized["options"], commonOptions, excludes)

        upxOptions = self.upxOptions.getOptionsWithName(setOptionsOnly)
        serialized["options"]["upx"] = {}
        self.serializeOptions(serialized["options"]["upx"], upxOptions, excludes)

        hookOptions = self.hookOptions.getOptionsWithName(setOptionsOnly)
        serialized["options"]["hooks"] = {}
        self.serializeOptions(serialized["options"]["hooks"], hookOptions, excludes)

        windowsOptions = self.windowsOptions.getOptionsWithName(setOptionsOnly)
        serialized["options"]["windows"] = {}
        self.serializeOptions(serialized["options"]["windows"], windowsOptions, excludes)

        macosOptions = self.macosOptions.getOptionsWithName(setOptionsOnly)
        serialized["options"]["macos"] = {}
        self.serializeOptions(serialized["options"]["macos"], macosOptions, excludes)

        return json.dumps(serialized, indent=4)

    @classmethod
    def serializeOptions(cls, serialized, options, excludes=None):
        if excludes is None:
            excludes = []
        for name, opt in options:
            if name in excludes:
                continue
            if opt.hasArgument:
                if opt.isSet:
                    val = opt.argument
                else:
                    val = OPTION_BY_DEFAULT
                serialized[name] = val
            else:
                if opt.isSet:
                    serialized[name] = opt.isSet
                else:
                    serialized[name] = OPTION_BY_DEFAULT

    @classmethod
    def deserializeOptions(cls, src, target):
        for k in src.keys():
            if k == "logLevel":
                i = 1
            val = src[k]
            if val == OPTION_BY_DEFAULT:
                continue
            if k.startswith("_") or isinstance(val, dict) or not hasattr(target, k):
                continue
            opt = getattr(target, k)
            if not isinstance(opt, Option):
                continue

            if isinstance(opt, MultipleOption):
                if isinstance(val, list) and len(val) > 0:
                    for arg in val:
                        opt.add(arg)
            else:
                if opt.hasArgument:
                    opt.argument = val
                else:
                    if val is True:
                        opt.set()
                    else:
                        opt.unset()

    @staticmethod
    def _get(d, key, defaultValue):
        if key in d:
            return d[key]
        return defaultValue

    @classmethod
    def load(cls, path, ignoreErrors=True):
        target = cls()
        with open(path) as file:
            jsonData = json.load(file)
        if not isinstance(jsonData, dict):
            if ignoreErrors:
                return target
            else:
                raise RuntimeError("bad file format")
        target.pyinstaller = cls._get(jsonData, "pyinstaller", target.pyinstaller)
        target.name = cls._get(jsonData, "name", target.name)
        target.author = cls._get(jsonData, "author", target.author)
        target.version = cls._get(jsonData, "version", target.version)
        target.description = cls._get(jsonData, "description", target.description)
        target.scripts = cls._get(jsonData, "scripts", target.scripts)
        try:
            if "options" in jsonData:
                options = jsonData["options"]
                cls.deserializeOptions(options, target.commonOptions)
                if "hooks" in options:
                    cls.deserializeOptions(options["hooks"], target.hookOptions)
                if "upx" in options:
                    cls.deserializeOptions(options["upx"], target.upxOptions)
                if "windows" in options:
                    cls.deserializeOptions(options["windows"], target.windowsOptions)
                if "macos" in options:
                    cls.deserializeOptions(options["macos"], target.macosOptions)
        except Exception as e:
            if ignoreErrors:
                return target
            else:
                raise e
        else:
            return target

    def toPakCommand(self, dependOnPlatform=True):
        # if len(self.scripts) <= 0:
        #     raise RuntimeError("no scripts to pack")
        # if self.pyinstaller is None or self.pyinstaller == "":
        #     raise RuntimeError("pyinstaller is none")

        argList = []
        argList.extend(self.commonOptions.toCommandArgList())
        argList.extend(self.hookOptions.toCommandArgList())
        argList.extend(self.upxOptions.toCommandArgList())
        if dependOnPlatform:
            if platform.system().lower() == "windows":
                argList.extend(self.windowsOptions.toCommandArgList())
            if platform.system().lower() == "darwin":
                argList.extend(self.macosOptions.toCommandArgList())
        cmd = f"{self.pyinstaller} {' '.join(argList)} {' '.join(self.scripts)}"
        return cmd

    def save(self, path, setOptionsOnly=True):
        dirs = dirname(path)
        makedirs(dirs, exist_ok=True)
        with open(path, "wb") as file:
            file.write(self.toJSON(setOptionsOnly).encode("utf-8"))

# # config = PackageConfigs()
# # config.scripts.append("main.py")
# # config.commonOptions.noConfirm.set()
# # config.commonOptions.cleanBeforePack.set()
# # config.commonOptions.extraBinaryPaths.add("./data/a.bin")
# # config.commonOptions.extraBinaryPaths.add("./data/b.bin")
# # config.commonOptions.hiddenImports.set("cython")
# # config.commonOptions.noConsoleWindow.set()
# # config.windowsOptions.manifestFile.set("./manifest.xml")
# # config.windowsOptions.uacAdmin.set()
# # config.save("./package.json", False)
#
# config2 = PackageConfigs.load("./package.json")
# config2.save("./package2.json")
