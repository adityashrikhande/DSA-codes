# leetcode link
# https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://leetcode.com/problems/sqrtx/%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1654058799432051%26amp;usg%3DAOvVaw3fpJimfC4ZzIgvS4_Ej88J&sa=D&source=docs&ust=1654058799494873&usg=AOvVaw0fVwpaHBpYyxbMqrz2Xvuv

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = 1
        r = x
        while l <= r:
            mid = l + (r-l)//2
            
            if mid*mid == x:
                return mid
            
            if mid*mid > x:
                r = mid - 1
            if mid*mid < x:
                l = mid + 1
                ans = mid
                
        return ans
        