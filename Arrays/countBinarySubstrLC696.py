p=0
c=1
res=0
for i in range(1,len(s)):
    if s[i-1] == s[i]:
        c+=1
    else:
        res+=min(p,c) 
        p=c
        c=1
res+=min(p,c)     
print(res)           