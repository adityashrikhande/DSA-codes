
def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
    items = sorted(items, key = lambda x: x[1]/x[0], reverse = True)
    #print(items)
    value = 0
    i = 0
    while w > 0 and i < n:
        if items[i][0] <= w:
            w -= items[i][0]
            value += items[i][1]
        else:
            value += (items[i][1]/items[i][0])*w
            w = 0
        i += 1
    
    return value         #"{:.2f}".format(value)