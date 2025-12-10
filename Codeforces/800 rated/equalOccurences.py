from collections import Counter
t = int(input())
for k in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c =  Counter(arr)
    m = max(c.values())
    mx = 0
    for i in range(m+1):
        res = 0
        for j in c:
            if c[j] >= i:
                res += i
        mx = max(mx,res)        
    print(mx)    