#!/usr/bin/python3

astr = "kiprop"

def reverse_str(a_str):
    """reverse a string"""
    reversed_string = ""
    i = len(a_str) - 1

    while i >= 0:
        reversed_string += a_str[i]
        i -= 1
    
    return reversed_string

print(reverse_str(astr))