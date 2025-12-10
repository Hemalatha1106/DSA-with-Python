numCourses = 2
prerequisites = [[1,0]]
q = []
topo = []
adj = [[] for i in range(numCourses)]
indegree = [0]*numCourses
for u, v in prerequisites:
    adj[u].append(v)
    indegree[v] += 1
for j in range(len(adj)):
    if indegree[j] == 0:
        q.append(j)
while q:
    u = q.pop(0)
    topo.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
if len(topo) != numCourses:
    print(False)
else:
    print(True)   
print(topo[::-1])                           