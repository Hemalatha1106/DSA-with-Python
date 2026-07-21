"""
LeetCode 100: Same Tree
URL: https://leetcode.com/problems/same-tree/
Difficulty: Easy
Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Approach:
This solution employs a recursive Depth-First Search (DFS) approach to traverse both binary trees simultaneously.

Key Observation:
It leverages short-circuiting logic by returning false immediately upon detecting any mismatch in node existence (one is None, the other isn't) or node values, thereby pruning unnecessary further comparisons.

Complexity:
- Time Complexity: O(N) (The algorithm visits each corresponding pair of nodes at most once, where N is the minimum number of nodes in the two trees (or the total nodes up to the first detected difference).)
- Space Complexity: O(H) (The space complexity is determined by the maximum depth of the recursion stack, which can be up to H (height of the tree). In the worst case (a skewed tree), H can be N (the total number of nodes).)
"""

# --- LEETVAULT CODE START ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True 
            if not p or not q:
                return False  
            if p.val!=q.val:
                return False
            l=dfs(p.left,q.left)
            r=dfs(p.right,q.right)
            return l and r
        return dfs(p,q)    

            