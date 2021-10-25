# -*- coding:utf-8 -*-
from enum import Enum
from typing import Union

from PySide2.QtWidgets import QLineEdit, QCheckBox, \
    QRadioButton, QComboBox, QListWidget
from QBinder import Binder, constant

DEFAULT_VALUE_UNSET = "DEFAULT-UNSET"
constant.AUTO_DUMP = False


class OptionForm(str, Enum):
    LONG_OPTION = "--"
    SHORT_OPTION = "-"


class OptionConnector(str, Enum):
    SPACE = " "
    EQUAL = "="
    NONE = ""


class ArgumentInvalidError(Exception):
    def __init__(self, optionName, argument):
        super(ArgumentInvalidError, self).__init__(f"argument '{argument}' of option '{optionName}' is invalid")


class BaseOption(object):
    def __init__(self, name, form, description):
        self._name = name
        self.form = form
        self.description = description

    def toString(self):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

    @property
    def isSet(self):
        raise NotImplementedError

    @property
    def argument(self):
        raise NotImplementedError

    def bind(self, widget):
        raise NotImplementedError

    def unset(self):
        raise NotImplementedError

    def set(self, *args, **kwargs):
        raise NotImplementedError


class BindingOption(BaseOption):
    def __init__(self, name, default="", form=OptionForm.LONG_OPTION, choices=None, connector=OptionConnector.EQUAL,
                 description="", validator=None, ignoreValidationError=True, wrapArgument=False):
        super().__init__(name, form, description)
        self._state = Binder()
        self._state.argument = ""
        self._ignoreValidationError = ignoreValidationError
        self._valuesForUnset = [None, "", DEFAULT_VALUE_UNSET]
        self.choices = choices
        self.connector = connector
        self.validator = validator
        self.wrapArgument = wrapArgument

        self.argument = default

    def unset(self):
        self.argument = self._valuesForUnset[0]

    def set(self, arg):
        self.argument = arg

    @property
    def name(self):
        return self._name

    @property
    def argument(self):
        return self._state.argument

    @argument.setter
    def argument(self, val):
        if val in self._valuesForUnset:
            self._state.argument = DEFAULT_VALUE_UNSET
            return
        # choices的校验优先级高于validator
        if self.choices is not None:
            if val not in self.choices:
                if self._ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    self._state.argument = DEFAULT_VALUE_UNSET
            else:
                self._state.argument = val
            return

        # 如果设置了validator，则用其进行校验
        if self.validator is not None:
            if self.validator(val):
                self._state.argument = val
            else:
                if self._ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    self._state.argument = DEFAULT_VALUE_UNSET
        else:
            self._state.argument = val

    @property
    def isSet(self):
        return not (self.argument in self._valuesForUnset)

    def toString(self):
        if self.isSet:
            if not self.wrapArgument:
                return f'{self.form}{self.name}{self.connector}{self.argument}'
            else:
                return f'{self.form}{self.name}{self.connector}"{self.argument}"'
        return ""

    def bind(self, widget):
        if isinstance(widget, QLineEdit):
            widget.setText(lambda: self.argument * 1)
            widget.textChanged.connect(self.set)
        elif isinstance(widget, QComboBox):
            if isinstance(self.choices, list) and len(self.choices) > 0:
                widget.addItems(self.choices)
            widget.setCurrentText(lambda: self.argument * 1)
            widget.currentTextChanged.connect(self.set)
        else:
            raise ValueError("unsupported widget type")
        self.argument = self.argument


class BindingFlag(BaseOption):
    def __init__(self, name, default=None, form=OptionForm.LONG_OPTION, description=""):
        super().__init__(name, form, description)
        self._state = Binder()
        self._state.argument = False
        self._valuesForSet = [True, "true", "1", 1, "on"]

        self.set(default)

    def set(self, val=True):
        if val in self._valuesForSet:
            val = True
        else:
            val = False
        self._state.argument = val

    def unset(self):
        self.set(False)

    @property
    def isSet(self):
        return self._state.argument in self._valuesForSet

    @property
    def name(self):
        return self._name

    @property
    def argument(self):
        return self.isSet

    def toString(self):
        if self.isSet:
            return f"{self.form}{self.name}"
        return ""

    def bind(self, widget: Union[QCheckBox, QRadioButton]):
        widget.setChecked(lambda: self._state.argument * 1)
        widget.clicked.connect(lambda: self.set(widget.isChecked()))
        self._state.argument = self._state.argument


class BindingMultipleOption(BaseOption):
    def __init__(self, name, default=None, form=OptionForm.LONG_OPTION, choices=None, connector=OptionConnector.EQUAL,
                 description="", validator=None, wrapArgument=False):
        super().__init__(name, form, description)

        if isinstance(default, list) or isinstance(default, tuple):
            default = [val for val in default]
        else:
            default = []

        self._state = Binder()
        self._state.argument = []
        self._valuesForUnset = [None, "", DEFAULT_VALUE_UNSET]
        self.choices = choices
        self.connector = connector
        self.validator = validator
        self.wrapArgument = wrapArgument

        self.addAll(True, *default)

    def unset(self):
        self.clear()

    @property
    def argument(self):
        return self._state.argument

    @property
    def isSet(self):
        if len(self._state.argument) == 0:
            return False
        return True

    def add(self, val, ignoreValidationError=True):
        # 防止元素重复
        if val in self._state.argument:
            return False

        if val in self._valuesForUnset:
            return False

        # choices的校验优先级高于validator
        if self.choices is not None:
            if val not in self.choices:
                if ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    return False
            else:
                self._state.argument.append(val)
                return True

        # 如果设置了validator，则用其进行校验
        if self.validator is not None:
            if self.validator(val):
                self._state.argument.append(val)
                return True
            else:
                if ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    return False
        else:
            self._state.argument.append(val)
            return True

    def remove(self, *values):
        for val in values:
            if val in self._state.argument:
                self._state.argument.remove(val)

    def removeAt(self, index):
        if index < 0 or index >= len(self._state.argument):
            return False
        self._state.argument.pop(index)
        return True

    def set(self, index, val, ignoreValidationError=True):
        # 防止越界访问
        if index < 0 or index >= len(self._state.argument):
            return False
        # 防止元素重复
        if val in self._state.argument:
            return False

        if val in self._valuesForUnset:
            return False

        # choices的校验优先级高于validator
        if self.choices is not None:
            if val not in self.choices:
                if ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    return False
            else:
                self._state.argument[index] = val
                return True

        # 如果设置了validator，则用其进行校验
        if self.validator is not None:
            if self.validator(val):
                self._state.argument[index] = val
                return True
            else:
                if ignoreValidationError:
                    raise ArgumentInvalidError(self._name, val)
                else:
                    return False
        else:
            self._state.argument[index] = val
            return True

    def indexOf(self, val):
        if self.isSet:
            return self.argument.index(val)
        return -1

    def clear(self):
        self._state.argument.clear()
        self._state.argument = []

    def replaceWith(self, values, ignoreValidationError=True):
        self.clear()
        for val in values:
            self.add(val, ignoreValidationError)

    def addAll(self, ignoreValidationError, *values):
        for val in values:
            self.add(val, ignoreValidationError)

    def _makeArgumentString(self, arg):
        if not self.wrapArgument:
            return f'{self.form}{self.name}{self.connector}{arg}'
        else:
            return f'{self.form}{self.name}{self.connector}"{arg}"'

    def toString(self):
        if self.isSet:
            return " ".join([self._makeArgumentString(arg) for arg in self._state.argument])
        return ""

    def bind(self, widget: Union[QListWidget]):
        def onUpdateItems():
            widget.clear()
            return self._state.argument

        widget.addItems(onUpdateItems)

        self._state.argument = self._state.argument


class Options(object):
    def toStringList(self):
        optionsSet = self.getOptions(filterUnsetOptions=True)
        return [o.toString() for o in optionsSet]

    def toString(self):
        return " ".join(self.toStringList())

    def getOptions(self, filterUnsetOptions=False, withNames=False):
        options = []
        for opt in dir(self):
            val = getattr(self, opt)
            if isinstance(val, BaseOption):
                if filterUnsetOptions:
                    if val.isSet:
                        if withNames:
                            options.append((opt, val))
                        else:
                            options.append(val)
                else:
                    if withNames:
                        options.append((opt, val))
                    else:
                        options.append(val)
        return options

# Simple test
# from PySide2.QtWidgets import QApplication, QFrame, QMainWindow, QVBoxLayout, QPushButton, QInputDialog, QMessageBox
# import sys
# app = QApplication(sys.argv)
#
# window = QMainWindow()
# panel = QFrame()
# layout = QVBoxLayout()
# edit = QLineEdit()
# cb = QCheckBox()
# cb.setText("flag")
# rb = QRadioButton()
# rb.setText("flag")
# combo = QComboBox()
# lw = QListWidget()
#
# opt = BindingOption("text")
# opt.validator = None
# opt.bind(edit)
# opt2 = BindingOption("text2")
# opt2.choices = ["1", "2", "3", DEFAULT_VALUE_UNSET]
# combo.addItems(opt2.choices)
# opt2.bind(combo)
# flag = BindingFlag("flag", default=False)
# opt3 = BindingMultipleOption("text3", default=["1", "2", "3"])
# opt3.bind(lw)
#
#
# def onGen():
#     print("Opt single argument:", opt.argument, opt.toString(), opt.isSet)
#     print("flag:", flag.toString())
#     print("combo:", opt2.toString())
#     print("list:", opt3.toString())
#
#
# genBtn = QPushButton(text="Gen")
# genBtn.clicked.connect(onGen)
#
#
# def onAdd():
#     text = QInputDialog.getText(window, "Add Item", "item to add:", QLineEdit.Normal, "item")[0]
#     r = opt3.add(text)
#     if r:
#         QMessageBox.information(window, "Message", "Ok")
#     else:
#         QMessageBox.information(window, "Message", "Failed")
#
#
# addBtn = QPushButton(text="Add")
# addBtn.clicked.connect(onAdd)
#
#
# def onRemoveItem():
#     selected = [w.text() for w in lw.selectedItems()]
#     for i in selected:
#         opt3.remove(i)
#
#
# removeBtn = QPushButton(text="Remove")
# removeBtn.clicked.connect(onRemoveItem)
#
# flag.bind(cb)
# flag.bind(rb)
# layout.addWidget(edit)
# layout.addWidget(cb)
# layout.addWidget(rb)
# layout.addWidget(combo)
# layout.addWidget(lw)
# layout.addWidget(addBtn)
# layout.addWidget(removeBtn)
# layout.addWidget(genBtn)
#
# panel.setLayout(layout)
# window.setCentralWidget(panel)
# window.show()
#
# sys.exit(app.exec_())
