#######
## Was a good idea, but has edge cases where
### total sum is correct but it is not 
### a permutation
#######


""" def solution(A):
    max_number = len(A)
    summation = int((max_number**2 + max_number)/2)

    if summation == sum(A):
        # correct
        return 1
    else:
        return 0     """

#######
## My own solution AND IT PASSED
## Time complexity: O(N) or O(N*log(N))
#######

def solution(A):

    # Edge cases
    if max(A) != len(A):
        return 0

    checklist = [-1]*len(A)
    unchecked = len(A)
        
    for elem in A:
        pos_index = elem-1
        if checklist[pos_index] != -1:
            # number already checked
            continue
        else:
            # number needs to be checked
            checklist[pos_index] = 1
            unchecked -= 1
    
    if unchecked == 0:
        # it is a permutation
        return 1
    else:
        return 0