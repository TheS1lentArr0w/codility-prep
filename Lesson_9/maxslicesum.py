#######
## YouTube link to explain the algorithm
## Link: https://www.youtube.com/watch?v=OFHjuHCJdmU&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=26
## This is Kadane's Algorithm
## Time complexity: O(N)
#######

def solution(A):
    mysum = 0
    mymax = float('-inf')

    for elem in A:
        mysum += elem

        if elem > mysum:
            mysum = elem
        
        if mysum > mymax:
            mymax = mysum
    
    return mymax