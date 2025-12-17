from collections import defaultdict
n = 8
edges = [[0,1],[1,2],[3,4],[4,5],[5,3],[6,7]]
secret = [2, 5]
s = set(secret)
def dfs(node,graph,visited):
    visited[node] = True
    st = [node]
    comp = []
    while st:
        cur = st.pop()
        comp.append(cur)
        for nei in graph[cur]:
            if not visited[nei]:
                st.append(nei)
                visited[nei] = True
    return comp
visited = [False]*(n+1)
graph = defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
seen = 0    
for i in range(len(secret)):    
    nodes = dfs(secret[i],graph,visited)
    for n in nodes:
        if n in s:
            seen += len(nodes)
            break
print(seen)        
