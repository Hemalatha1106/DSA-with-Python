board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
n = len(board)
m = len(board[0])
visited = [[0]*m for i in range(n)]
mainQ = []
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            if board[i][j] == "O":
                visited[i][j] = 1
                mainQ.append([i,j])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while mainQ:
    r, c = mainQ.pop(0)
    for i in range(4):
        cr = r+dx[i]
        cc = c+dy[i]
        if cr >= 0 and cr < n and cc >= 0 and cc < m:
            if board[cr][cc] == "O" and visited[cr][cc] == 0:
                visited[cr][cc] = 1
                mainQ.append([cr,cc])
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            board[i][j] = "X"   
        else:
            board[i][j] = "O"
print(board)                            