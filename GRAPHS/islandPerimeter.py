#https://leetcode.com/problems/island-perimeter?envType=problem-list-v2&envId=depth-first-search
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
n = len(grid)
m = len(grid[0])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            t = 4
            for k in range(4):
                row = i+dx[k]
                col = j+dy[k]
                if row >= 0 and row < n and col >= 0 and col < m and grid[row][col] == 1:
                    t -= 1
            res += t
print(res)

