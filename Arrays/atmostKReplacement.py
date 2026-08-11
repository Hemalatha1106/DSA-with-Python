from collections import defaultdict
s=input("Enter s: ")
k=int(input("Enter k: "))
d=defaultdict(int)
l=0
res=0
for r in range(len(s)):
    d[s[r]]+=1
    mx=max(d.values())
    while (r-l+1)-mx>k:
        d[s[l]]-=1
        l+=1
    res=max(res,r-l+1)
print(res)        