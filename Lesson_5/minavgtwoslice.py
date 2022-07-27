#######
## This is a maths problem
## Difficult if you haven't seen it before
## Link: https://www.youtube.com/watch?v=Xu_hTjFAauk&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=13
#######

#######
## BIG ASSUMPTION
## Would not have known this otherwise

## Slices of 4 or more numbers always contain a smaller slice
## with a lower average
### THEREFORE
## Only slices of 2 or 3 need to be tested.

#######

def solution(A):
    min_avg = float('inf')
    start_index = 0

    for index in range(0,len(A)-2):
        avg1 = (A[index] + A[index+1] + A[index+2])/3
        avg2 = (A[index] + A[index+1])/2
        new_min = min(avg1,avg2)
        if new_min < min_avg:
            min_avg = new_min
            start_index = index
    
    # Edge case, last 2 elements slice is not tested
    avg1 = (A[-2] + A[-1]) / 2
    if avg1 < min_avg:
        min_avg = avg1
        start_index = len(A)-2
    
    return start_index