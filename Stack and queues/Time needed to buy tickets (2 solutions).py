
# Note: There are 2 solutions one with queue and one with simple iteration
# Note: There are 2 solutions one with queue and one with simple iteration
# Note: There are 2 solutions one with queue and one with simple iteration

class Solution:
    """
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        temp = tickets[k]
        tickets[k] = (-1) * tickets[k]
        q = deque(tickets)
        i = 0
        time = 0
        
        while i < temp-1:
            
            for j in range(len(q)):
                
                if q[0] < 0:
                    time += 1
                    q.append(q.popleft()+1)
            
                elif q[0] == 0:
                    q.append(q.popleft())
                    
                else:
                    time += 1
                    q.append(q.popleft()-1)
                    
            i += 1
            
        for i in range(len(q)):
            
            if q[0] != 0:
                time += 1
            
            if q[0] == -1:
                #print ('yes')
                break
                
            q.popleft()
                
        return time
    """
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        time = 0
        find = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                
                if tickets[i] <= find:
                    time += tickets[i]
                else:
                    time += find
            else:
                if tickets[i] < find:
                    time += tickets[i]
                else:
                    time += find-1
            
        
        return time
    
    