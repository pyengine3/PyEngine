import os

text = ""
for i in os.listdir("."):
    if i not in ["launch_tests.py", "launch_server_for_test.py"] and i.endswith(".py"):
        text += i + " "
os.system("python -m unittest -v "+text[:-1])

