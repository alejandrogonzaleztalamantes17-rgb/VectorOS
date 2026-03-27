import datetime
from etc.printxf import printx

def times():
    time_f = datetime.datetime.now().strftime("%H:%M:%S")
    printx(time_f)