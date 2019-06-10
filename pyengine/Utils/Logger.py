import logging
from logging.handlers import RotatingFileHandler
import os

__all__ = ["loggers"]


class Logger(logging.Logger):
    def __init__(self, name, file=None, stream=False):
        super(Logger, self).__init__(name)

        self.file_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s',
                                                datefmt='%d/%m/%Y %H:%M:%S')

        self.stream_formatter = logging.Formatter('FROM '+name+' - %(asctime)s - %(levelname)s: %(message)s',
                                                  datefmt='%d/%m/%Y %H:%M:%S')

        if file is not None:
            self.file_handler = RotatingFileHandler(file, "a", 1000000, 1)
            self.file_handler.setFormatter(self.file_formatter)
            self.addHandler(self.file_handler)
        else:
            self.file_handler = None

        if stream:
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setFormatter(self.stream_formatter)
            self.addHandler(self.stream_handler)
        else:
            self.stream_handler = None

    def setLevel(self, level):
        super(Logger, self).setLevel(level)
        if self.stream_handler:
            self.stream_handler.setLevel(level)
        if self.file_handler:
            self.file_handler.setLevel(level)


class Loggers:
    def __init__(self):
        if not os.path.exists("logs"):
            os.mkdir("logs")

        self.loggers = {
            "PyEngine": Logger("PyEngine", "logs/pyengine.log", True)
        }

    def create_logger(self, name, file=None, stream=False):
        self.loggers[name] = Logger(name, file, stream)
        return self.loggers[name]

    def get_logger(self, name):
        try:
            return self.loggers[name]
        except KeyError:
            raise KeyError("Logger '"+name+"' doesn't exist")


loggers = Loggers()

