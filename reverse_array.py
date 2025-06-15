"""
INTIALIZE reversed_array
GET length of array
SET i TO length of array - 1

WHILE i >= 0;
    GET ith element of array
    APPEND to reversed array
    DECREMENT i
ENDWHILE

RETURN reversed_array
"""

def reverse_array(array):
    """function to reverse an array"""
    reversed_array = []
    i = len(array) - 1

    while i >= 0:
        reversed_array.append(array[i])
        i -= 1
    
    return reversed_array

cars = ["bentley", "subaru", "land rover"]
print(reverse_array(cars))