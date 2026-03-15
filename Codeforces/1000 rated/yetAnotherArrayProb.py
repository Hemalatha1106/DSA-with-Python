import math
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=-1
    c=2
    while True:
        for i in arr:
            if math.gcd(c,i)==1:
                ans=c
                break
        if ans!=-1:
            break
        c+=1    
    print(ans)            
            

     