
def solve(idx, s, di, sen, ans, n):
    if idx == n:
        ans.append(' '.join(sen))
        return
    for i in range(idx, n):
        if s[idx:i+1] in di:
            sen.append(s[idx:i+1])
            solve(i+1, s, di, sen, ans, n)
            sen.pop()

def wordBreak(s, di):

    # Write your code here
    n = len(s)
    sen = []
    ans = []
    solve(0, s, di, sen, ans, n)
    return ans
