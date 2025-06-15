# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    found_zeros = []
    binary_n = bin(N)[2:]
    found_1 = False
    count = 0

    for x in binary_n:
        if x == '0' and found_1:
            count += 1
        if x == '1' and not(found_1):
            found_1 = True
        elif x == '1' and found_1:
            found_zeros.append(count)
            count = 0
    return max(found_zeros)

"""
binary gap

- change to binary 
- count the zeros

- if I see 1 i start counting the zeros 
- I can use 
9 

9 / 2 = 4 rem  1
4/2 = 2 rem 0
2/2 = 1 rem 0
1 / 2 = 
1001

8 / 2 = 4 rem 0
4/2 = 2 rem 0



def to_binary (num):
    binary_str = ""

    while num = 

    return int(binary_str)
"""
