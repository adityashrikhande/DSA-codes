
def romanToInt(s):

    # Write your code here
    # Return the int value
    d = {}
    d['I'] = 1
    d['V'] = 5
    d['X'] = 10
    d['L'] = 50
    d['C'] = 100
    d['D'] = 500
    d['M'] = 1000
    d['IV'] = 4
    d['XL'] = 40
    d['XC'] = 90
    d['CD'] = 400
    d['CM'] = 900
    d['IX'] = 9
    
    ans = 0
    n = len(s)
    i = 0
    while i < n:
        if i+2 <= n and s[i: i+2] in d.keys(): 
            ans += d[s[i: i+2]]
            i += 1
        else:
            ans += d[s[i]]
        i += 1
    
    return ans
    