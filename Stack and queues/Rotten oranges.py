
def minTimeToRot(grid, n, m):

    # Write your code here.
    rotten = 0
    fresh = 0
    q = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                rotten += 1
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    if fresh == 0 or rotten == 0:
        return 0
    
    min = 0
    q2 = []
    while True:
        while len(q) != 0:
            temp = q.pop()
            i = temp[0]
            j = temp[1]
            if i > 0 and grid[i-1][j] == 1:
                q2.append((i-1, j))
                grid[i-1][j] = 2
                fresh -= 1
            if j > 0 and grid[i][j-1] == 1:
                q2.append((i, j-1))
                grid[i][j-1] = 2
                fresh -= 1
            if i < n-1 and grid[i+1][j] == 1:
                q2.append((i+1, j))
                grid[i+1][j] = 2
                fresh -= 1
            if j < m-1 and grid[i][j+1] == 1:
                q2.append((i, j+1))
                grid[i][j+1] = 2
                fresh -= 1
        q = q2
        if len(q2) == 0:
            if fresh > 0:
                return -1
            break
        q2 = []
        min += 1
        
    return min