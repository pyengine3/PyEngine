import os

__all__ = ["Lang"]


class Lang:
    def __init__(self, file: str):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.dic = {}
        self.__file = file
        if os.path.exists(file):
            with open(file) as f:
                for i in f.readlines():
                    if len(i.split(": ")) == 2:
                        self.dic[i.split(": ")[0]] = i.split(": ")[1].replace("\n", "")
                    else:
                        raise ValueError("Unknown format of lang : '"+i+"'")
        else:
            raise ValueError("File don't exist.")

    def get_translate(self, key: str, default: str) -> str:
        try:
            return self.dic[key]
        except KeyError:
            return default
