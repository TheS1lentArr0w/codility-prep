#######
## Seems like a stack problem similar to brackets.py
#######

def solution(S):
    bracket_stack = []

    for elem in S:
        
        if elem == '(':
            bracket_stack.append(elem)
        elif elem == ')':
            if bracket_stack == []:
                return 0
            else:
                bracket_stack.pop()
    
    if bracket_stack == []:
        return 1
    else:
        return 0