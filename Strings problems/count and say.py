
def writeAsYouSpeak(n):
    # Write your code here.
    ans = '1'
    if n == 1:
        return ans
    
    for i in range(1, n):
        cnt = 1
        char = ans[0]
        m = len(ans)
        st = ''
        for j in range(1, m):
            if ans[j] == ans[j-1]:
                cnt += 1
            else:
                st += str(cnt)+char
                char = ans[j]
                cnt = 1
        st += str(cnt)+char
        ans = st
    
    return ans
            