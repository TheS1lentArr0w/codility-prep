#######
## My own solution
## Crap because time complexity is bad: O(N*N)
#######

""" def solution(A):
    Apre = []
    Apost = []
    smallest_diff = float('inf')
    for split in range(1,len(A)):
        Apre = A[0:split]
        Apost = A[split:]
        diff = abs(sum(Apre) - sum(Apost))
        
        if diff < smallest_diff:
            smallest_diff = diff
    
    return smallest_diff """

#######
## Can't fully understand the calculation of m within the for loop
## Got from stackoverflow
#######

""" def solution(A):  
    # Sum        
    s = sum(A)
    # Minimum
    m = float('inf')
    left_sum = 0

    # for each element from index 0 to index n-1 (doesn't include last element)
    for elem in A[:-1]:
        left_sum += elem
        m = min(abs(s - 2*left_sum), m)
    return m """


#######
## Got this solution from codesays
#######

def solution(A):
    # First element
    head = A[0]
    # Sum of 2nd element to end
    tail = sum(A[1:])
    # First difference calculated
    min_dif = abs(head - tail)
    # Start from index 1, last iteration is for second last element
    for index in range(1, len(A)-1):
        # add cur elem to head
        head += A[index]
        # subtract cur elem from tail
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif

## Faster because there is no constant slicing of the array
## Just accessing the array which is O(1), then taking that element and adding it
### to another integer
## Actual time complexity: O(N)
### This is due to the for loop
## Link: https://codesays.com/2014/solution-to-tape-equilibrium-by-codility/