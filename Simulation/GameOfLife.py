board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
n = len(board)
m = len(board[0])
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def categoryZero(board,r,c):
    alive_count = 0
    for k in range(8):
        row = r+dx[k]
        col = c+dy[k]
        if row >= 0 and row < n and col >= 0 and col < m:
            if board[row][col] == 1:
                alive_count += 1
    return alive_count == 3
def categoryOne(board,r,c):
    alive_count = 0
    for k in range(8): 
        row = r+dx[k]
        col = c+dy[k]
        if row >= 0 and row < n and col >= 0 and col < m:
            if board[row][col] == 1:
                alive_count += 1
    if alive_count < 2 or alive_count > 3:
        return False
    return True    
boardCopy = [a[:] for a in board]                               
for i in range(n):
    for j in range(m):
        if boardCopy[i][j] == 0:
            if categoryZero(boardCopy,i,j):
                board[i][j] = 1
        else:
            if not categoryOne(boardCopy,i,j):
                board[i][j] = 0
print(board)                