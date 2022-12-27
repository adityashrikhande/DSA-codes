
# Brute force  O(N!*N)time  and O(N)space

def solve(s, index, res, n):
    if index == n:
        res.append(''.join(s))
        return

    for i in range(index, n):
        s[i], s[index] = s[index], s[i]
        solve(s, index + 1, res, n)
        s[i], s[index] = s[index], s[i]
      
    
def kthPermutation(n, k):
    
    s = ""
    res = []
    
    for i in range(1, n+1):
        s += str(i)
    
    n = len(s)

    solve(list(s), 0, res, n)
    
    res.sort()
    
    return res[k-1]

# Optimal O(N^2)time and O(N) space

def kthPermutation(n, k):
    
    ans = ""
    numbers = []
    fact = 1
    for i in range(1, n):
        fact = fact*i
        numbers.append(i)
    numbers.append(n)
    k = k-1
    while True:
        ans += str(numbers[k//fact])
        numbers.pop(k//fact)
        if len(numbers) == 0:
            break
        k = k%fact
        fact = fact//len(numbers)
    
    return ans
    
  