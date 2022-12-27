
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.isend = True
        
    def getprefix(self, word):
        node = self.root
        prefi = ''
        for char in word:
            if node.count == 1:
                break
            else:
                prefi += char
            node = node.children[char]
            
        return prefi
        

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        
        ans = []
        
        trie = Trie()
      
        for word in A:                 
            trie.insert(word)
            
        for word in A:
            ans.append(trie.getprefix(word))
            
        return ans 
        
