
def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    d = {}
    sum = 0
    d[sum] = -1
    n = len(arr)
    
    ans = 0
    
    for i in range(n):
        sum += arr[i]
        if sum in d.keys():
            ans = max(ans, i-d[sum])
        else:
            d[sum] = i
    
    return ans