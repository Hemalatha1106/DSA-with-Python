"""
LeetCode 1004: Max Consecutive Ones III
URL: https://leetcode.com/problems/max-consecutive-ones-iii/
Difficulty: Medium
Category: Array, Binary Search, Sliding Window, Prefix Sum

Approach:
This solution employs a sliding window technique to find the longest subarray that contains at most 'k' zeros.

Key Observation:
The algorithm efficiently expands the window from the right and shrinks it from the left only when the count of zeros within the window exceeds 'k', ensuring the window always represents a valid candidate subarray.

Complexity:
- Time Complexity: O(N) (Both the left and right pointers traverse the array at most once, leading to a linear scan of the input.)
- Space Complexity: O(1) (The algorithm uses a constant amount of extra space for variables regardless of the input size.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z=0
        mx=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            mx=max(mx,r-l+1)
        return mx                 