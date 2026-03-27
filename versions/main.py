import time
import datetime
import xml.etree.ElementTree as XMLSYS
import os
import random
import platform
import sys
from etc.printxf import printx
from cmds.timef import times
from cmds.quitf import quits
from sysv.clearf import clears
from styles.colorsst import colores
from sysv.oopsf import oops
from cmds.timelivef import timelives

entmdf = "V\\>"
dirs = []
files = ["whilef.sys"]

count_drm = 0
count = 0

tree = XMLSYS.parse("config.xml")
root = tree.getroot()

with open("whilef.txt", "w") as f:
    f.write("sys: ")
    f.write("whilef =True")
    f.write("while whilef:")
    f.write("    pass")
    f.write("")
    f.write("Segurity whilef.sys")

PATH = os.path.join(os.getcwd(), "HOME_vos")

def banner():
    print(r"""
__     __        _              ___  ____
\ \   / /__  ___| |_ ___  _ __ / _ \/ ___|
 \ \ / / _ \/ __| __/ _ \| '__| | | \___ \
  \ V /  __/ (__| || (_) | |  | |_| |___) |
   \_/ \___|\___|\__\___/|_|   \___/|____
""")
banner()

whilef = True
while whilef:
    ent = input(entmdf).strip()

    if ent == "time":
        times()
    elif ent == "quit":
        quits()
    elif ent.startswith("echo "):
        echoc = ent[5:]
        if echoc == "$VERSION":
            printx("1.0 (VectorOS 1)")
        else:
            printx(echoc)
    elif ent == "clear":
        clears()
    elif ent == "miau":
        printx("""/\\_/\\
( o.o )
> ^ <""")
    elif ent.startswith("mkdir "):
        mkdir = ent[6:]
        if mkdir in dirs:
            printx("The dir already exists")
        else:
            dirs.append(mkdir)
    elif ent == "dir":
        if len(dirs) == 0:
            printx("Not folders saved")
        else:
            for d in dirs:
                printx(colores["brg_yellow"] + "<DIR>    " + "\033[0m" + d)
    elif ent == "time -l":
        timelives()
    elif ent.startswith("cfle "):
        mkfile = ent[5:]
        files.append(mkfile)
    elif ent == "mf":
        if len(files) == 0:
            printx("Not files saved")
        else:
            for f in files:
                printx(colores["brg_blue"] + "<FLE>    " + "\033[0m" + f)
    elif ent.startswith("mksdir "):
        mkdirr = ent[len("mksdir "):].strip()

        FLL_PATH = os.path.join(PATH, mkdirr)
        try:
            os.makedirs(FLL_PATH, exist_ok=True)
            printx("ll")
        except Exception as e:
            printx("Error")
    elif ent == "sdir":
        for item in os.listdir(PATH):
            FLL_PATH = os.path.join(PATH, item)
            if os.path.isdir(FLL_PATH):
                printx(item)
    elif ent.startswith("rm "):
        rmfile = ent[3:]
        if rmfile == "whilef.sys":
            count_drm += 1
            printx("File protect by System")
            if count_drm == 3:
                oops()
                exit()
        else:
            if rmfile in files:
                files.remove(rmfile)
            else:
                printx("sys: vectoros: no such file or directory")
    elif ent == "csfle":
        count += 1
        if count == 1:
            printx("Coming Soon")
        if count == 2:
            printx("Don't you understand? Coming soon")
        if count == 3:
            printx("What? Are you deaf?")
        if count == 4:
            printx("I'll call Hey5")
        if count == 5:
            printx("Hey5:Don't understand that it will be released soon?")
        if count == 6:
            printx("Hey5:I'd better go by helicopter")
        if count == 7:
            printx("Where are you going Hey5?")
        if count == 8:
            printx("Hey5:I'm leaving, this person doesn't understand")
            count = 0
    elif ent == "about":
        printx(f"Name: {root.find('name').text}")
        printx(f"Version: {root.find('v').text}")
        printx(f"Created By: {root.find('crby').text}")
        printx(f"Made in: {root.find('mdin').text}")
        printx(f"Special Thanks ♡: {root.find('spth').text}, {root.find('spth2').text}, {root.find('spth3').text}")
    elif ent == "loa":
        printx(colores["brg_green"] + r"""
        -o          o-
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm:NMMMMMMN:mMMd`
      hMMMMMMMMMMMMMMMMMMh
  ..  yyyyyyyyyyyyyyyyyyyy  ..
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs""" + "\033[0m")
    elif ent == "i fell in the street":
        printx("""
 _     ___  _
| |   / _ \\| |
| |  | | | | |
| |__| |_| | |___
|_____\\___/|_____|""" + "\n")
    elif ent == "low":
        #the sims
        printx("\033[96m" + r"""
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@

        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@
        @@@@@@@@   @@@@@@@@""" + "\033[0m" + "\n")
    elif ent == "lol":
        printx("""
           .--.
          |o_o |
          |:_/ |
         //   \\ \\
        (|     | )
       /'\\_   _/`\\
       \\___)=(___/""" + "\n")
    elif ent == "lom":
        printx(r"""
           ,--./,-.
          / #      \
         |          |
          \        /
           `._,._.'""")
         # ----- Zona LOL -----
    elif ent == "i am happy":
        printx("Im going to bother you to make you angry")
    elif ent == "i lost my phone":
        printx("Look for it, LOL")
    elif ent == "ragebait":
        printx("Hey5: You smell bad (just kidding)")
        printx("SYS: i am angry")
        printx("Hey5: Do you know what Ragebait is?")
        printx("SYS: No")
        printx("Hey5: When they get angry about something of a joke")
    elif ent == "the table of one (Its very easy)":
        printx("1x1 = 1")
        printx("1x2 = 2")
        printx("1x3 = 3")
        printx("1x4 = 4")
        printx("1x5 = 5")
        printx("1x6 = 6")
        printx("1x7 = 7")
        printx("1x8 = 8")
        printx("1x9 = 9")
        printx("1x10 = 10")
        printx("You were right, it's very easy")
    elif ent == "spanish mode":
        printx("El monte everest no tiene nada en contra de mi")
    elif ent == "chinese mode":
        printx("珠穆朗玛峰对我没有任何敌意")
    elif ent == "ching chang chung":
        printx("Chang Chung cheng ching chang")
    elif ent == "padres que se arrempintieron de tener hijos":
        printx("you")
    elif ent == "polish mode":
        printx("Mount Everest nie ma nic przeciwko mnie")
    elif ent == "buy a PC":
        printx("*grabs it and throws it*")
      # ----- Final de la Zona LOL -----
    elif ent == "help":
        printx("time, clear, quit, mkdir, dir, cfle, mf, mksdir, sdir, echo")
        printx("Advanced:loa, low, lol, lom")
    elif ent.startswith("pyrun "):
        file_run = ent[6:]
        if os.path.exists(file_run):
            os.system(f"python {file_run}")
        else:
            printx("sys: VectorOS: no such file or directory")
    elif ent == "help $pyrun":
        printx("Pyrun is used for to run external python files, remember that the Python files you want to run must be in /storage/emulated/0/VectorOS")
    else:
        err = root.find('error')
        if err is not None:
            msg = err.text.replace("{ent}", ent)
            printx(msg)
        else:
            printx("Command Not Found")