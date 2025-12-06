graph = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7]
}
def detectCycle(curr,graph,visited):
    q = []
    visited[curr] = True
    q.append((curr,-1))
    while q:
        node = q[0][0]
        parent = q[0][1]
        q.pop(0)
        for neighbour in graph[node]:
            if visited[neighbour] == False:
                visited[neighbour] = True
                q.append((neighbour,node))
            elif neighbour != parent:
                return True
    return False
visited = [False]*(len(graph)+1)
for i in range(1,len(graph)+1):
    if visited[i] == False:
        if detectCycle(i,graph,visited):
            print(True)
            exit()
print(False)            

