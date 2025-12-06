image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1 
color = 2
start = image[sr][sc]
n = len(image)
m = len(image[0])
q = []
q.append((sr,sc))
image[sr][sc] = color
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    s = len(q)
    for i in range(s):
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or image[nx][ny]!=start:
                continue
            image[nx][ny] = color 
            q.append((nx,ny))
print(image)