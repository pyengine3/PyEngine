from pygame import locals as const

from pyengine.Utils.Color import Colors
from pyengine.Utils.Font import Font
from pyengine.Utils.Logger import loggers
from pyengine.Utils.Vec2 import Vec2
from pyengine.Widgets.Entry import Entry
from pyengine.Widgets.Label import Label

__all__ = ["Console"]


def print_command(console, window, args):
    console.reply(" ".join(args))


def debug_command(console, window, args):
    if window.debug:
        console.reply("Debug desactivated")
    else:
        console.reply("Debug activated")
    window.debug = not window.debug


class Console(Entry):
    def __init__(self, window, pos=Vec2(), width=600):
        pos = Vec2(pos.x, pos.y + 20)
        super(Console, self).__init__(pos, width)
        self.window = window
        self.commands = {
            "print": print_command, "debug": debug_command
        }
        self.lastscommands = []
        self.current_command = len(self.lastscommands)
        self.font = Font(size=18)

        self.retour = Label(Vec2(pos.x, pos.y - 21), ">", Colors.BLACK.value, Font(size=18), Colors.WHITE.value)
        self.retour.parent = self

    def reply(self, texte=""):
        self.retour.text = "> "+texte

    def hide(self):
        super(Console, self).hide()
        self.retour.hide()

    def show(self):
        super(Console, self).show()
        self.retour.show()

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        system.add_widget(self.retour)

    def add_command(self, name, function):
        if name in self.commands:
            loggers.get_logger("PyEngine").warning("Command overrided : "+name)
        self.commands[name] = function

    def delete_command(self, name):
        try:
            del self.commands[name]
        except KeyError:
            raise ValueError("Command '"+name+"' doesn't exist")

    def keypress(self, evt):
        temp = self.text
        super(Console, self).keypress(evt)
        if temp == self.text:
            if evt.key == const.K_RETURN:
                self.lastscommands.append(self.text)
                self.current_command = len(self.lastscommands)
                self.execute_command(self.text)
                self.text = ""
            elif evt.key == const.K_UP:
                if self.current_command > 0:
                    self.current_command -= 1
                    self.text = self.lastscommands[self.current_command]
            elif evt.key == const.K_DOWN:
                if self.current_command < len(self.lastscommands) - 1:
                    self.current_command += 1
                    self.text = self.lastscommands[self.current_command]
                elif self.current_command < len(self.lastscommands):
                    self.text = ""
                    self.current_command += 1

    def execute_command(self, command):
        if len(command.split(" ")) > 1:
            args = command.split(" ")[1:]
        else:
            args = []
        command = command.split(" ")[0]
        if command in self.commands:
            self.commands[command](self, self.window, args)
        else:
            loggers.get_logger("PyEngine").warning("Unknown command : " + command)
