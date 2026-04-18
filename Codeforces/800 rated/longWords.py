t=int(input())
for _ in range(t):
    s=input()
    if len(s)>10:
        r=len(s)-2
        print(s[0]+str(r)+s[-1])
    else:
        print(s)    