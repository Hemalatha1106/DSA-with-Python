"""
LeetCode 968: Binary Tree Cameras
URL: https://leetcode.com/problems/binary-tree-cameras/
Difficulty: Hard
Category: Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees

Approach:
The algorithm uses a post-order Depth-First Search (DFS) to traverse the tree, assigning a state to each node based on its coverage status and making greedy decisions from children up to parents.

Key Observation:
It minimizes cameras by identifying uncovered children (state 0) and immediately placing a camera at their parent (current node, state 1), or if a child already has a camera (state 1), the current node is covered (state 2).

Complexity:
- Time Complexity: O(N) (Each node in the binary tree is visited exactly once during the DFS traversal.)
- Space Complexity: O(H) (The space complexity is determined by the maximum depth of the recursion stack, which in the worst case (a skewed tree) can be equal to the height (H) of the tree.)
"""

# --- LEETVAULT CODE START ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #2->covered, 1->hasCamera, 0->not covered
        self.c=0
        def dfs(root):
            if not root:
                return 2
            left=dfs(root.left)
            right=dfs(root.right)
            if left==0 or right==0:
                self.c+=1
                return 1    
            if left==1 or right==1:
                return 2
            if left==2 and right==2:
                return 0
        r=dfs(root)
        if r==0:
            self.c+=1
        return self.c                
