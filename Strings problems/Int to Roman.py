
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):

        temp = A

        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        integ = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        st_build = ""

        for i in range(len(integ)):
            while temp >= integ[i]:
                temp -= integ[i]
                st_build += roman[i]
        
        return st_build
