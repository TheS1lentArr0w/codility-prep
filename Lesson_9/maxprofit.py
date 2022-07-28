#######
## A max slice problem. Link: https://codility.com/media/train/7-MaxSlice.pdf
## Got solution from YouTube.
## Link: https://www.youtube.com/watch?v=AOeexLMJ_5w&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=25
## The fastest solution from the codility lesson was confusing
#######

def solution(A):
    # edge case
    if A == []:
        return 0

    mymin = A[0]
    mymax = 0
    mysum = 0

    # Start from index 1 because need to compare to previous element
    for index in range(1,len(A)):

        # new minimum?
        if A[index] < mymin:
            mymin = A[index]
            mysum = 0
        else:
            mysum += A[index] - A[index-1]
        
        # new max?
        if mymax < mysum:
            mymax = mysum
    
    return mymax