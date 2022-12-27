def largestRectangle(arr):
    # Write your code here.
    st = [0]
    n = len(arr)
    larr = [0]*n
    rarr = [n-1]*n
    
    for i in range(1, n):
        while len(st) != 0 and arr[st[-1]] >= arr[i]:
            st.pop()
        if len(st) == 0:
            larr[i] = 0
        else:
            larr[i] = st[-1] + 1
        st.append(i)
    
    st = [n-1]
    for i in range(n-1, -1, -1):
        while len(st) != 0 and arr[st[-1]] >= arr[i]:
            st.pop()
        if len(st) == 0:
            rarr[i] = n-1
        else:
            rarr[i] = st[-1]-1
        st.append(i)
    ans = 0
    for i in range(n):
        ans = max(ans, (rarr[i] - larr[i] + 1)*arr[i])
    
    return ans

# optimised

def largestRectangle(arr):
    # Write your code here.
    st = []
    n = len(arr)
    ans = 0
    for i in range(0, n+1):
        while len(st) != 0 and (i == n or arr[st[-1]] >= arr[i]):
            temp = st.pop()
            wid = 0
            if len(st) == 0:
                wid = i
            else:
                wid = i - st[-1] - 1
            ans = max(ans, wid*arr[temp])
        st.append(i)
    
    return ans
            