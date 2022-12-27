
def areAnagram(str1, str2):
    # Write your code here.
    n = len(str1)
    m = len(str2)
    
    if n != m:
        return False
    
    h1 = [0]*257
    h2 = [0]*257
    
    for i in range(n):
        h1[ord(str1[i])] += 1
            
    for i in range(n):
        h2[ord(str2[i])] += 1
    
    for i in range(257):
        if h1[i] != h2[i]:
            return False

    return True