
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        li = []
        
        for i in A:
            
            if len(li) == 0:
                li.append(i)
            
            elif li[len(li)-1] == '(' and i == ')':
                li.pop()
                
            else:
                li.append(i)
                
        if len(li) == 0:
            return 1
        else:
            return 0