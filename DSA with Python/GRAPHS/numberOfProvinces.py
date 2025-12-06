from collections import defaultdict
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
adjLs = defaultdict(set)
for i in range(len(isConnected)):
    for j in range(len(isConnected[i])):
        if isConnected[i][j] == 1:
            adjLs[i].add(j)
            adjLs[j].add(i)
print(adjLs)    
def dfs(graph,node,visited):
    # if node not in visited:#<-----also checking here, that actually no need. so maintain one check.
    visited.add(node) 
    res.append(node)   
    for n in graph[node]:
        if n not in visited:
            dfs(graph,n,visited)
visited = set()
res = []
c = 0
for k in range(len(isConnected)):           
    if k not in visited:#<---- checking here
        c += 1
        dfs(adjLs,k,visited)
print(res)
print(c)        