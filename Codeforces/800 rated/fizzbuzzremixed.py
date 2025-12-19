t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for j in range(0,n+1):
        if j%3 == j%5:
            cnt += 1
    print(cnt)        