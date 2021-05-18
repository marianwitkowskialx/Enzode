
# Dekorator

class BaseClass:
    def func1(self):
        print("BaseClass - func1")

    def func2(self):
        print("BaseClass - func2")

# klasa dekorująca
class DecoratorClass:
    def __init__(self, base_class):
        self._base_class = base_class

    def func1(self):
        print("Dekorator dla func1")
        self._base_class.func1()

    def __getattr__(self, item):
        return getattr(self._base_class, item)

###
obj = BaseClass()
obj.func1()

obj_decorator = DecoratorClass(obj)
obj_decorator.func1()
obj_decorator.func2()