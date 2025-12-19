from collections import Counter
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = sorted(list(map(int, input().split())),reverse=True)
    a = Counter(arr)
    cnt = 0
    for j in arr:
        if j >= k-j:
            if k-j in a.keys() and a[k-j] > 0:
                cnt += 1
                a[j] -= 1
                a[k-j] -= 1
        else:
            break        
    print(cnt)        
