# -*- coding:utf-8 -*-

OPTION_BY_DEFAULT = "BY-DEFAULT"


class ArgumentType(object):
    ANY = "any",
    STRING = "string",
    INT = "int",
    BOOL = "bool"


class ArgumentValidators(object):
    validators = {
        ArgumentType.ANY: lambda v: True,
        ArgumentType.STRING: lambda v: isinstance(v, str),
        ArgumentType.INT: lambda v: isinstance(v, int),
        ArgumentType.BOOL: lambda v: isinstance(v, bool)
    }

    @classmethod
    def registerValidator(cls, argumentType, validator):
        cls.validators[argumentType] = validator

    @classmethod
    def getValidator(cls, argumentType):
        return cls.validators[argumentType]


class OptionType(object):
    SHORT_OPT = 1
    LONG_OPT = 0

    @classmethod
    def prefix(cls, optionType):
        if optionType == cls.LONG_OPT:
            return "--"
        else:
            return "-"


class OptionStatus(int):
    SET = 0
    UNSET = 1


class Option(object):
    def __init__(self,
                 name,
                 optionType=OptionType.LONG_OPT,
                 hasArgument=False,
                 argumentType=ArgumentType.ANY,
                 argumentChoices=None,
                 connector="=",
                 desc=""):
        self._name = name
        self._optionStatus = OptionStatus.UNSET
        self._type = optionType
        self._hasArgument = hasArgument
        self._argumentType = argumentType
        self._argumentChoices = argumentChoices
        self._argument = ""
        self._connector = connector
        self._desc = desc

    @staticmethod
    def _makeOptionString(optionName, optionType, argument, connector="="):
        if argument is None:
            return f"{OptionType.prefix(optionType)}{optionName}"
        else:
            return f"{OptionType.prefix(optionType)}{optionName}{connector}{argument}"

    def isOptionSet(self):
        return self._optionStatus == OptionStatus.SET

    @property
    def connector(self):
        return self._connector

    @connector.setter
    def connector(self, c):
        self._connector = c

    def set(self, arg=None):
        if not self._hasArgument:
            self._optionStatus = OptionStatus.SET
            return
        self.argument = arg

    def unset(self):
        self._optionStatus = OptionStatus.UNSET
        self._argument = None

    @property
    def name(self):
        return self._name

    @property
    def optionType(self):
        return self._type

    @property
    def isSet(self):
        return self.isOptionSet()

    @property
    def hasArgument(self):
        return self._hasArgument

    @property
    def argumentType(self):
        return self._argumentType

    @property
    def argumentChoices(self):
        return self._argumentChoices

    @argumentChoices.setter
    def argumentChoices(self, choices):
        self._argumentChoices = choices

    @property
    def argument(self):
        return self._argument

    @argument.setter
    def argument(self, arg):
        if not self._hasArgument:
            raise ValueError("this option do not have argument")

        # 特殊值处理：我们定义，如果赋予argument的值为：None，""(空串)，或者是OPTION_BY_DEFAULT定义的值
        # 则代表将这个option设置为UNSET状态
        if arg is None or arg == "" or arg == OPTION_BY_DEFAULT:
            self.unset()
            return

        # 验证
        if self._argumentChoices is not None:
            if arg not in self._argumentChoices:
                raise ValueError("argument is not allowed")
            else:
                self._argument = arg
                self._optionStatus = OptionStatus.SET
        else:
            if ArgumentValidators.getValidator(self._argumentType)(arg):
                self._argument = arg
                self._optionStatus = OptionStatus.SET
            else:
                self._argument = None
                self._optionStatus = OptionStatus.UNSET
                raise ValueError("argument is not valid")

    @property
    def description(self):
        return self._desc

    @description.setter
    def description(self, desc):
        self._desc = desc

    def stringify(self):
        if self._optionStatus == OptionStatus.UNSET:
            return ""
        else:
            if not self._hasArgument:
                return self._makeOptionString(self._name, self._type, None)
            else:
                return self._makeOptionString(self._name, self._type, self._argument, self._connector)


class MultipleOption(Option):
    def __init__(self, name, optionType=OptionType.LONG_OPT, argumentType=ArgumentType.ANY, argumentChoices=None,
                 connector="=", desc=None):
        super().__init__(name, optionType, True, argumentType, argumentChoices, connector, desc)
        self._argument = []

    @property
    def argument(self):
        return super().argument

    def set(self, *args):
        if len(args) <= 0:
            raise RuntimeError("provide one or more args")
        for arg in args:
            self.add(arg)

    def unset(self):
        self._optionStatus = OptionStatus.UNSET
        self._argument.clear()

    def add(self, arg):
        if arg in self._argument:
            return
        # 忽略特殊值
        if arg is None or arg == "" or arg == OPTION_BY_DEFAULT:
            return
            # 验证
        if self._argumentChoices is not None:
            if arg not in self._argumentChoices:
                raise ValueError("argument is not allowed")
            else:
                self._argument.append(arg)
                self._optionStatus = OptionStatus.SET
        else:
            if ArgumentValidators.getValidator(self._argumentType)(arg):
                self._argument.append(arg)
                self._optionStatus = OptionStatus.SET
            else:
                raise ValueError("argument is not valid")

    def remove(self, arg):
        if arg in self._argument:
            self._argument.remove(arg)
        if len(self._argument) <= 0:
            self.unset()

    def addAll(self, *args):
        for arg in args:
            self.add(arg)

    def stringify(self):
        if not self.isOptionSet():
            return ""
        if len(self._argument) <= 0:
            return ""
        return " ".join(
            [self._makeOptionString(self._name, self._type, arg, self._connector) for arg in self._argument])


def toMetadata(opt):
    metadata = {
        "name": opt.name,
        "type": opt.optionType,
        "description": opt.description,
        "connector": opt.connector,
    }
    if opt.hasArgument:
        if isinstance(opt.argument, list):
            metadata["argument"] = []
        else:
            metadata["argument"] = None
        metadata["argumentType"] = opt.argumentType
        metadata["argumentChoices"] = opt.argumentChoices
    return metadata


def fromMetadata(metadata):
    if "argument" not in metadata:
        opt = Option(
            name=metadata["name"],
            optionType=metadata["type"],
            hasArgument=False,
        )
    else:
        argument = metadata["argument"]
        if isinstance(argument, list):
            opt = MultipleOption(
                name=metadata["name"],
                optionType=metadata["type"],
                argumentType=metadata["argumentType"],
            )
        else:
            opt = Option(
                name=metadata["name"],
                optionType=metadata["type"],
                hasArgument=True,
                argumentType=metadata["argumentType"]
            )
        if "argumentChoices" in metadata:
            opt.argumentChoices = metadata["argumentChoices"]
        else:
            opt.argumentChoices = None
    if "connector" in metadata:
        opt.connector = metadata["connector"]
    if "description" in metadata:
        opt.description = metadata["description"]
    return opt

# o1 = Option("test1", hasArgument=True)
# o1.set(1)
# m1 = toMetadata(o1)
# print(m1)
#
# o2 = MultipleOption("test2")
# m2 = toMetadata(o2)
# print(m2)
# #
# o3 = Option("test3")
# m3 = toMetadata(o3)
# print(m3)
#
# a1 = fromMetadata(m1)
# a2 = fromMetadata(m2)
# a3 = fromMetadata(m3)
# print(a1, a1.argumentType, a1.hasArgument)
# print(a3, a3.argumentType, a3.hasArgument)
