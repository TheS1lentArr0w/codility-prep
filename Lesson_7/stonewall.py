#######
## Solution is a bit tricky to wrap my head around
## Link: https://www.youtube.com/watch?v=BhBJ7MqjF-s&list=PLwEOixRFAUxZHuTDDgdmE0d4I40mBZLbF&index=22
## Time complexity: O(N)
#######

def solution(H):
    last_elem = 0
    stonescount = 0
    storage = []

    for index in range(0,len(H)):
        if H[index] > last_elem:
            # Increasing in height
            ## Can only add a stone for this condition
            last_elem = H[index]
            stonescount += 1
            # Keep this height in storage just in case it's needed
            storage.append(H[index])
        
        elif H[index] < last_elem:
            # Decreasing in height

            while len(storage) > 0 and H[index] < storage[-1]:
                # checking to see if current height is lower than what is
                # previously seen
                # If so, not needed in memory
                storage.pop()
            
            if len(storage) == 0 or H[index] != storage[-1]:
                # check if storage is empty, if so, need another stone for this height
                # if storage isn't empty and the heights match, can use a previous
                ## stone for this height
                # the last check checks for mismatching heights
                ### E.G. envision going down the side of a pyramid
                stonescount += 1
                storage.append(H[index])
            
            last_elem = H[index]
    
    return stonescount