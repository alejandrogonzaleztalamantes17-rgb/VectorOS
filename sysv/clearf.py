import os

def clears():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")