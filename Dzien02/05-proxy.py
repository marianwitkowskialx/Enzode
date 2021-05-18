
# Proxy

class Car:
    def drive(self):
        print("I'm driving....")

class CarProxy():
    def __init__(self):
        self._age = 15
        self._car = None

    def drive(self):
        if self._age>=18:
            self._car = Car()
            self._car.drive()
        else:
            raise ValueError("Za młody!")

#####
car = CarProxy()
car._age = 14
car.drive()