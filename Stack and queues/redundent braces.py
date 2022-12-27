
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):

        li = []
        op = ['(', ')', '+', '-', '/', '*']
        
        for i in A:    
            if i in op:    
                if len(li) == 0:
                    li.append(i)
                elif i == ')':
                    if li[len(li) - 1] == '(':
                        return 1
                    else:
                        while li[len(li)-1] > 0:
                            if li[len(li) - 1] != '(':
                                li.pop()
                            else:
                                li.pop()
                                break
                else:
                    li.append(i)
                    
        return 0