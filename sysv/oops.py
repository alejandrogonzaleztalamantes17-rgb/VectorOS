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

entmdf = "V\\>"

printx("VectorOS 1.0")
whilef = True
while whilef:
    ent = input(entmdf).strip()

       
    if ent == "time":
        times()
    elif ent == "quit":
        quits()
    elif ent == "clear":
        clears()
    elif ent == "miau":
        print("""/\\_/\\
( o.o )
> ^ <""")