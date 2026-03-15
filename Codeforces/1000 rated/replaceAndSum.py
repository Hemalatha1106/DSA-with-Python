t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for ind,(i,j) in enumerate(zip(a,b)):
        a[ind]=max(i,j)
    for i in range(len(a)-2,-1,-1):
        a[i]=max(a[i],a[i+1])
    p=[0]
    for i in range(len(a)):
        p.append(p[-1]+a[i])       
    ans=[]   
    for i in range(q):
        l,r=map(int,input().split())
        ans.append(p[r]-p[l-1])
    for i in ans:
        print(i,end=" ")
    print(" ")    


