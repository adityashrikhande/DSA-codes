
def compareVersions(a, b):
    #Write your code here
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n or j < m:
        st1 = ''
        st2 = ''
        while i < n and a[i] != '.':
            st1 += a[i]
            i += 1
        while j < m and b[j] != '.':
            st2 += b[j]
            j += 1
        i += 1
        j += 1
        if len(st1) == 0:
            st1 = '0'
        if len(st2) == 0:
            st2 = '0'
        if int(st1) > int(st2):
            return 1
        if int(st1) < int(st2):
            return -1
        
    return 0