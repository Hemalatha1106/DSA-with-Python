from collections import defaultdict
class solution:
    def shortestPathDAG(self, n, edges, src):
        d = defaultdict(list)
        for i,j,w in edges:
            d[i].append([j,w])
        visited=set()    
        st=[]
        def dfs(node):
            visited.add(node)
            for nei,a in d[node]:
                if nei not in visited:
                    dfs(nei)
            st.append(node)  
        for i in range(n):
            if i not in visited:
                dfs(i)
        st.reverse()
        dist = [float('inf') for _ in range(n)]
        dist[0] = 0
        for u in st:
            if dist[u] == float('inf'):
                continue
            for v,wt in d[u]:
                if dist[u]+wt < dist[v]:
                    dist[v] = dist[u]+wt
        return dist                             
s = solution()
n = 6
edges = [
    (0,1,2), (0,4,1),
    (4,5,4), (4,2,3),
    (1,2,3), (2,3,6),
    (5,3,1)
]
src = 0
print(s.shortestPathDAG(n,edges,src))            