#!/usr/bin/python3
""" reversing string with stacks """


"""
FUNCTION  reverse_string(str)
INIT stack TO []
INIT reversed_str

FOR element IN str: 
    APPEND TO stack

WHILE stack:
    SET reversed_str TO WHAT IS POPED BY stack

"""

def reverse_string(str):
    stack = []
    reversed_str = ""
    for element in str:
        stack.append(element)

    while stack:
        reversed_str += stack.pop()
    return reversed_str

print(reverse_string("kiprop"))