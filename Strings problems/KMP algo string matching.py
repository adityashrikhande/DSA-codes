
# O(N + M) time

def findPattern(pat:str, str:str):
    # Write your code here.
    m = len(pat)
    n = len(str)
    prefix = [0]*m
    i = 1
    for i in range(1, m):
        j = prefix[i-1]
        while j > 0 and pat[j] != pat[i]:
            j = prefix[j-1]
        if pat[i] == pat[j]:
            j += 1
        prefix[i] = j
    #print(che)
    #return 1
    j = 0
    i = 0
    cnt = 0
    while i < n:           
        if str[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = prefix[j-1]
        if j == m:
            return True
    
    return False
            