#dfs implementation
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
n = len(graph)
visited = [-1 for i in range(n+1)]
def dfs(graph, c, visited, node):
    visited[node] = c
    for i in graph[node]:
        if visited[i] != -1:
            if visited[i] == c:
                return False
        else:
            if not dfs(graph, 1-c, visited, i):
                return False
    return True
for j in graph:
    if visited[j] == -1:
        if not dfs(graph, 0, visited, j):
            print("Not a Biparatite graph")
            exit()
print("Biparatite graph")               