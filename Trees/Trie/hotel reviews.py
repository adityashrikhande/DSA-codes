
class Node:
    def __init__(self, char=None):
        self.char = char
        self.neighbours = {}
        self.is_word = False
        
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie_root = Node()
        
        for word in A.split('_'):
            curr_tree_pos = trie_root
            for char in word:
                if char not in curr_tree_pos.neighbours:
                    curr_tree_pos.neighbours[char] = Node(char)
                
                curr_tree_pos = curr_tree_pos.neighbours[char]
            curr_tree_pos.is_word = True
        
        reviews_goodness = []
        for i, review in enumerate(B):
            goodness_score = 0
            for word in review.split('_'):
                curr_tree_pos = trie_root
                legal_candidate = True
                for char in word:
                    if char not in curr_tree_pos.neighbours:
                        legal_candidate = False
                        break
                    
                    curr_tree_pos = curr_tree_pos.neighbours[char]
                
                if legal_candidate and curr_tree_pos.is_word:
                    goodness_score += 1
            
            reviews_goodness.append((goodness_score, i))
            
        reviews_goodness.sort(key = lambda t: (t[0], len(reviews_goodness) - t[1]), reverse=True) # imp comparator
        
        return [t[1] for t in reviews_goodness]

