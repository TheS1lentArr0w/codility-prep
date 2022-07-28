#######
## Link to lesson: https://codility.com/media/train/6-Leader.pdf
## There is a more efficient solution in the lesson if needed
## Time complexity: O(NlogN) or O(N)
#######

def solution(A):

    ## edge cases
    if A == []:
        return -1
    if len(A) == 1:
        return 0

    ## return index of any dominator
    B = sorted(A)

    candidate = B[len(B) // 2]
    count = 0

    for elem in B:
        if elem == candidate:
            count += 1
    
    if count > len(A) // 2:
        return A.index(candidate)
    else:
        return -1