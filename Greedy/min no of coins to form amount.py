
def findMinimumCoins(amount):

	# Write your code here
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(coins)
    cnt = 0
    for i in range(n-1, -1, -1):
        while coins[i] <= amount:
            amount -= coins[i]
            cnt += 1
        if amount == 0:
            break
    
    return cnt