def recr(ind,prev):
    if ind==len(nums):
        return 0
    notpick=recr(ind+1,prev)
    pick=0
    if prev==-1 or nums[ind]>nums[prev]:
        pick=1+recr(ind+1,ind)
    return max(pick,notpick)
nums=[10,9,2,5,3,7,101,18]
res=recr(0,-1)
print(res)    