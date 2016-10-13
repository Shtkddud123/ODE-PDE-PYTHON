import threading
import time

def loop1_10():
    for i in range(1,11):
        time.sleep(5)
        print(i)

threading.Thread(name="dfdf",target=loop1_10).start()
