def solution(N):

    # Type check
    if isinstance(N,int) == False:
        # Not an integer
        return 0
    
    # Within limits check
    if N < 1 or N > 2147483647:
        return 0

    # Convert N to binary
    binN = bin(N)   # Results in a string representation
    binN = binN[2:] # Trims the '0b' at the start of the string representation
    binN = binN.strip('0')  # strips leading and trailing '0's

    # .split()
    array_of_zeros = binN.split('1')

    return len(max(array_of_zeros))