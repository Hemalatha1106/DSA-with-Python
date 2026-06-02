from collections import defaultdict
import heapq
n = 4
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (2, 3, 1)
]
graph=defaultdict(list)
for i,j,w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))
pq=[(0,0,-1)]#weight,node,parent
visited=set()
mst=[]
cost=0
while pq:
    wt,node,parent=heapq.heappop(pq)
    if node in visited:
        continue
    visited.add(node)
    cost+=wt
    if parent!=-1:
        mst.append((parent,node,wt))
    for nei,weight in graph[node]:
        if nei not in visited:
            heapq.heappush(pq,(weight,nei,node))
print(cost)                