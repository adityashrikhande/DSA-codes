
def uniqueSubstrings(st):
    # Write your code here.
    n = len(st)
    l = 0
    r = 0
    char = [0 for i in range(26)]
    ans = 0
    
    while r <= l and l < n:
        if char[ord(st[l])-97] == 0:
            ans = max(ans, l+1-r)
        else:
            while r < l and char[ord(st[l])-97] != 0:
                char[ord(st[r])-97] -= 1
                r += 1       
        char[ord(st[l])-97] += 1
        l += 1
    
    return ans
        