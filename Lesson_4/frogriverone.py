def solution(X, A):
    ## Edge cases
    # if 1 not in array, cannot cross
    if 1 not in A:
        return -1
    
    # variables
    covered = [-1]*X
    uncovered = X

    for index,elem in enumerate(A):
        pos_index = elem-1
        if covered[pos_index] != -1:
            # position already covered
            continue
        else:
            # position needs to be covered
            covered[pos_index] = 1
            uncovered -= 1
            if uncovered == 0:
                # all positions covered
                return index
    
    # some positions not covered
    return -1

## Had some help from below link
## Link: https://codesays.com/2014/solution-to-frog-river-one-by-codility/
## Time Complexity: O(N)