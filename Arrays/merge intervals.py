
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        
        n = len(intervals)
        
        if n == 1:
            return intervals
        
        lis = intervals
        
        i = 1
        while i < len(lis):
            if lis[i][0] <= lis[i-1][1]:
                lis[i-1][1] = max(lis[i-1][1], lis[i][1])
                lis.pop(i)
            else:
                i += 1
        
        print(intervals, lis)
                
        return lis
            
        