from collections import deque
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
start = 1
queue = deque([1])
res = []
visited = set()
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        res.append(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
print(res)                
