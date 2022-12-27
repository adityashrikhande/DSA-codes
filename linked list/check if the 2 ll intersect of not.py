
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findIntersection(firstHead, secondHead) :

	# write your code
    d = {}
    temp = firstHead
    while temp != None:
        d[temp] = 1
        temp = temp.next
    temp = secondHead
    while temp != None:
        if temp in d.keys():
            return temp.data
        temp = temp.next
    return -1
  
