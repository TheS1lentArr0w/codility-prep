#######
## Going to actually try and learn prefix sums for this solution
## YouTube link explains algo, implementing algo myself personally
## Link: https://www.youtube.com/watch?v=4SyckIAmYXk

## Time complexity: O(N + M)
## Reason being a brute force algo would iterate over S each time a slice is needed
## Prefix sums allow you to access that information by only traversing S once and
## recording the results.
#######

def solution(S, P, Q):
    # Initialise A, C, G, T arrays
    # 1 if occurs, 0 if not
    A = [0] * len(S)
    C = [0] * len(S)
    G = [0] * len(S)
    T = [0] * len(S)

    nucleotide_dict = {
        'A':1,
        'C':2,
        'G':3,
        'T':4
    }

    for index,letter in enumerate(S):
        if letter == 'A':
            A[index] = 1
        elif letter == 'C':
            C[index] = 1
        elif letter == 'G':
            G[index] = 1
        elif letter == 'T':
            T[index] = 1
    
    # Make a prefix sums array of A, C, G, T

    A = prefix(A)
    C = prefix(C)
    G = prefix(G)
    T = prefix(T)

    results = []

    for index in range(0,len(P)):
        start = P[index]
        end = Q[index]

        # Edge case, start == end
        if start == end:
            results.append(nucleotide_dict[S[start]])
            continue
        
        ## This group of if statements require the 'or S[start] == "A"' condition
        ## because of the edge case of e.g. 'AC' and start=0,end=1. A prefix sum will be [1, 1]
        ## Algo won't see a change in the prefix sum and will move on, which is incorrect
        # Check for A
        if A[end] != A[start] or S[start] == "A":
            # Been a change
            results.append(1)
            continue
        # Check for C
        if C[end] != C[start] or S[start] == 'C':
            results.append(2)
            continue
        # Check for G
        if G[end] != G[start] or S[start] == 'G':
            results.append(3)
            continue
        # Check for T
        if T[end] != T[start] or S[start] == 'T':
            results.append(4)
            continue
    
    return results

def prefix(A):
    for i in range(1,len(A)):
        A[i] = A[i] + A[i-1]
    
    return A