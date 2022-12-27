
# O(logn)

def uniqueElement(arr, n):
    # Write your code here
    low = 0
    high = n-2
    while low <= high:
        mid = (low+high)//2
        if mid%2 == 0:
            if arr[mid] == arr[mid+1]:
                low = mid+1
            else:
                high = mid-1
        else:
            if arr[mid] == arr[mid+1]:
                high = mid-1
            else:
                low = mid+1
    
    return arr[low]
