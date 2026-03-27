import datetime
import sys
import select
import time

def timelives():
    running = True

    print("PRESS ENTER TO STOP")

    while running:
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        sys.stdout.write("\r" + hora + "   ")
        sys.stdout.flush()

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            input()
            running = False

        time.sleep(1)

    print("\nStopped.")
