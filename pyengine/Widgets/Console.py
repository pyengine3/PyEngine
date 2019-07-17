from pyengine.Widgets import Entry, Label
from pyengine.Utils import loggers, Font, Vec2, Colors

from pygame import locals as const

__all__ = ["Console"]


def print_command(console, window, args):
    console.reply(" ".join(args))


class Console(Entry):
    def __init__(self, window, pos=Vec2(0, 20), width=600):
        super(Console, self).__init__(pos, width)
        self.window = window
        self.commands = {
            "print": print_command
        }
        self.lastscommands = []
        self.current_command = len(self.lastscommands)
        self.label.font = Font(size=16)

        self.retour = Label(Vec2(pos.x, pos.y - 20), ">", Colors.BLACK.value, Font(size=16), Colors.WHITE.value)
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
        system.add_widget(self.label)
        system.add_widget(self.retour)

    def add_command(self, name, function):
        try:
            self.commands[name] = function
            loggers.get_logger("PyEngine").warning("Command overrided : "+name)
        except KeyError:
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
