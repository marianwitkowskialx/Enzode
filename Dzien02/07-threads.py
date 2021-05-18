
# Wątki w Python
import threading
import time

total_counter = 0
lock = threading.Lock()

def inc_total_counter():
    global total_counter
    global lock

    lock.acquire()
    total_counter += 1
    lock.release()
    
    print(f"Total counter: {total_counter}")

def func1(counter):
    while counter:
        print(f"func1: {counter}")
        time.sleep(1)
        inc_total_counter()
        counter -= 1

def func2(counter):
    while counter:
        print(f"func2: {counter}")
        time.sleep(2.8)
        inc_total_counter()
        counter -= 1

if __name__ == "__main__":
    # tworzenie wątków
    t1 = threading.Thread(target=func1, args=(5,) )
    t2 = threading.Thread(target=func2, args=(5,) )

    # wystartowanie wątków
    t1.start()
    t2.start()

    # poczekaj na koniec wątków
    t2.join()
    print("koniec t2")
    t1.join()
    print("koniec t1")


    print("Done")