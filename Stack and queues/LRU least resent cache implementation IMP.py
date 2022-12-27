
from sys import stdin

class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

first = Node([-1, -1])
tail = Node([-1, -1])
first.next = tail
tail.prev = first   

def delnode(node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def addnode(node):
    nex = first.next
    first.next = node
    node.prev = first
    nex.prev = node
    node.next = nex

class LRUCache:
    # Initialize the LRU Cache
    def __init__(self, capacity):
        # Your code goes here
        self.capacity = capacity
        self.cnt = 0
        self.d = {}
        
    def get(self, key):
        # Your code goes here
        if key not in self.d.keys():
            return -1
        else:
            ad = self.d[key]
            delnode(ad)
            addnode(ad)
            
            return ad.data[1]
    
    def put(self, key, value):
        # Your code goes here
        if key in self.d.keys():
            ad = self.d[key]
            ad.data[1] = value
            delnode(ad)
            addnode(ad)
        else:
            if self.cnt == self.capacity:
                del self.d[tail.prev.data[0]]
                delnode(tail.prev)
                nd = Node([key, value])
                addnode(nd)
                self.d[key] = nd
                
            else:
                nd = Node([key, value])
                addnode(nd)
                self.d[key] = nd
                self.cnt += 1
              
# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
	query = list(map(int, stdin.readline().rstrip().split()))

	if query[0] == 0:
		key = query[1]
		print(cache.get(key))
	elif query[0] == 1:
		key = query[1]
		value = query[2]
		cache.put(key, value)
	
	q -= 1