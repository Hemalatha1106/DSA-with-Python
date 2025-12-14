import math
t = int(input())
for j in range(t):
    n,k,p = map(int,input().split())
    k = abs(k)
    if n*p < k:
        print(-1)
    else:
        print(math.ceil(k/p))    
    