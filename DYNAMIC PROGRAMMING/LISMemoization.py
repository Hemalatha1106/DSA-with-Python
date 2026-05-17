def recr(ind,prev):
    if ind==len(nums):
        return 0
    if dp[ind][prev+1]!=-1:
        return dp[ind][prev+1]
    notpick=recr(ind+1,prev)
    pick=0
    if prev==-1 or nums[ind]>nums[prev]:
        pick=1+recr(ind+1,ind)
    dp[ind][prev+1]=max(pick,notpick)
    return dp[ind][prev+1]
nums=[10,9,2,5,3,7,101,18]
n=len(nums)
dp=[[-1]*(n+1) for _ in range(n)]
res=recr(0,-1)
print(res)    