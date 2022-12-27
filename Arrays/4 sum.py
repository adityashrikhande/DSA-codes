
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        
        nums.sort()
        
        for i in range(0, n-3, 1):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n-2, 1):
                
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        
                        a = nums[i]
                        b = nums[j]
                        c = nums[left]
                        d = nums[right]
                        
                        temp = [a, b, c, d]
                        ans.append(temp)
                        
                        while left < right and nums[left] == temp[2]:
                            left += 1
                        while left < right and nums[right] == temp[3]:
                            right -= 1
                        
                           
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                        
                    else:
                        right -= 1
                
        return ans
                        
                    