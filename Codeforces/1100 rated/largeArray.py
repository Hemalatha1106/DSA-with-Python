import math
t=int(input())
#should think how many copy fails
for _ in range(t):
    n,k,x=map(int,input().split())
    arr=list(map(int,input().split()))
    res=0
    p=0
    sm=sum(arr)
    suff=[]
    for i in arr:
        suff.append(sm-p)
        p+=i
    total=sum(arr)    
    for i in range(len(arr)):
        if suff[i]>=x:
            res+=k
        else:
            need=x-suff[i]
            cyc=math.ceil(need/total)
            if cyc<k:
                res+=(k-cyc)  
    print(res)            
