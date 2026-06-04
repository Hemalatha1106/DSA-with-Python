mxr=0
mxc=0
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
for i,j in stones:
    mxr=max(mxr,i)
    mxc=max(mxc,j)
n=mxr+mxc+2   
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
seen=set()
for i,j in stones:
    union(i,j+mxr+1)
    seen.add(i)
    seen.add(j+mxr+1)
c=0
for i in seen:
    if find(i)==i:
        c+=1
print(len(stones)-c)            
            
