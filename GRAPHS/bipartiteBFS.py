graph = {0:[1,3],1:[0,2],2:[1,3],3:[0,2]}
visited = [-1]*len(graph)
for i in graph:
    if visited[i] == -1:
        q = [i]
        visited[i] = 0
        while q:
            node = q.pop(0)
            for j in graph[node]:
                if visited[j] == -1:
                    visited[j] = 1-visited[node]
                    q.append(j)
                else:
                    if visited[j] == visited[node]:
                        print(False)
                        exit()
print(True)                        


