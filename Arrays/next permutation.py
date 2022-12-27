
def nextPermutation(permutation, n): # given an array permutation containing elements from 1 to n in any order
    # Write your code here.
    # Return a list.
    
    split = -1
    
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i+1]:
            split = i
            break
    
    if split != -1:
        for i in range(n-1,-1,-1):
            if permutation[i] > permutation[split]:
                cng = i
                break
        permutation[split], permutation[cng] = permutation[cng], permutation[split]
        
        l = split + 1
        r = n-1
        
        while l < r:
            permutation[l], permutation[r] = permutation[r], permutation[l]
            l += 1
            r -= 1
             
    else:
        l = 0
        r = n-1
        while l < r:
            permutation[l], permutation[r] = permutation[r], permutation[l]
            l += 1
            r -= 1
            
    return permutation
            
        
             
                