def solution(A):
    A.sort()

    try1 = A[-1] * A[-2] * A[-3]
    # 2 -ve and 1 +ve could be larger product
    try2 = A[0] * A[1] * A[-1]

    return max(try1, try2)