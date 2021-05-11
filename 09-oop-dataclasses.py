
class Employee1:
    def __init__(self, name : str, yob : int, level : int =0):
        self.name = name
        self.yob = yob
        self.level = level

from dataclasses import dataclass

@dataclass
class Employee2:
    name : str = "ABCDEF"
    yob : int = 0
    level : int = 0

from dataclasses import field

@dataclass
class Employee3:
    name : str = "ABCDEF"
    yob : int = field(default=2000, repr=False, compare=False)
    level : int = 0

    def __post_init__(self):
        self.level = 1
        self.yob = "AAAAA"
        self.name = "XYZ"

employee = Employee3()
print(employee)

