from PySide2.QtCore import QObject


class AppMeta(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.appName = self.tr(u"PyInstallerGUI")
        self.appVersion = self.tr(u"0.0.2")
        self.appLicense = self.tr(u"GPL V3")
        self.appCopyright = self.tr(u"")
        self.appDescription = self.tr(u"A GUI wrapper for pyinstaller. Helps you get rid of the long command line.")
        self.appHomepage = self.tr(u"https://github.com/zimolab/PyInstallerGUI")
        self.author = self.tr(u"zimolab")
        self.contact = self.tr(u"zimolab@aliyun.com")

        self.description = f'## {self.appName}\n' \
                           f'##### {self.tr(u"version:")} {self.appVersion}\n' \
                           f'###### {self.tr(u"license:")} {self.appLicense}\n' \
                           f'###### {self.tr(u"homepage:")} {self.appHomepage}\n ' \
                           f'###### {self.tr(u"author:  ")} [{self.author}]({self.contact}) \n' \
                           f'###### \n' \
                           f'###### {self.appDescription}'

    def describeMe(self):
        return self.description
