
def solve(matrix, r, c, sub):
    
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                for ele in range(1,10):
                    a = (row//3)*3
                    b = (col//3)
                    if r[row][ele] == 0 and c[ele][col] == 0 and sub[a+b][ele] == 0:
                        matrix[row][col] = ele
                        r[row][ele] = 1
                        c[ele][col] = 1
                        sub[a+b][ele] = 1
                    
                        if solve(matrix, r, c, sub):
                            return True
                        
                        matrix[row][col] = 0
                        r[row][ele] = 0
                        c[ele][col] = 0
                        sub[a+b][ele] = 0
                return False
    return True


def isItSudoku(matrix):

    # Write your code here.
    r = [[0 for i in range(10)] for j in range(10)]
    c = [[0 for i in range(10)] for j in range(10)]
    sub = [[0 for i in range(10)] for j in range(10)]
    
    for row in range(9):
        for col in range(9):
            r[row][matrix[row][col]] = 1
    for row in range(9):
        for col in range(9):
            c[matrix[row][col]][col] = 1
    for row in range(9):
        for col in range(9):
            a = (row//3)*3
            b = (col//3)
            sub[a+b][matrix[row][col]] = 1
    
    return solve(matrix, r, c, sub)
    