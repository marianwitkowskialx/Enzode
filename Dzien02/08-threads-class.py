
# Wątek na bazie klasy Thread
import threading
import time

class MyThread(threading.Thread):

    def __init__(self, name, counter, sleep):
        super(MyThread, self).__init__()
        self._counter = counter
        self._name = name
        self._sleep = sleep

    def run(self):
        print(f"starting {self._name}")
        while self._counter:
            print(f"Thread {self._name}: counter {self._counter}")
            time.sleep(self._sleep)
            self._counter -= 1

if __name__ == "__main__":
    t1 = MyThread("TH1", 10, 1)
    t2 = MyThread("TH2", 6, 3)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")