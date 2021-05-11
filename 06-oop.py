
# OOP
class MetaProduct:
    pass

class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_info(self):
        return f"Id={self.__id}, nazwa:{self.__name}, price: {self.__price}"

    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return self.get_info()

# Dziedziczenie klas
class Alcohol(Product):

    def __init__(self, id, name, price, type="vodka"):
        super(Alcohol, self).__init__(id, name, price)
        self.__type = type

    def __str__(self):
        s = f"{super().__str__()}, type={self.__type}"
        return s
#############
coca_cola = Product(1, "Coca-cola", 4.99)
print(coca_cola.get_info())

coca_cola.set_price(4.29)
print(coca_cola)

#print(dir(coca_cola))
coca_cola._Product__price = 999 # nadpisanie pola "prywatnego" z zewnątrz obiektu
print(coca_cola)

smirnoff = Alcohol(2, "Smirnoff", 88, "vodka")
print(smirnoff)





