class Solution:
    def goodDaysToRobBank(self, security, time):
        inc = [0]
        dec = [0]
        c = 0
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                c+=1
                inc.append(c)
            else:
                c=0
                inc.append(c)
        c=0        
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                c += 1
                dec.append(c)
            else:
                c=0
                dec.append(c)
        dec =  dec[::-1]
        res = []
        for ind,(i,j) in enumerate(zip(inc,dec)):
            if i >= time and j >= time:
                res.append(ind)
        return res    
sol = Solution()
print(sol.goodDaysToRobBank([5,3,3,3,5,6,2],2))
