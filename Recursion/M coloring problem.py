
def issafe(node, mat, col, color, n):
    for i in range(n):
        if mat[i][node] == 1 and color[i] == col:
            return False
    return True

def solve(node, mat, n, color, m):
    if node == n:
        return True
    for col in range(1, m+1):
        if issafe(node, mat, col, color, n):
            color[node] = col
            if solve(node+1, mat, n, color, m):
                return True
            color[node] = 0
    return False
            

def graphColoring(mat,m):
    
    #Your code goes here
    n = len(mat)
    color = [0 for i in range(n)]
    if solve(0, mat, n, color, m):
        return 'YES'
    else:
        return 'NO'
