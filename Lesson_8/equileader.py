#######
## Seems like a combination of leader problem and prefix sums problem
## Link: https://www.youtube.com/watch?v=CZHukXHrFu4&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=24
## Time complexity: O(N)
#######

def solution(A):
    # first, find the leader and total count of leader
    total_count,leader = find_leader(A)

    # iterate over array
    leader_count = 0
    equileader_count = 0
    for index in range(0,len(A)-1):

        if A[index] == leader:
            leader_count += 1

        # equileader check
        if index+1<2*leader_count and len(A) - index - 1 < 2*(total_count-leader_count):
            equileader_count += 1

    ## return number of equileaders
    return equileader_count

def find_leader(A):

    ## edge cases
    if A == []:
        return 0,-1
    if len(A) == 1:
        return 1,A[0]

    ## return index of any dominator
    B = sorted(A)

    candidate = B[len(B) // 2]
    count = 0

    for elem in B:
        if elem == candidate:
            count += 1
    
    if count > len(A) // 2:
        return count,candidate
    else:
        return 0,-1