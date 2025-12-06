n = int(input())
for i in range(n):
    num = int(input())
    l = list(map(int,input().split()))
    check = int(input())
    while len(l) > 1:
        change = True
        for j in range(1,len(l)):
            change = False
            if abs(max(l[j],l[j-1])-min(l[j],l[j-1])) > 1:
                l[j] = (max(l[j],l[j-1])+min(l[j],l[j-1]))//2
                l.pop(j-1)
                change = True
                break
        if not change:
            break
    print(l)        
    if len(l) == 1 and l[0] == check:
        print("YES")
    else:
        print("NO")           