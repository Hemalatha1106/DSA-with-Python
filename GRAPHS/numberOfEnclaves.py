grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
n = len(grid)
m = len(grid[0])
visited = [[0]*m for _ in range(n)]
q = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                q.append([i,j])
                visited[i][j] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    f = q.pop(0)
    r = f[0]
    c = f[1]
    for i in range(4):
        cr = r+dx[i]
        cc = c+dy[i]
        if cr >= 0 and cr < n and cc >= 0 and cc < m and grid[cr][cc] == 1 and visited[cr][cc] == 0:
            q.append([cr,cc])
            visited[cr][cc] = 1
res = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            grid[i][j] = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            res += 1
print(res)         