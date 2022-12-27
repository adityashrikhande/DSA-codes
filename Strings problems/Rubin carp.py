
def stringMatch(str, pat):

    # Write your code here
    # Return a list denoting the answer to the problem
    n = len(pat)
    m = len(str)
    ans = []
    j = n
    for i in range(m):
        if j <= m and str[i:j] == pat:
            ans.append(i)
        if j == m:
            break
        j += 1
    
    return ans

# using hash value reducing the comparison of str and pat

def stringMatch(str, pat):

    # Write your code here
    # Return a list denoting the answer to the problem
    n = len(pat)
    m = len(str)
    ans = []
    j = n
    com = 0
    che = 0
    for i in range(n):
        com += ord(pat[i])*(26**(n-i-1))   # increasing complexity of hash function
        che += ord(str[i])*(26**(n-i-1))
    j = n
    for i in range(m):
        if che == com and str[i:j] == pat:
            ans.append(i)
        
        if j < m:
            che = (che-ord(str[i])*(26**(j-i-1)))*26 + ord(str[j])*(26**(0))   # rolling hash
            
        j += 1
        
    return ans