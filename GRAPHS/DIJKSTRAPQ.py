from collections import defaultdict
import heapq
n = 5
m= 6
edges = [[0,1,2], [0,2,4], [1,2,1], [1,3,7], [2,4,3], [4,3,2]]
d = defaultdict(list)
for i,j,w in edges:
    d[i].append([j,w])
    d[j].append([i,w])
dist = [float('inf')]*n
dist[0] = 0
pq = [[0,0]]
while pq:
    curdis,node = heapq.heappop(pq)
    if curdis > dist[node]:
        continue
    for nei, w in d[node]:
        if curdis+w < dist[nei]:
            dist[nei] = curdis+w
            heapq.heappush(pq,[curdis+w,nei]) 
print(dist)            


