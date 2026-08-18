"""
LeetCode 687: Longest Univalue Path
URL: https://leetcode.com/problems/longest-univalue-path/
Difficulty: Medium
Category: Tree, Depth-First Search, Binary Tree, DP on Trees

Approach:
A recursive Depth-First Search (DFS) traversal explores the tree. For each node, it recursively calculates the longest univalue path extending downwards and updates a global maximum path length by considering paths that pass through the current node.

Key Observation:
The `dfs` function returns the length of the longest univalue path starting from the current node and going down either left or right, while simultaneously updating a global maximum path that could combine paths from both children.

Complexity:
- Time Complexity: O(N) (Each node in the tree is visited exactly once by the `dfs` function, and constant time operations are performed at each visit.)
- Space Complexity: O(H) (The space complexity is determined by the recursion stack depth, which can be up to the height of the tree (H); in the worst-case skewed tree, H equals N.)
"""

# --- LEETVAULT CODE START ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left=0
            right=0
            lp=dfs(root.left)
            rp=dfs(root.right)
            if root.left and root.val==root.left.val:
                left=lp+1
            if root.right and root.val==root.right.val:
                right=rp+1   
            self.mx=max(self.mx,left+right)
            return max(left,right)
        self.mx=0
        dfs(root)
        return self.mx             