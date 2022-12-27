
# O(N)time O(1)space

def getTrappedWater(arr, n) :
    # Write your code here.
    left = 0
    right = n-1
    lmax = arr[0]
    rmax = arr[n-1]
    ans = 0
    
    while left < right:
        lmax = max(lmax, arr[left])
        rmax = max(rmax, arr[right])
        if lmax < rmax:
            ans += lmax - arr[left]
            left += 1
        else:
            ans += rmax - arr[right]
            right -= 1
    
    return ans
            