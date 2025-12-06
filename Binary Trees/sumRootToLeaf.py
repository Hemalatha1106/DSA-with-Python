#https://leetcode.com/problems/sum-root-to-leaf-numbers?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calc(root,s,l):
            if not root:
                return
            s += str(root.val) 
            if not root.left and not root.right:
                l.append(s)      
            calc(root.left,s,l)
            calc(root.right,s,l) 
        l = []
        s = ""
        calc(root,s,l)
        l = list(map(int,l))
        return sum(l)
               