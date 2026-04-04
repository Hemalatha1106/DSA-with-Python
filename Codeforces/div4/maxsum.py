t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l.sort()
    s=0
    for j in range(6):
        s-=l[j]
    print(l[-1]+s)    