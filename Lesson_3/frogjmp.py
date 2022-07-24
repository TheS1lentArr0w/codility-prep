# Time complexity: O(1)

def solution(X, Y, D):
    # Edge case, X == Y
    if X == Y:
        return 0
    
    distance = Y - X

    
    if distance % D == 0:
        # if distance can be traversed by D cleanly, ending up at exactly Y, return that
        return distance//D

    else:
        # return the above but 1 more step
        return distance//D + 1