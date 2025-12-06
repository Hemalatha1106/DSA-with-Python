#Definition for a binary tree node.
#https://leetcode.com/problems/minimum-depth-of-binary-tree?envType=problem-list-v2&envId=depth-first-search
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        l = [0]
        m = [float('inf')]
        if not root:
            return 0
        def calc(root,m,l):
            if not root:
                return 
            l[0] += 1
            if not root.left and not root.right:
                m[0] = min(m[0],l[0])
            calc(root.left,m,l)
            calc(root.right,m,l)
            l[0] -= 1
        calc(root,m,l)
        return m[0]   
