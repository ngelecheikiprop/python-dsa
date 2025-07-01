#!/usr/bin/python3
""" sorting an array using buble sort """

"""

[4,7,2,3]
 0 1 2

 i = 0
 temp = 0
 len = 4 

 1 < 4
 4 !> 7
 i = 1

 7 > 2 -> 
 arr 4 2 7 3
 idx 0 1 2 3


 i = 2
 7 is more -> 4 2 3 7

 i = 3 
 i + 1  = 4

 2 4 3 7
 2 3 4 7



 
FUNCTION buble_sort (arr)
    INIT i TO 0
    INIT temp TO 0
    SET arr_len = len(arr)
    WHILE i < arr_len
        WHILE i + 1 < arr_len THEN
            IF arr[i] > arr[i + 1] THEN
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i+1] = temp
            ELSE
                continue
            ENDIF
            INCR i
        ENDWHILE
        INCR 1
    ENDWHILE
    RET arr

"""

def buble_sort(arr):
    i = 0
    j = 0
    temp = 0
    arr_len = len(arr)

    print(arr)
    while j < arr_len:
        i = 0
        print("j = {}".format(i))
        while i + 1 < arr_len:
            print(" i = {}".format(i))
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                print(arr)
            i += 1
        j += 1
    return arr

print(buble_sort([7, 2, 9, 4, 1, 10, 3, 8, 6, 5]))