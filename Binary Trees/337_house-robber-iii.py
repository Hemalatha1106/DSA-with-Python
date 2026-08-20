"""
LeetCode 337: House Robber III
URL: https://leetcode.com/problems/house-robber-iii/
Difficulty: Medium
Category: Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees

Approach:
This solution uses a recursive Depth-First Search (DFS) approach to traverse the binary tree.

Key Observation:
The key insight is that for each node, the function returns a pair of values: the maximum money if the current node is robbed, and the maximum money if the current node is not robbed. This allows for optimal decision-making at each parent node.

DP State:
For each node `u`, the state is defined as a pair `(rob_u, not_rob_u)`, representing the maximum money robable from the subtree rooted at `u` if `u` is robbed, and if `u` is not robbed, respectively.

DP Transition:
Given a node `u` and its children's states `(rob_l, not_rob_l)` and `(rob_r, not_rob_r)`, `rob_u = u.val + not_rob_l + not_rob_r`, and `not_rob_u = max(rob_l, not_rob_l) + max(rob_r, not_rob_r)`.

Complexity:
- Time Complexity: O(N) (Each of the N nodes in the tree is visited exactly once during the DFS traversal, performing constant time operations.)
- Space Complexity: O(H) (The space complexity is determined by the maximum depth of the recursion stack, which is proportional to the height H of the tree. In the worst case (a skewed tree), H can be N.)
"""

# --- LEETVAULT CODE START ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0,0)
            robleft,notrobleft=dfs(root.left)
            robright,notrobright=dfs(root.right)
            pick=root.val+notrobleft+notrobright
            notpick=max(robleft,notrobleft)+max(robright,notrobright)
            return (pick,notpick)
        return max(dfs(root))        