
# retrun length of after removing duplicates

def removeDuplicates(arr,n):
    # Write your code here.
    i = 0
    j = 0
    while i < n:
        arr[i] = arr[j]
        while j < n and arr[j] == arr[i]:
            j += 1
        i += 1
        if j == n:
            break
    
    return i
        