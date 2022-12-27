
def reverseString(str):
	#Write your code here.
    temp = ''
    n = len(str)
    for i in range(n-1, -1, -1):
        if str[i] != ' ' and (i == n-1 or str[i+1] == ' '):
            end = i
        if (str[i] == ' ' and i != n-1 and str[i+1] != ' '):
            temp += ' ' + str[i+1:end+1]
        if (str[i] != ' ' and i == 0):
            temp += ' ' + str[i:end+1]
    
    return temp[1:]