
def permu(s, n, idx, ans):
    if idx == n:
        ans.append(''.join(s))
        return
    for i in range(idx, n):
        s[i], s[idx] = s[idx], s[i]
        permu(s, n, idx+1, ans)
        s[i], s[idx] = s[idx], s[i]

def findPermutations(s):
    # Write your code here.
    ans = []
    n = len(s)
    
    permu(list(s), n, 0, ans)
    
    return ans