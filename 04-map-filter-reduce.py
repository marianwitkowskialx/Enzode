import numpy as np

# Map, filter, reduce
numbers = [5, 2, 10, -10, 4]

"""
result = []
for num in numbers:
    result.append( num**2 )
print(result)
"""

#result = [n**2 for n in numbers]
#print(result)

def square(x):
    return x**2

#print( list(map( square, numbers )) )
print( list(map( lambda x: x**2 , numbers )) )
print( np.array(numbers)**2 )

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
print( list(map( lambda x,y: x+y , l1, l2 )) )
print(np.array(l1) + np.array(l2))

# filtrowanie
# numbers > 0
print( list(filter(lambda x:x>0, numbers)) )

arr = np.array(numbers)
print( arr[arr>0] )

# reduce
from functools import reduce
numbers = [1,2,3,4,5]
"""
[2,3,4,5]
[6,4,5]
[24,5]
= 24*5
"""
print(reduce(lambda x,y:x*y, numbers))




