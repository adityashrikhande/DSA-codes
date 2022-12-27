
def modularExponentiation(x, n, m):   # m = MOD
	# Write your code here.
    ans = 1
    temp = n
    while temp:
        if temp%2 == 0:
            x *= x%m
            temp //= 2
        else:
            ans *= x%m
            temp -= 1
            
    return ans%m