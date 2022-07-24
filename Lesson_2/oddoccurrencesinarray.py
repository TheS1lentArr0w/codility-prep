#########
## This solution timed out on performance tests with bigger input arrays.
#########

# def solution(A):
#     # Can use % 2 to find out if there are even occurrences of a value

#     # Create set of A first to find all unique elements
#     B = set(A)

#     # Iterate through set and if occurrences of element % 2 != 0, return that
#     for elem in B:
#         count = A.count(elem)
#         if count % 2 != 0:
#             # Odd occurrences
#             return elem

#########

def solution(A):
    # Edge case if len(A) == 1
    if len(A) == 1:
        return A[0]
    
    # Bitwise XOR of all elements
    result = 0

    for elem in A:
        result ^= elem
    
    return result


## Explanation of above can be found here: https://codesays.com/2014/solution-to-perm-missing-elem-by-codility/
## Basically, pairs going through the XOR operation will return 0
## So when an odd element comes up, the result will become that element.
## Preferred solution because it's a really quick solution
## Time complexity becomes O(N) or O(N*log(N))