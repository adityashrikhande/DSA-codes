
def majorityElementII(arr):
	# Write your code here.
    c1 = 0
    c2 = 0
    n1 = -1
    n2 = -1
    
    n = len(arr)
    
    for num in arr:
        if num == n1:            # sequence is IMP
            c1 += 1
        elif num == n2:
            c2 += 1
        elif c1 == 0:
            n1 = num
            c1 = 1
        elif c2 == 0:
            n2 = num
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    
    c1 = 0
    c2 = 0
    for i in range(n):
        if arr[i] == n1:
            c1 += 1
        elif arr[i] == n2:
            c2 += 1
            
    ans = []
    if c1 > n//3:
        ans.append(n1)
    if c2 > n//3:
        ans.append(n2)
        
    return ans
        
        