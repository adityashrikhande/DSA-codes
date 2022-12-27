
def minCharsforPalindrome(str):

    # Write your code here
    cnt = 0
    n = len(str)
    i = n-1
    while i > 0:
        if str[i] != str[0]:
            i -= 1
            cnt += 1
        else:
            k = i
            j = 0
            while k > j and str[j] == str[k]:
                j += 1
                k -= 1
            
            if j >= k:
                return cnt
            else:
                i -= 1
                cnt += 1
    return cnt