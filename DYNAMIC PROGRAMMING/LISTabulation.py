nums=[10,9,2,5,3,7,101,18]
n=len(nums)
dp=[[0]*(n+1) for _ in range(n+1)]
for ind in range(n-1,-1,-1):
    for prev in range(ind-1,-2,-1):
        notpick=dp[ind+1][prev+1]
        pick=0
        if prev==-1 or nums[ind]>nums[prev]:
            pick=1+dp[ind+1][ind+1]
        dp[ind][prev+1]=max(pick,notpick)    
print(dp[0][0])        