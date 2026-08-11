class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        def possible(m):
            c=1
            prev=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-prev>=m:
                    c+=1
                    prev=arr[i]
                if c==k:
                    return True
            return False 
        arr.sort()
        l=0
        r=arr[-1]-arr[0]
        while l<=r:
            m=(l+r)//2
            if possible(m):
                ans=m
                l=m+1
            else:
                r=m-1
        return ans        