#!/usr/bin/python3
"""

'(', '{', '[', ']', '}' ')'

}

stack = {,   


FUNCTION solution(S)

    INIT stack TO []
    FOR c IN S DO
        IF c == ')'  and '(' IN stack AND stack.pop() == '(' THEN
            CONTINUE
        ELSE IF  c == '}'  and '{' IN stack AND stack.pop() == '{' THEN
            CONTINUE
        ELSE IF c == ']'  and '[' IN stack AND stack.pop() == '[' THEN
            CONTINUE
        ELSE IF '{' or  '(' or '['
            APPEND TO stack
        ELSE 
            RET FALSE
    RET TRUE

{[()()]}

how do I check the opposite?
if { check }
start with this

append()

"""


def solution(S):
    stack = []
    for c in S:
        if c == ')' and '(' in stack and stack.pop() == '(':
            continue
        elif c == '}' and '{' in stack and stack.pop() == '{':
            continue
        elif c == ']' and '[' in stack and stack.pop() == '[':
            continue
        elif c == '[' or c == '{' or c == '(':
            stack.append(c)
        else:
            return False
    return True

print(solution("([)()]"))
