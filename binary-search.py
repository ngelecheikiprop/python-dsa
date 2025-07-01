#!/usr/bin/python3
""" searches in a sorted list using recursion """

""" PSEUDO CODE

FUNCTION binary_serach(arr, target)
    
    SET arr_len TO lenght of arr
    SET mid_idx TO arr_len / 2

    IF arr_len == 0 THEN
        RAISE empty array
    ENDIF

    IF arr_len == 1:
        IF arr[0] == target
            RET True
        RET false
    ENDIF

    IF arr[mid_idx] == target THEN
        return mid_idx 
    ELSE IF arr[mid_idx] < target THEN
        binary_search(arr[mid_idx + 1 : ], target)
    ELSE IF arr[mid_idx] > target THEN
        binary_search([:mid_idx], target)
    ENDIF


arr 1,2,3,4
    0,1,2,3
    4 / 2  = 2
    arr[2] = 3
    3 !4 
    3 < 4 yes  -> 4 target
    1 / 2 = 0
    if lenght is 1 check if equal then return the value
"""

def binary_search(arr, target):
    """
    looks for  a value in a array
    
    Args:
        arr(array): what to search in
        target(int, string): what to look for

    Returns:
        True if value is inside
        False if not 
    """
    arr_len = len(arr)
    mid_idx = arr_len // 2
    print("mid idx is {}".format(mid_idx))

    if arr_len == 0:
        raise ValueError("empty array has been given")
    
    #if we have one value in the array just check it againist the target
    if arr_len == 1:
        print("we have reached the end, array has lenght  1 with value {}".format(arr[0]))
        if arr[0] == target:
            return True
        return False
    
    
    if arr[mid_idx] == target:
        print("{} is equal to {}".format(arr[mid_idx], target))
        return True
    elif arr[mid_idx] < target:
        print("{} is less than  {}".format(arr[mid_idx], target))
        return binary_search(arr[mid_idx + 1:], target)
    elif arr[mid_idx] > target:
        print("{} is more than {}".format(arr[mid_idx], target))
        print("going to {}".format(arr[:mid_idx]))
        return binary_search(arr[:mid_idx], target)


print(binary_search([1,2,3,4,5,6,7,8,9], 5))