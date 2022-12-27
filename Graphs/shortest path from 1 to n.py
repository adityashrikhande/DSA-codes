
class Solution:
    def minStep (self, n):
        #complete the function here
        
        cnt = 0
        
        temp = n
        
        while temp > 1:
            if temp%3 == 0:
                temp = temp//3
                cnt += 1
            else:
                temp -= 1
                cnt += 1
                
        return cnt