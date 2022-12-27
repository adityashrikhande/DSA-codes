
# O(N^2) time O(1) space (neglecting ans space) 

class Solution(object):
    def threeSum(self, arr):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(arr)
        arr.sort()
        ans = []
        i = 0
        while i < n-2:
            left = i+1
            right = n-1
            while left < right:
                if arr[i]+arr[left]+arr[right] == 0:
                    a = arr[i]
                    b = arr[left]
                    c = arr[right]
                    temp = [a,b,c]
                    ans.append(temp)
                    while left < right and arr[left+1] == b:
                        left += 1
                    while right > left and arr[right-1] == c:
                        right -= 1
                    left += 1
                    right -= 1        
                elif arr[i]+arr[left]+arr[right] < 0:
                    left += 1
                else:
                    right -= 1
            while i+1 < n and arr[i] == arr[i+1]:
                i += 1
            i += 1

        return ans