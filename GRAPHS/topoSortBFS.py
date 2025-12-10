n = 6
edges = [
  [5, 2],
  [5, 0],
  [4, 0],
  [4, 1],
  [2, 3],
  [3, 1]
]
q = []
adj = [[] for _ in range(n)]
indegree = [0]*n
for u,v in edges:
    adj[u].append(v)
    indegree[v] += 1
for i in range(n):
    if indegree[i] == 0:
        q.append(i)
topo = []
while q:
    u = q.pop(0)
    topo.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
if len(topo) != n:
    print("Cyclic, topo doesn't exists")
else:
    print(topo)
                                