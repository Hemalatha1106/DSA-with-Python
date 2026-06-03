n = 4
connections = [[0,1],[0,2],[1,2]]
if len(connections)<n-1:
    print(-1)
    exit()
parent=list(range(n))
rank=[0]*n
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(u,v):
    ultU=find(u)
    ultV=find(v)
    if ultU==ultV:
        return False
    elif rank[ultU]>rank[ultV]:
        parent[ultV]=ultU
    elif rank[ultV]>rank[ultU]:
        parent[ultU]=ultV
    else:
        parent[ultV]=ultU
        rank[ultU]+=1
    return True
for i,j in connections:
    union(i,j)
res=0
for i in range(n):
    if find(i)==i:
        res+=1
print(res-1)
