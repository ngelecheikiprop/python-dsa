"""

INTIALIZE binary_str

WHILE NUM // 2 != 0:
    APPEND NUM % 2 TO binary_str
ENDWHILE

RETURN binary_str
"""

def to_binary(num):
    """ make a number binary """
    binary_str = ""
    # bin_num = 0
    # mult = 1
    
    while num // 2 !=  0:
        # bin_num += num % 2
        # bin_num *= mult
        # mult *= 10
        binary_str += str(num % 2)
        num //= 2
    binary_str += str(num % 2)
    # return str(bin_num)
    return reverse_str(binary_str)

def reverse_str(a_str):
    """ reverse a string """
    reversed_string = ""
    i = len(a_str) - 1

    while i >= 0:
        reversed_string += a_str[i]
        i -= 1
    return reversed_string

print(to_binary(8))