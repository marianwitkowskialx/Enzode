import os
# Prosty kalkulator

class Calculator:

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        if b==0:
            raise ValueError("nie mozna dzielic przez zero")
        return a/b

    def dir_exist(self, name):
        return name in os.listdir()
