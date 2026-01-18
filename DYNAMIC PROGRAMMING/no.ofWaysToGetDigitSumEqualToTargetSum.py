mod=10**9+7
class Solution:
    def countWays(self, n, target):
        def recur(d,s):
            if d==0:
                return 1 if s==target else 0
            res=0
            if dp[d][s] != -1:
                return dp[d][s]
            for digit in range(10):
                if digit==0 and d==n:
                    continue
                if s+digit <= target:
                    res= (res+recur(d-1,s+digit))%mod
            dp[d][s] = res        
            return dp[d][s]
        dp=[[-1]*(target+1) for _ in range(n+1)]
        return recur(n,0)
sol=Solution()
print(sol.countWays(2,3))
        