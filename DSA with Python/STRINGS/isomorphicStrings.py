s = 'abb'
t = "mpp"
hashmap = dict()
if len(s) != len(t):
    print(False)
    exit()
for i in range(len(s)):
    if s[i] not in hashmap.keys() and t[i] not in hashmap.values():
        hashmap[s[i]] = t[i]
    else:
        if s[i] in hashmap.keys():
            if hashmap[s[i]] != t[i]:
                print(False)
                exit()
        else:
            print(False)
            exit()        
print(True)            
