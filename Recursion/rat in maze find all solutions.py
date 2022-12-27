
def solve(row, col, maze, ans, vis, n):
    if row == n-1 and col == n-1:
        vis[row][col] = 1
        temp = []
        for r in range(n):
            temp.extend(vis[r])
        ans.append(temp)
        return
    if row == n or col == n or row == -1 or col == -1 or vis[row][col] == 1:
        return
    if maze[row][col] == 0:
        return
    vis[row][col] = 1
    solve(row+1, col, maze, ans, vis, n)
    solve(row-1, col, maze, ans, vis, n)
    solve(row, col+1, maze, ans, vis, n)
    solve(row, col-1, maze, ans, vis, n)
    vis[row][col] = 0
    
    
def ratInAMaze(maze, n):
    # Write your code here.
    if maze[n-1][n-1] == 0 or maze[0][0] == 0:
        return []
    vis = [[0 for i in range(n)] for j in range(n)]
    ans = []
    solve(0, 0, maze, ans, vis, n)
    ans.sort()
    for i in ans:
        for j in i:
            print(j, end = " ")
        print()
