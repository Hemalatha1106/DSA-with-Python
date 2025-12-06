#https://leetcode.com/problems/flatten-binary-tree-to-linked-list?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        def preOrder(root):
            if not root:
                return
            l.append(root)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        def trav(root,l):       
            if not root:
                return
            root.left = None    
            for i in range(1,len(l)):        
                prev = l[i-1]
                node = l[i]    
                prev.right = node
                prev.left = None
            return root
        return trav(root,l)        
