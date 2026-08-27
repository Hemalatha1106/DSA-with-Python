"""
LeetCode 226: Invert Binary Tree
URL: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Approach:
This implementation uses a recursive Depth-First Search (DFS) traversal to visit every node in the binary tree.

Key Observation:
At each visited node, the left and right child pointers are swapped, and then the inversion process is recursively applied to the newly positioned left and right subtrees.

Complexity:
- Time Complexity: O(N) (Each node in the tree is visited exactly once, and a constant amount of work (swap, recursion calls) is performed at each node.)
- Space Complexity: O(N) (The space complexity is determined by the maximum depth of the recursion stack, which in the worst-case (a skewed tree) can be equal to the number of nodes (N).)
"""

# --- LEETVAULT CODE START ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                return
            root.left,root.right=root.right,root.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root            