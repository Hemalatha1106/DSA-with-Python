from collections import Counter
t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = Counter(arr)
    res = 0
    for i in c:
        if c[i] > i:
            res += c[i]-i
        elif c[i] < i:
            res += c[i]
        else:
            pass        
    print(res)        