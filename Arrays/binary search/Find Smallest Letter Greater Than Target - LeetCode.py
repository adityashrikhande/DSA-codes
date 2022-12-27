
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        
        
        if letters[r] <= target or letters[0] > target:
            return letters[0]
        
        while l < r:
            mid = l + (r-l)//2
            
            if letters[mid] <= target:
                l = mid + 1
            elif letters[mid] > target:
                r = mid
        
                    
        return letters[r]
                