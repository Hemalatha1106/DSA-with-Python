import heapq
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
visited=set()
cost=0
pq=[(0,0)]
while pq:
    wt,node=heapq.heappop(pq)
    if node in visited:
        continue
    cost+=wt
    visited.add(node)
    point1=points[node]
    for nei in range(len(points)):
        if nei not in visited:
            point2=points[nei]
            d=abs(point2[0]-point1[0])+abs(point1[1]-point2[1])
            heapq.heappush(pq,(d,nei))
print(cost)            

    