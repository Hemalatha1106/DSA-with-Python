from collections import defaultdict
e=5
v=7
edges = [[1, 2] ,[7, 2], [3, 5], [3, 4], [4, 5]]
d = defaultdict(list)
def dfs(node,d,visited):
    comp = []
    st = [node]
    visited[node] = True
    while st:
        cur = st.pop()
        comp.append(cur)
        for n in d[cur]:
            if not visited[n]:
                st.append(n)
                visited[n] = True
    return comp            
for u,w in edges:
    d[u].append(w)
    d[w].append(u)
visited = [False]*(v+1)    
good = 0
for i in range(1,v+1):
    if not visited[i]:
        visited[i] = True
        nodes = dfs(i,d,visited)
        ch = True
        for j in nodes:
            if len(d[j]) != len(nodes)-1:
                ch = False
                break
        if ch:
            good += 1
print(good)                