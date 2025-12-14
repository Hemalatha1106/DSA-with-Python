t = int(input())
for i in range(t):
    n = input()
    if len(n) > 2 and n[0] == "1" and n[1] == "0" and int(n[2]) > 0 and int(n[2:]) > 1:
        print("YES")
    else:
        print("NO")    
