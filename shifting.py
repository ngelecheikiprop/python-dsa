"""
[3, 8, 9, 7, 6]
 [9, 7, 6, 3, 8]
0 + 3 = 3
gaps 3 

0 -> 3 (0 + 3)
4 -> 2 (4 + 3 - 5)

6 + 3 = 

FUNCTION (A, K)
    INTIALIZE shifted_arr TO []
    INTIALIZE shifted_idx TO 0
    INTILIAZE length_of_array TO LENGHT OF k
    INTILIAZE i TO 0  
    FOR element IN A DO
        APPEND "temp" TO shifted_arr
    WHILE i < LENGTH OF A DO
        ASSIGN i + K TO shifted_idx
        IF shift_idx >= i THEN
            UPDATE shifted_idx TO  shifted_idx - length_of_array
        ENDIF
        shifted_arr[shifted_idx] = a[i]
    RETURN shifted_arr

"""

def shift_array(a, k):
    shifted_arr = []
    shifted_idx = 0
    len_of_array = len(a)
    i = 0
    for element in a:
        shifted_arr.append("temp")
    while i < len_of_array:
        # print(a[i])
        shifted_idx = i +  k
        if shifted_idx >= len_of_array:
            shifted_idx -= len_of_array
        shifted_arr[shifted_idx] = a[i]
        i += 1
    return shifted_arr

print(shift_array([3, 8, 9, 7, 6], 3))