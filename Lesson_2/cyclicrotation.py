def solution(A, K):
    # Use modular arithmetic, modulo operator
    # x = (x + y) % a
    ## Where a is the largest number it needs to be. (e.g. for a 12hr clock, a = 12)

    # create return array the same size as A
    B = [0] * len(A)

    for idx,elem in enumerate(A):
        B[(idx + K) % (len(A))] = elem

    return B