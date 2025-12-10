t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    x = l[0]
    n = l[1]
    if n%2 == 0:
        print(0)
    else:
        print(x)    