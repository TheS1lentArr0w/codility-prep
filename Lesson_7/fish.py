#######
## Another stack problem
## Time complexity: O(N)
#######

def solution(A, B):
    fish_eaten = 0
    fish_stack = []

    for index in range(0,len(A)):

        # skip until you find the first fish headed east
        ## AKA B elem == 1
        if B[index] == 0 and fish_stack == []:
            continue
        
        # B elem == 1 now
        if B[index] == 1:
            fish_stack.append(A[index])
        else:
            # B elem == 0
            # Need to do comparisons
            for elem in reversed(fish_stack):
                if A[index] > elem:
                    # new fish eats fish in fish_stack
                    fish_stack.pop()
                    fish_eaten += 1
                else:
                    # fish in fish_stack eats new fish
                    fish_eaten += 1
                    break
    
    return len(A) - fish_eaten