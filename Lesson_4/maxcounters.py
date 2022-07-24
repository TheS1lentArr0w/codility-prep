#######
## My own solution
## Correctness is 100%
## Time complexity: O(N*M)
## Timed out with large samples
## To do with max counter operation happening
### everytime
#######

""" def solution(N, A):
    counters = [0] * N
    for operation in A:

        # Do max counter operation first
        if operation > len(counters):
            counters = [max(counters)] * N
            continue
        
        # increase(X) operation
        counter_index = operation-1
        counters[counter_index] += 1
    
    return counters """

#######
## 
#######

def solution(N, A):
    counters = [0] * N
    max_val = 0         # The used value in previous max counter operation
    current_max = 0     # Current max val of any counter
    for operation in A:

        if 1 <= operation <= N:
            # increase(X) command

            # only occurs when max_val is larger
            # therefore, lazy write
            if max_val > counters[operation-1]:
                counters[operation-1] = max_val
            
            # normal increase(X)
            counters[operation-1] += 1

            # update current_max
            if current_max < counters[operation-1]:
                current_max = counters[operation-1]
        else:
            # max counter operation
            # just record current maximum value
            ## for later writing
            max_val = current_max
    
    # update counters
    # if any counter below max_val
    for index in range(0,N):
        if counters[index] < max_val:
            counters[index] = max_val
    
    return counters

#######
## Reason why the above scores 100% is because of
## lazy writing. When max counters operation 
## occurs, keeping a side note on it.
## Then, update counters at the very end
## Time complexity: O(N + M)