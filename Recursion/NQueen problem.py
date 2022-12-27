
def issafe(row, col, board, n):
    drow = row
    dcol = col
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1
        
    row = drow
    col = dcol
    while row >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
    
    row = drow
    col = dcol
    while col < n and row >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

def Queen(row, ans, board, n):
    if row == n:
        temp = []
        for i in range(n):
            temp.extend(board[i])
        ans.append(temp)
        return
    for col in range(n):
        if issafe(row, col, board, n):
            board[row][col] = 1
            Queen(row+1, ans, board, n)
            board[row][col] = 0
    
def solveNQueens(n):
    # Write your code here.
    if n == 1:
        return [[1]]
    if n <= 3:
        return []
    
    ans = []
    board = [[0 for i in range(n)] for j in range(n)]
    
    Queen(0, ans, board, n)
    
    return ans

    

# Optimal hashing to search safe square

def Queen(row, ans, board, n, up, upleft, upright):
    if row == n:
        temp = []
        for i in range(n):
            temp.extend(board[i])
        ans.append(temp)
        return
    for col in range(n):
        if up[col] == 0 and upleft[(n-1)+(col-row)] == 0 and upright[row + col] == 0:
            board[row][col] = 1
            up[col] = 1
            upleft[(n-1)+(col-row)] = 1
            upright[row + col] = 1
            Queen(row+1, ans, board, n, up, upleft, upright)
            board[row][col] = 0
            up[col] = 0
            upleft[(n-1)+(col-row)] = 0
            upright[row + col] = 0
    
def solveNQueens(n):
    # Write your code here.
    if n == 1:
        return [[1]]
    if n <= 3:
        return []
    
    ans = []
    board = [[0 for i in range(n)] for j in range(n)]
    upleft = [0 for i in range(2*n-1)]
    upright = [0 for i in range(2*n-1)]
    up = [0 for i in range(n)]
    Queen(0, ans, board, n, up, upleft, upright)
    
    return ans