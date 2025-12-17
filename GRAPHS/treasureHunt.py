from collections import defaultdict
n = 8
edges = [[0,1],[1,2],[2,3],[4,5],[5,6],[6,4],[7,3]]
treasures = [0,5]
def dfs(node,graph,visited):
    visited[node] = True
    comp = []
    st = [node]
    while st:
        cur = st.pop()
        comp.append(cur)
        for nei in graph[cur]:
            if not visited[nei]:
                visited[nei] = True
                st.append(nei)
    return comp
graph = defaultdict(list)
visited = [False]*(n+1)  
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
res = 0    
for n in range(len(treasures)):
    if not visited[treasures[n]]:
        nodes = dfs(treasures[n],graph,visited)
        res += len(list(set(nodes)))
print(res)
      