#######
# Could not for the LIFE OF ME wrap my head around 
# this solution
# Tried learning through the md file.
# Can try and work it out in future.

# Decided to go for an alternative solution below
#######
""" def solution(A):
    length = len(A)
    xor_sum = 0
    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index + 1)
    return xor_sum^(length + 1) """


#######
## Alternative Solution
## Time Complexity: O(N) or O(Nlog(N))
#######

def solution(A):
    # Edge case, empty array
    if len(A) == 0:
        return 1
    
    # Sort A in ascending order
    A.sort()

    # In this for loop, compare element to index
    # Element should == index + 1 (e.g. index 0, elem 1 etc.)
    # If not, that's your missing element
    for i in range(0,len(A)):
        if A[i] != i+1:
            return i+1
    
    # If the above for loop doesn't return anything
    # The missing element is at the end
    return (len(A)+1)
