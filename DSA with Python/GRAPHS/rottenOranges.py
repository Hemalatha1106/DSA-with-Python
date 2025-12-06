grid = [ [2,1,1] , [0,1,1] , [1,0,1] ]
q = []
total = 0
n = len(grid)
m = len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            q.append((i,j))
        if grid[i][j] != 0:
            total+=1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cur_cnt = 0
time = 0
while q:
    s = len(q)
    cur_cnt += s
    for i in range(s):
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != 1:
                continue
            grid[nx][ny] = 2
            q.append((nx,ny))
    if q:
        time += 1
print(time if cur_cnt == total else -1)               
            

