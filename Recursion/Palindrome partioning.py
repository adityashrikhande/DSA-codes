
def check(s, i, j):
    l = i
    r = j
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def party(i, n, s, ans, temp):
    
    if i == n:
        ans.append(temp[:])
    
    for idx in range(i, n):
        temp.append(s[i:idx+1])
        if check(s, i, idx):
            party(idx+1, n, s, ans, temp)
        temp.pop()
        
        
def partition(s):
    # Write your code here.
    ans = []
    temp = []
    n = len(s)
    party(0, n, s, ans, temp)
    return ans