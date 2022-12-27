
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        
        od = OrderedDict()
        
        for i in range(n):
            
            od[s[i]] = 0
           
        for i in range(n):
            
            od[s[i]] += 1
           
        for i in range(n):
            
            if od[s[i]] == 1:
                return i
        
        return -1
                
                