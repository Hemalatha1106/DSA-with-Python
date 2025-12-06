# Definition for a binary tree node.
#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers?envType=problem-list-v2&envId=depth-first-search
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        s = [0]
        b = []
        def calc(root,b,s):
            if not root:
                return
            b.append(str(root.val))
            if not root.left and not root.right:
                a = "".join(b)
                s[0] += int(a,2)
            calc(root.left,b,s)
            calc(root.right,b,s)
            b.pop()
        calc(root,b,s)
        return s[0]  
