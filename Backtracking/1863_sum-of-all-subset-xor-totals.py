"""
LeetCode 1863: Sum of All Subset XOR Totals
URL: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Difficulty: Easy
Category: Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

Approach:
This solution employs a recursive Depth-First Search (DFS) algorithm, often referred to as backtracking, to implicitly generate all possible subsets of the input array.

Key Observation:
The recursive function explores two branches for each element: either including it in the current subset's XOR sum or excluding it, and then sums the results from both paths to accumulate all subset XOR totals.

Complexity:
- Time Complexity: O(2^N) (For an input array of N elements, there are 2^N possible subsets, and the DFS function visits each potential subset path exactly once.)
- Space Complexity: O(N) (The space complexity is determined by the maximum depth of the recursion stack, which can go up to N in the worst case (length of the `nums` array).)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(ind,x):
            if ind>=len(nums):
                return x
            pick=dfs(ind+1,x^nums[ind])
            notpick=dfs(ind+1,x)
            return pick+notpick
        return dfs(0,0)        