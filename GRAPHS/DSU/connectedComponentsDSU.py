from collections import defaultdict
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
n=len(isConnected[0])
parent=list(range(n))
rank=[0]*(n)
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(u,v):
    uu=find(u)
    uv=find(v)
    if uu==uv:
        return False
    elif rank[uu]>rank[uv]:
        parent[uv]=uu
    elif rank[uv]>rank[uu]:
        parent[uu]=uv
    else:
        parent[uv]=uu
        rank[uu]+=1
    return True
d=defaultdict(list)
for i in range(len(isConnected)):
    for j in range(len(isConnected[i])):
        if isConnected[i][j]==1:
            d[i].append(j)
            d[j].append(i)
for i in d:
    for j in d[i]:
        union(i,j)            
components=0
for i in range(n):
    if find(i)==i:
        components+=1
print(components)        
