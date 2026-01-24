t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mx=max(arr)
    print(mx*len(arr))
    