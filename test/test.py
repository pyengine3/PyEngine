from pyengine import Window
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button
from pyengine.Utils import Colors, Vec2, Lang, Config
import os


def setlang(obj, button):
    if lang.file == "langs/fr.lang":
        lang.file = "langs/en.lang"
        conf.set("lang", "langs/en.lang")
    else:
        lang.file = "langs/fr.lang"
        conf.set("lang", "langs/fr.lang")
    conf.save()
    hello.text = lang.get_translate("label", "Hello !")
    b.label.text = lang.get_translate("button", "English")


fenetre = Window(500, 300, Colors.WHITE.value)

uisystem = fenetre.world.get_system(UISystem)

if os.path.exists("config.json"):
    conf = Config("config.json")
else:
    conf = Config("config.json")
    conf.create({
        "lang": "langs/fr.lang"
    })
lang = Lang(conf.get("lang"))

hello = Label(Vec2(10, 10), lang.get_translate("label", "Hello !"), Colors.BLACK.value)
b = Button(Vec2(10, 100), lang.get_translate("button", "English"), setlang)

uisystem.add_widget(hello)
uisystem.add_widget(b)

fenetre.run()
