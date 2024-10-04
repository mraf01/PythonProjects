import time
import sys

sys.stdout = open("./file_per_le_print.txt", "w+")

ii = 1
while ii < 10:
    time.sleep(2)
    print("Ciao a tutti da myapp")
    sys.stdout.flush()
    ii += 1

sys.stdout.close()
