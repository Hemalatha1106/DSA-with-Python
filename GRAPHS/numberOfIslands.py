#https://leetcode.com/problems/number-of-islands?envType=problem-list-v2&envId=depth-first-search
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
n = len(grid)
m = len(grid[0])
visited = [[0]*m for _ in range(n)]
def bfs(row,col):
    q = [[row,col]]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        f = q.pop(0)
        r = f[0]
        c = f[1]
        for k in range(4):
            cr = r+dx[k]
            cc = c+dy[k]
            if cr >= 0 and cr < n and cc >= 0 and cc < m and visited[cr][cc] == 0 and grid[cr][cc] == "1":
                visited[cr][cc] = 1
                q.append([cr,cc])           
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "1" and visited[i][j] == 0:
            visited[i][j] = 1
            res += 1
            bfs(i,j)                 
print(res)            