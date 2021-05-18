
# Wzorzec Builder

class User:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def setFirstName(self, first_name):
        self._first_name = first_name

    def setLastName(self, last_name):
        self._last_name = last_name

    def setAge(self, age):
        self._age = age

    def print(self):
        print(f"User: {self._first_name} {self._last_name}, age:{self._age} ")

class UserBuilder:
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._age = ""

    @staticmethod
    def item():
        return UserBuilder()

    def withFirstName(self, first_name):
        self._first_name = first_name
        return self

    def withLastName(self, last_name):
        self._last_name = last_name
        return self

    def withAge(self, age):
        self._age = age
        return self

    def build(self):
        return User(self._first_name, self._last_name, self._age)

### przykład użycia ###
user = UserBuilder().item().\
    withFirstName("Jan").\
    withLastName("Kowalski").\
    withAge(44).build()
user.print()