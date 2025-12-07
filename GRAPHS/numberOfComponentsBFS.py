graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3]
}
n = 5
visited = [-1]*n
res = 0
for i in graph:
    if visited[i] == -1:
        visited[i] = 1
        q = [i]
        while q:
            node = q.pop(0)
            for j in graph[node]:
                if visited[j] == -1:
                    visited[j] = 1
                    q.append(j)
        res += 1
print(res)        