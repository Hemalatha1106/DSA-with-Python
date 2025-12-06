n = int(input())
for i in range(n):
    l = int(input())
    s = input()
    c = s[-1]
    res = 0
    for ch in s:
        if ch != c:
            res += 1
    print(res)        