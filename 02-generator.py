
# Generatory
"""
for x in range(3):
    print(x)
"""

def my_generator():
    n = 1
    print("Pierwsze wzbudzenie")
    yield n

    n += 1
    print("Drugie wzbudzenie")
    yield n

    n += 1
    print("Trzecie wzbudzenie")
    yield n

gen = my_generator()
items = []
x = next(gen)
items.append(x)

x = next(gen)
items.append(x)

x = next(gen)
items.append(x)

#x = next(gen)
#items.append(x)

print(items)

# wykorzystanie generatora w uchwycie pliku
with open("01-funkcje.py", "rt", encoding="utf8") as fd:
    for line in fd:
        print(line.rstrip())



