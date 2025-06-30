#!/usr/bin/python3 

"""
print all possible 

start with 2 letters 

ab -> ba 

swap str[1]str[0]


abc

abc
acb
cba

"""

def swap(letters):
    """
    assuming always 2 letters:
    return letters [1]+letters[0]
    """
    return letters [1]+letters[0]

letters = "ab"
print(swap(letters))

def permutate(letters):
    """
    print as it is 
    for 3 letters 
    rotate , flip

    rotate function 
    """
    pass


def rotate(word):
    """
    INTIALIZE new_word TO ""
    SET word_lenght TO len(word)

    FOR i FROM 0 TO word_length INCR 1
        new_word += 'x'
    ENDFOR

    FOR idx FROM 0 TO word_lenght INCR 1:
        new_idx = idx + 1
        IF new_idx >= word_length:
            new_idx -= word_length
        ENDIF
        new_word += word[idx]
    ENDFOR
    """

    new_word = ""
    word_len = len(word)
    print("making temp")
    
    #fill the worrd with temporary values to have a place to put values later
    for i in range(word_len):
        new_word += 'x'
    print(new_word)

    print("finished making temp")
    
    for idx in range(word_len):
        print("inside the secend for loop with idx {}".format(idx))
        new_idx = idx + 1
        if new_idx >= word_len:
            print("inside if statment")
            print("idx for {} now is {} and will be {}".format(word[idx], idx, new_idx))
            new_idx -= word_len
        new_word = replace(new_word, word[idx], new_idx)
    return new_word 

def replace(letter, char,  idx):
    if (idx) >= len(letter):
        raise  IndexError("index out of range")
    return letter[0:idx] + char + letter [idx+1:]


rotate("abc")


letters = "abcd"
len(letters)
rep_a = replace(letters,'x', 4)
print(rep_a)

numbers = [1,2,3,4]
numbers[3] = 5
print(numbers)

"my first name is {1} and last name {0}".format("david", "kiprop")