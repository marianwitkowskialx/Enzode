# Dekoratory

# "normalna" funkcja
def generic_func():
    print("Funkcja typu generic")

# dekorator funkcji
def dekor(func):
    def internal_func():
        print("Dekor internal func")
        return func()

    return internal_func

#dekor_func = dekor(generic_func)
#dekor_func()

from datetime import datetime
##### aplikacja dekoratora na funkcji #######
def apply_discount(func):
    def wraper():
        if datetime.now().hour>=13 and datetime.now().hour<16:
            return 0.9*func()
        else:
            return func()

    return wraper

@apply_discount  # aplikacja dekoratora
def get_price():
    return 100.00

#print(get_price())

#######################################
import functools

@functools.lru_cache(128) # cache'owanie wyników funkcji - memoizacja
def fibo_rek(n):
    if n<=1:
        return n
    else:
        return fibo_rek(n-2) + fibo_rek(n-1)

def fibo_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

N = 55
#print(fibo_rek(N), fibo_loop(N))

import time

ts1 = time.time_ns()
for _ in range(1_000):
    fibo_rek(N)
ts2 = time.time_ns()
print(ts2-ts1)
fibo_rek.cache_clear()

ts1 = time.time_ns()
for _ in range(1_000):
    fibo_loop(N)
ts2 = time.time_ns()
print(ts2-ts1)

