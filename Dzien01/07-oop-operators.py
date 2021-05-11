
# Przeciązanie operatorów

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[ {self.x} , {self.y} ]"

    def add_vector(self, vector):
        return Vector( self.x+vector.x , self.y+vector.y )

    def __add__(self, vector):
        if type(vector) is Vector:
            return Vector( self.x+vector.x , self.y+vector.y )
        if type(vector) in [int, float]:
            return Vector( self.x+vector , self.y+vector )
        if type(vector) is tuple and len(vector)==2:
            return Vector(self.x + vector[0], self.y + vector[1])
        raise TypeError("błędny typ danych")

    def __eq__(self, vector):
        return self.x==vector.x and self.y==vector.y

v1 = Vector(2, 3)
v2 = Vector(2,3)

v3 = v1.add_vector(v2)
print(v3)
print(v1 == v2 )