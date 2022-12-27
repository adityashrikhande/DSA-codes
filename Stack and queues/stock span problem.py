
def findSpans(price):
    # Write your code here.
    st = []
    n = len(price)
    ans = [0 for i in range(n)]

    for i in range(n):
        while len(st) != 0 and price[st[-1]] <= price[i]:
            st.pop()
        if len(st) == 0:
            ans[i] = i+1
        else:
            ans[i] = i-st[-1]
        st.append(i)
    
    return ans