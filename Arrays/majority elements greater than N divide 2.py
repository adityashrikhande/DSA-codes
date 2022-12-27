
def findMajorityElement(arr, n):
	# Write your code here.
	
    count = 0
    element = 0
    
    for num in arr:
        if count == 0:
            element = num
        
        if num == element:
            count += 1
        else:
            count -= 1
            
    count = 0
    for num in arr:
        if num == element:
            count += 1
    
    if count <= n//2:
        return -1
            
    return element