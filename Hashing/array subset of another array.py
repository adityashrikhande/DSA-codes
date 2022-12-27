
def isSubset( a1, a2, n, m):
    
    dic = dict()
    
    for i in range(n):
        dic[a1[i]] = 0
    
    i = 0
    
    while i < m:
        
        if a2[i] not in dic.keys():
            return 'No'
        i += 1    
    
    return 'Yes'
    