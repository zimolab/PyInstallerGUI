# -*- coding:utf-8 -*-

"""
在子线程里执行目录
"""
import threading


class ExecutingThread(threading.Thread):
    pass


class CommandExecutor(object):
    _process = None
    _isExecuting = False

    @classmethod
    def execute(cls, cmd, onOutputHandler, onErrorHandler, onStartHandler, onEndHandler):
        if cls._isExecuting:
            return False
