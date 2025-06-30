"""
def (arr, targe)
    FOR item IN array:
        IF ellement == target 
            RET i
        ENDIF
    ENDFOR
    RET null
"""

def find_element(arr, target):
    for element in arr:
        if element == target:
            return arr.index(element)
    return 0

find_element([1,2,3,4], 3)