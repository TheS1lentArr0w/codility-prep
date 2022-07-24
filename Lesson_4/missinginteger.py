#######
## Was correct
## Time complexity: O(N**2)
## Problem is that searching the entire list
### every single time
#######

""" def solution(A):
    checking_num = 1
    num_exists = True
    while num_exists:

        # check if checking_num exists
        if checking_num in A:
            # it exists
            checking_num += 1
            continue
        else:
            # it doesn't exist
            num_exists = False
            break
    
    return checking_num """

#######
## Finally good
## Time complexity: O(N) or O(Nlog(N))
#######

def solution(A):

    # edge case, 1 doesn't exist
    if 1 not in A:
        return 1

    bool_array = [False] * max(A)

    for elem in A:
        if elem < 0:
            continue
        else:
            if bool_array[elem-1] == False:
                bool_array[elem-1] = True
    
    for index,bool in enumerate(bool_array):
        if bool == False:
            return index+1
    
    return max(A) + 1