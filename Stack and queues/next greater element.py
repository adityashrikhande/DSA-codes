
# ans for taking arr circular 

def nextGreater(arr,n):
    
    #Your code goes here
    st = []
    ans = [0]*n
    for i in range(2*n-1, -1, -1):
        while len(st) != 0 and st[-1] <= arr[i%n]:
            st.pop()
        if i < n:
            if len(st) != 0:
                ans[i] = st[-1]
            else:
                ans[i] = -1
        
        st.append(arr[i%n])
    return ans

# without circular

def nextGreater(arr,n):
    #Your code goes here
    st = []
    ans = [0]*n
    for i in range(n-1, -1, -1):
        while len(st) != 0 and st[-1] <= arr[i]:
            st.pop()
        
        if len(st) != 0:
            ans[i] = st[-1]
        else:
            ans[i] = -1
        
        st.append(arr[i])
    return ans