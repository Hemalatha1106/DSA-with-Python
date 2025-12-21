nums = [1,2,2,3,3,4]
k = 2
nums.sort()
m = float('-inf')#this prefix max, keep tracks of previous taken max number, to ensure to select the current number greater than it.
res = 0
for i in nums:
    l = i-k #this is lower bound hema
    h = i+k # this is upper bound hema
    if m < l:#here what happens naa if prefix max is lower than required lowest bound, then the valind distint is formed i.e we increase cnt and before max to selected lowed bound
        res += 1
        m = max(m,l)
    elif m < h:
        res += 1
        m += 1
print(res)            
