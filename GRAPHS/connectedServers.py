grid = [[1,0],[1,1]]
def dfs(r,c,visited,n,m):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    st = [[r,c]]
    comp = 0
    visited[r][c] = 1
    while st:
        node = st.pop()
        comp += 1
        for i in range(4):
            cr = dx[i]+node[0]
            cc = dy[i]+node[1]
            if cr >= 0 and cr < n and cc>= 0 and cc < m and visited[cr][cc] == 0 and grid[cr][cc] == 1:
                st.append([cr,cc])
                visited[cr][cc] = 1
    return comp            
n = len(grid)
m = len(grid[0])
visited = [[0]*m for _ in range(n)]
res = 0
for row in range(n):
    for col in range(m):
        if visited[row][col] == 0 and grid[row][col] == 1:
            nodes = dfs(row,col,visited,n,m)
            res += nodes
print(res)            
