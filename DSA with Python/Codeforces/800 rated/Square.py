n = int(input())
for i in range(n):
    a, b, c, d = input().split()
    if a == b == c == d:
        print("YES")
    else:
        print("NO")    
