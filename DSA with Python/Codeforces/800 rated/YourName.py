n = int(input())
for i in range(n):
    num = int(input())
    s1, s2 = input().split()
    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("No")
            
