"""
LeetCode 875: Koko Eating Bananas
URL: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Medium
Category: Array, Binary Search

Approach:
This implementation uses binary search on the answer space to find the minimum eating speed. It searches for the smallest integer 'k' (eating speed) within a determined range that allows Koko to finish all bananas within 'h' hours.

Key Observation:
The key is that the 'possible' function, which checks if a given speed 't' is feasible, exhibits monotonicity: if speed 't' works, any speed greater than 't' will also work. This property enables an efficient binary search to find the minimum working speed.

Complexity:
- Time Complexity: O(N log M) (The binary search performs 'log M' iterations where 'M' is the maximum pile size, and each iteration calls the 'possible' helper function which iterates through all 'N' piles.)
- Space Complexity: O(1) (The algorithm uses a constant amount of extra space for variables regardless of the input size, not counting the input array itself.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(t):
            res=0
            for i in piles:
                res+=ceil(i/t)
            return res<=h
        l=1
        r=max(piles)
        while l<=r:
            m=(l+r)//2
            if possible(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans                        