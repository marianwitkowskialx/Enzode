
# Singleton - jedna instancja obiektu w całej aplikacji
class Singleton:
    _INSTANCE = None

    class __Singleton:
        def __init__(self):
            self._data = None

        def set_data(self, data):
            self._data = data

        def get_data(self):
            return self._data

    def __new__(self):
        if not Singleton._INSTANCE:
            Singleton._INSTANCE = Singleton.__Singleton()
        return Singleton._INSTANCE

###
singleton = Singleton()
singleton.set_data({"a":1, "b":2, "c":3})
print(singleton.get_data())
