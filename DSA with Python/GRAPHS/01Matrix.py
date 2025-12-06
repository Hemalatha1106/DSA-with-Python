matrix = [ [0,0,0],[0,1,0],[1,1,1] ]
n = len(matrix)
m = len(matrix[0])
q = []
visited = [[0]*m for i in range(n)]
res = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            q.append([[i,j],0])
            visited[i][j] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    f = q[0]
    r = f[0][0]
    c = f[0][1]
    s = f[1]
    q.pop(0)
    res[r][c] = s
    for i in range(4):
        if r+dx[i] >= 0 and r+dx[i] < n and c+dy[i] >= 0 and c+dy[i]<m and visited[r+dx[i]][c+dy[i]] == 0:
            q.append([[r+dx[i],c+dy[i]],s+1])
            visited[r+dx[i]][c+dy[i]] = 1
print(res)