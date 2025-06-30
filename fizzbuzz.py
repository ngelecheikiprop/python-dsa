"""
FOR i FROM 0 to 100 INCREMENT 1 do
    IF i % 3 == 0 AND 1 % 5 == 0 do
        print fizzbuzz
    ELSEIF i % 3 === 0:
        print fizz
    ELSEIF  i % 5 ===0 ;
        print buz
    ELSE
        i
    ENDIF
ENDFOR
"""

for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)