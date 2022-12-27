
def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit
    jobs = sorted(jobs, key = lambda x:x[1], reverse = True)
    n = len(jobs)
    profit = 0
    vis = [-1 for i in range(3001)]
    for i in range(n):
        for j in range(jobs[i][0], 0, -1):
            if vis[j] == -1:
                profit += jobs[i][1]
                vis[j] = i
                break
    return profit
            
    