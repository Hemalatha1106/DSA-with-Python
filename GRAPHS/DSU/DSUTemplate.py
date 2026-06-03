class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def findUltimateParent(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        UltParentOfU=self.findUltimateParent(u)
        UltParentOfV=self.findUltimateParent(v)
        if UltParentOfU==UltParentOfV:
            return False
        elif self.rank[UltParentOfU]>self.rank[UltParentOfV]:
            self.parent[UltParentOfV]=UltParentOfU
        elif self.rank[UltParentOfU]<self.rank[UltParentOfV]:
            self.parent[UltParentOfU]=UltParentOfV
        else:
            self.parent[UltParentOfV]=UltParentOfU        
            self.rank[UltParentOfU]+=1
        return True
a=DSU(6)
a.union(1,2)  
a.union(3,4)  
a.union(2,3)
if a.findUltimateParent(2)==a.findUltimateParent(5):
    print("belongs to same")
else:
    print("does not belongs")      
a.union(2,5)  
   
if a.findUltimateParent(2)==a.findUltimateParent(5):
    print("belongs to same")
else:
    print("does not belongs")      


    