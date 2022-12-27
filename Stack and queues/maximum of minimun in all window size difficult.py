
def maxMinWindow(a, n):
    # Write your code here
    # Return a list of integers
    stack = []  

    #using arrays to store previous and next smaller numbers.
    left = [-1 for i in range(n)]
    right = [n for i in range(n)] 

    #filling elements of left[] using logic discussed in 
    #next greater element problem.
    for i in range(n):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            left[i] = stack[-1]
        stack.append(i)

    #emptying the stack as stack is going to be used for right[].
    stack = []

    #filling elements of right[] using same logic.
    for i in range(n-1,-1,-1):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            right[i] = stack[-1]
        stack.append(i)

    #creating and initializing answer list.
    ans= [-1*1e9 for i in range(n+1)]

    #filling answer list by comparing minimums of all
    #lengths computed using left[] and right[].
    for i in range(n):
        
        #length of the interval.
        length = right[i]-left[i]-1
        
        #a[i] is a possible answer for this length 'length' interval,
        #check if a[i] is more than max for 'length'.
        ans[length] = max(ans[length],a[i])

    #some entries in ans[] may not be filled yet. Filling
    #them by taking values from right side of ans[].
    for i in range(n-1,-1,-1):
        ans[i] = max(ans[i],ans[i+1])

    #returning the answer list.
    return ans[1:]