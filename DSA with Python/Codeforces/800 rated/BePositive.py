import collections
n = int(input())
for i in range(n):
    t = int(input())
    nums = list(map(int,input().split()))
    c = collections.Counter(nums)
    res = 0
    for i in c:
        if i == -1 and c[i]%2 != 0:
            res += 2
        elif i == 0:
            res += c[i]
        else:
            pass
    print(res)            