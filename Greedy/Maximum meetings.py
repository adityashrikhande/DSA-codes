
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here


        meet = []
        n = len(start)
        for i in range(n):
            meet.append([end[i], start[i], i+1])
        meet.sort()
        
        ans = []
        i = 0
        ans.append(meet[0][2])
        end = meet[0][0]
        for i in range(1, n):
            if meet[i][1] > end:
                ans.append(meet[i][2])
                end = meet[i][0]
            i += 1
        
        #ans.sort()
        return len(ans)
