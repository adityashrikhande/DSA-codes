
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        
        q1 = [A]
        q2 = []
        levellist = []
        flag = 1
        finallist = [[A.val]]
        
        while len(q1) != 0:
            
            node = q1[0]
            q1.pop(0)
            
            if node.left != None:
                q2.append(node.left)
                levellist.append(node.left.val)
            if node.right != None:
                q2.append(node.right)
                levellist.append(node.right.val)
                
            if len(q1) == 0:
                
                q1 = q2[:]
                
                if flag == 0:
                    flag = 1
                    if len(levellist) > 0:
                        finallist.append(levellist)
                else:
                    flag = 0
                    left = 0
                    right = len(levellist)-1
                    
                    while left < right:
                        levellist[left], levellist[right] = levellist[right], levellist[left]
                        left += 1
                        right -= 1
                      
                    if len(levellist) > 0:
                        finallist.append(levellist)
                
                q2 = []
                levellist = []
                    
        flag = 0
               
        return finallist