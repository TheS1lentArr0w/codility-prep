#######
## Stack problem
## Got this pretty much myself
## Just forgot about edge case where a closing bracket occurs before an opening one
#######


def solution(S):
    bracket_stack = []
    opening_brackets = ['(','{','[']
    closing_brackets = [')','}',']']
    my_dict = {
    ')':'(',
    '}':'{',
    ']':'['
    }

    for elem in S:
        if elem in opening_brackets:
            # Opening a new bracket
            bracket_stack.append(elem)
        
        if elem in closing_brackets:
            # First, check if there is anything in bracket_stack
            # If not, that means a closing bracket occurred without its opening pair
            if bracket_stack == []:
                return 0

            # Make sure top of stack matches the closing bracket
            if my_dict[elem] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return 0
    
    if bracket_stack == []:
        return 1
    else:
        return 0