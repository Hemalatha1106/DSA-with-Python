t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n > 2:
        a = n//3
        b = n%3
        n = a+b
        res += a
    print(res)    
