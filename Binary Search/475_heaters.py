"""
LeetCode 475: Heaters
URL: https://leetcode.com/problems/heaters/
Difficulty: Medium
Category: Array, Two Pointers, Binary Search, Sorting

Approach:
The solution employs binary search on the answer (the minimum radius) to find the smallest possible radius that satisfies the condition.

Key Observation:
To check if a given radius `r` is 'possible', the code iterates through each house and uses binary search (`bisect_left`) on the sorted list of heaters to efficiently find the closest heater on either side, then verifies if the house is covered.

Complexity:
- Time Complexity: O(M log M + N log M) (Sorting heaters takes O(M log M). The binary search for the radius performs log(max_radius) iterations, each calling `possible(r)` which iterates N houses and performs O(log M) lookup for each.)
- Space Complexity: O(M) (Python's `list.sort()` method, which is Timsort, uses O(M) auxiliary space in the worst case for sorting the heaters list.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def possible(r):
            c=0
            for i in houses:
                p=bisect_left(heaters,i)
                if p<len(heaters) and heaters[p]-i<=r:
                    continue
                if p>0 and i-heaters[p-1]<=r:
                    continue    
                return False            
            return True                   
        l=0
        r=max(abs(max(heaters)-min(houses)),abs(min(heaters)-max(houses)))
        ans=-1
        heaters.sort()
        while l<=r:
            m=(l+r)//2
            if possible(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans         