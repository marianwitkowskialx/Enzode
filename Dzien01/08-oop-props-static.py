from datetime import date

# OOP - metody statyczne, classmethods, properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name={self.name}, age={self.age}"

    @staticmethod
    def is_adult(age):
        return age>=18

    @classmethod
    def create_from_year(cls, name, yob):
        age = date.today().year - yob
        return cls(name, age)

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def del_age(self):
        del(self.age)

    AGE = property(get_age, set_age, del_age)

person1 = Person("Jan", 33)
print(person1)

print(Person.is_adult(18))

person2 = Person.create_from_year("Bob", 1980)
print(person2)
print(person2.AGE)
person2.AGE = 44
print(person2.AGE)
del(person2.AGE)
print(dir(person2))
