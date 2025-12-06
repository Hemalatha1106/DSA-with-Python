grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
n = len(grid)
m = len(grid[0])
visited = [[0]*m for _ in range(n)]

def dfs(r, c):
    visited[r][c] = 1
    # 4 directions
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)

# Step 1: DFS from all boundary 1s
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if visited[i][j] == 0:
                    dfs(i, j)

# Step 2: convert all visited land to 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            grid[i][j] = 0

# Step 3: count remaining 1s
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            res += 1

print(res)
