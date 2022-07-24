#######
## Really elegant solution
## Link: https://stackoverflow.com/questions/48046020/passingcars-in-codility-using-python
## Time complexity: O(N)
#######

def solution(A):
    zeros = 0
    passing = 0

    for elem in A:
        if elem == 0:
            # keep totalling zeros
            zeros += 1
        else:
            # every time a 1 occurs, all zeros
            ## pass it
            passing += zeros
    
    # edge case
    if passing > 1000000000:
        return -1
    
    return passing