
class Solution:
    def nthFibonacci(self, n):
        # code here 
        
        a = [0 for i in range(n+1)]
        
        if n <= 1:
            return n
        
        a[0] = 0
        a[1] = 1
        
        for i in range(2, n+1):
            a[i] = (a[i-1] + a[i-2])%(1e9 + 7)
            
        return int(a[n])
        
        