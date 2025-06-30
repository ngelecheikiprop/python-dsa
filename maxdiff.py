#!/usr/bin/python3

def find_max(num):
    """to find the max value of a number"""
    num_str = str(num)
    # print(type(num_str))
    for letter in num_str:
        # print(f"letter for now is {letter}")
        if letter != '9':
            # print(f"type of num_str is {type(num_str)}")
            replace_str = num_str.replace(letter, "9")
            # print(f"after replacing {replace_str}")
            break
    return int(replace_str)

def find_min(num):
    """to find the min value of a number"""
    num_str = str(num)
    # print(type(num_str))
    i = len(num_str) - 1
    while i >= 0:
        letter = num_str[i]
        # print(f"letter for now is {letter}")
        if letter != '0':
            # print(f"type of num_str is {type(num_str)}")
            replace_str = num_str.replace(letter, "0")
            # print(f"after replacing {replace_str}")
            break
    return int(replace_str)

# print(find_min(11891))

def maxDiff(num):
    return find_max(num) - find_min(num)

print(f"the max diff of the number given is : {maxDiff(11891)}")


"""
===================
white boarding 
===================

to make a number big make the left most digit big
to make a number small make the right most number small 

change all the values 

11
11891

99899

00890


loop through all numbers, if the number there 


"""