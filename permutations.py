#!/usr/bin/python3

def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)

def permutations(letters, r):
    n = len(letters)
    num = factorial(n)
    den = factorial(n-r)
    return num / den

permutations("ABC", 3)