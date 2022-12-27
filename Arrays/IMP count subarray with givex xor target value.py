
def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    freq = {}
    cnt = 0
    xor = 0
    n = len(arr)
    for i in range(n):
        xor ^= arr[i]
        if xor == x:
            cnt += 1
        if (xor ^ x) in freq.keys():
            cnt += freq[xor^x]
            
        if (xor) in freq.keys():
            freq[xor] += 1
        else:
            freq[xor] = 1
            
    return cnt
        