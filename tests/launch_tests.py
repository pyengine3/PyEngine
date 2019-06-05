import os

text = ""
for i in os.listdir("."):
    if i != "launch_tests.py" and i.endswith(".py"):
        text += i + " "
os.system("python -m unittest -v "+text[:-1])

