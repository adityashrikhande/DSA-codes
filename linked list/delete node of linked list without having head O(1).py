
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Write your code here.
    node.data = node.next.data
    temp = node.next
    node.next = node.next.next
    temp.next = None