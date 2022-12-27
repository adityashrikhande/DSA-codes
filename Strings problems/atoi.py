
def atoi(str):
    # Write your code here.
    n = len(str)
    if n == 0:
        return 0
    ans = ''
    if str[0] == '-':
        ans += str[0]
    
    for i in range(n):
        if str[i] >= '0' and str[i] <= '9':
            ans += str[i]
    
    if len(ans) == 0 or (len(ans) == 1 and ans[0] == '-'):
        return 0
    return int(ans)