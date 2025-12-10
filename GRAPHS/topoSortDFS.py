from collections import defaultdict
n = 6
edges = [
  [5, 2],
  [5, 0],
  [4, 0],
  [4, 1],
  [2, 3],
  [3, 1]
]
d = defaultdict(list)
st = []
for i in edges:
    d[i[0]].append(i[1])
visited = [False]*n    
print(d)
def dfs(u):
    visited[u] = True
    for j in d[u]:
        if not visited[j]:
            dfs(j)
    st.append(u)
for i in range(n):
    if not visited[i]:
        dfs(i)
print(st[::-1])        
