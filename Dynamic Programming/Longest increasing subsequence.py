
# rec + memo

class Solution:
    
    #Function to find length of longest increasing subsequence.
    
    dp = [[-1 for i in range(1000)] for j in range(1000)]
    
    def lis(self, a, idx, prev):
        
        if idx == len(a):
            return 0
            
        if self.dp[idx][prev+1] != -1:
            return self.dp[idx][prev+1]
            
        le = self.lis(a, idx+1, prev)
            
        if prev == -1 or a[idx] > a[prev]:
            le = max(1 + self.lis(a, idx+1, idx), le)
            
        self.dp[idx][prev+1] = le
        
        return self.dp[idx][prev+1]
            
    
    def longestSubsequence(self,a,n):
        # code here
        
        for i in range(n+1):
            for j in range(n+1):
                self.dp[i][j] = -1

        return self.lis(a, 0, -1)

# Tabulation Dp        O(N*N)

class Solution:
    
    #Function to find length of longest increasing subsequence.
    
    
    def longestSubsequence(self,a,n):
        # code here
        
        lis = [1 for i in range(n)]
        maxi = 1
        
        for i in range(1,n):
            for j in range(i):
                
                if a[i] > a[j] and lis[i] <= lis[j]:
                    lis[i] = 1 + lis[j]
                
                maxi = max(maxi, lis[i])
        
        return maxi


# binary search only length calculation      O(n*log(n))

class Solution:
    
    #Function to find length of longest increasing subsequence.
    
    def binarysearch(self, temp, l, r, find):
        
        while l < r:
            
            mid = (l + r)//2
            
            if temp[mid] >= find:
                r = mid
            elif temp[mid] < find:
                l = mid+1
        return r
            
    
    def longestSubsequence(self,a,n):
        # code here
        
        temp = [a[0]]
        maxi = 1
        
        for i in range(1,n):
            
            if a[i] > temp[-1]:
                temp.append(a[i])
                maxi += 1
            else:
                idx = self.binarysearch(temp, 0, len(temp) - 1, a[i])
                temp[idx] = a[i]
        
        return maxi
            
       
       