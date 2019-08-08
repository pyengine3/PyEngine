import json
import os

from pyengine.Utils.Logger import loggers

__all__ = ["Config"]


class Config:
    def __init__(self, file: str):
        self.dic = {}
        self.created = False
        self.file = file

    def get(self, key):
        try:
            return self.dic[key]
        except KeyError:
            loggers.to_all("warning", "Key '"+key+"' doesn't exist in Config File")

    def set(self, key, val):
        self.dic[key] = val

    def save(self):
        with open(self.file, "w") as f:
            f.write(json.dumps(self.dic, indent=4))
        loggers.to_all("info", "Config File saved")

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, val):
        self.__file = val
        if os.path.exists(val):
            self.created = True
            with open(val, "r") as f:
                self.dic = json.load(f)
        else:
            self.created = False

    def create(self, dic):
        if self.created:
            loggers.to_all("warning", "Config File already exist but recreated")
        else:
            loggers.to_all("info", "Config File created")
        with open(self.file, "w") as f:
            f.write(json.dumps(dic, indent=4))
        self.dic = dic

