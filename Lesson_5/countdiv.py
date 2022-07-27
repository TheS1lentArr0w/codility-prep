#######
## Entirely a maths question
## Time complexity: O(1)
#######

def solution(A, B, K):
    if A % K == 0:
        return (B-A) // K + 1
    else:
        return (B - (A - A % K)) // K