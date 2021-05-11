import math

a = "Ala ma kota"
b = 12.34

a, b = "Ala ma kota", 12.34
a = "Ala ma kota"; b = 12.34 # nie "w duchu" Pythona


x = 10
# Funkcje
def test():
    global x
    print(x)
    pass

# Type hint dla parametrów funkcji
def oblicz_pole_kola(r : float) -> float:
    r = float(r)
    if not type(r) in [int, float]:
        raise TypeError("zły format danej")
    return math.pi*(r**2)

#print(oblicz_pole_kola("2.5"))

# Funkcje z parametrami opcjonalnymi
def create_employee(fname, lname, phone="221234567", email="hello@company.com"):
    return {
        "fname" : fname, "lname": lname,
        "phone" : phone, "email" : email
    }


"""
print(create_employee("John","Wick","606123456", "john@wick.com"))
print(create_employee("John","Wick"))
print(create_employee("John","Wick", email="john2@wick.com"))
print(create_employee("John","Wick", phone="123456789"))
print(create_employee("John","Wick", "123456789"))
print(create_employee("John","Wick", email="john2@wick.com", phone="123456789"))
print("Hello","world!", sep=" | ", end="**KONIEC LINII")
"""

######## funkcja z dowolną liczbą parametrow ########
def many_arguments(_id, *args):
    print(f"ID={_id}")
    for arg in args:
        print( str(arg)[::-1] )

#many_arguments(1, "Ala","ma","kota")

###### funkcja z parametrami nazwanymi ########
def many_keys(id, fallback="BRAK", **kwargs):
    print(f"ID={id}")
    print(f"fname={kwargs.get('fname', fallback)}")
    print(f"lname={kwargs.get('lname', fallback)}")
    print(f"email={kwargs.get('email', fallback)}")

many_keys(123, fname="John", lname="Wick", fallback="*")