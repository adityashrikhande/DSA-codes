
# map of key -> sum and value -> index
# treating 0 as -1

class Solution:
    def maxLen(self, arr, n):
        # code here
        sum = 0
        ans = 0
        map = dict()
        map[0] = -1
        
        for i in range(n):
            
            if arr[i] == 0:
                sum += -1
            else:
                sum += 1
                
            if sum in map.keys():
                ans = max(ans, i - map[sum])
            else:
                map[sum] = i
                
        return ans