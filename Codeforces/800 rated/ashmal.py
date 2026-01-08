t = int(input())
for a in range(t):
    n = int(input())
    l = list(input().split())
    s = []
    for i in l:
        if not s:
            s.append(i)
        elif i > s[0]:
            s.append(i)
        elif i <= s[0]:
            s.insert(0,i)
    print("".join(s))        
       
