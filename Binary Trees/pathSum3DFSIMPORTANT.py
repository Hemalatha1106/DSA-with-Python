#https://leetcode.com/problems/path-sum-iii?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        s = 0
        h = {0:1}
        self.res = 0
        def trav(root,s,h):
            if not root:
                return None
            s += root.val    
            if s-targetSum in h.keys():
                self.res += h[s-targetSum]
            h[s] = h.get(s,0)+1
            trav(root.left,s,h)
            trav(root.right,s,h)
            h[s] -= 1
            s -= root.val
        trav(root,s,h)    
        return self.res