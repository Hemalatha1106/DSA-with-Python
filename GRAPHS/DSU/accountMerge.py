#leetcode 721
from collections import defaultdict
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
n=len(accounts)
parent=list(range(n))
rank=[1]*n
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
acc_ind={}
for i,acc in enumerate(accounts):
    for m in acc[1:]:
        if m in acc_ind:
            union(acc_ind[m],i)
        else:
            acc_ind[m]=i
merge=defaultdict(list)
for acc,ind in acc_ind.items():
    p=find(ind)
    merge[p].append(acc)
res=[]
for ind,accs in merge.items():
    res.append([accounts[ind][0]]+sorted(accs))
print(res)