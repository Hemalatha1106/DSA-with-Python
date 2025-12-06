#recursive method 
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
def dfs(graph,node,visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for n in graph[node]:
            dfs(graph,n,visited)
visited = set()
start = 1
dfs(graph,start,visited)            