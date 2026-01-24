t=int(input())
for i in range(t):
    n,m,h=map(int,(input().split()))
    arr=list(map(int,input().split()))
    temp=arr.copy()
    for j in range(m):
        b,c=map(int,(input().split()))
        temp[b-1]+=c
        if temp[b-1]>h:
            temp=arr.copy()  
    for k in temp:
        print(k,end=" ")    