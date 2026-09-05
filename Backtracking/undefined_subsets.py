"""
LeetCode undefined: Subsets
URL: https://leetcode.com/problems/subsets/
Difficulty: Medium
Category: Array, Backtracking, Bit Manipulation

Approach:
This implementation uses a recursive backtracking (Depth-First Search) approach to systematically generate all possible subsets by making a choice for each element.

Key Observation:
The core design involves two recursive calls for each element: one to include it in the current subset and one to exclude it, utilizing `l.pop()` for efficient backtracking.

Complexity:
- Time Complexity: O(N * 2^N) (There are `2^N` possible subsets. For each subset, constructing and copying it to the result list takes `O(N)` time, where `N` is the number of elements in `nums`.)
- Space Complexity: O(N) (The auxiliary space is dominated by the recursion stack depth and the temporary list `l`, both of which can grow up to `N` elements.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(ind,l):
            if ind==len(nums):
                res.append(l[:])
                return
            l.append(nums[ind])
            dfs(ind+1,l)
            l.pop()
            dfs(ind+1,l)
        res=[]
        dfs(0,[])
        return res    