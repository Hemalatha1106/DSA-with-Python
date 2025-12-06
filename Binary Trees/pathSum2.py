#https://leetcode.com/problems/path-sum-ii?envType=problem-list-v2&envId=depth-first-search
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.   
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def NodePath(root,target,fnl_res,path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and root.val == target:
                fnl_res.append(list(path))
            else:
                NodePath(root.left,target-root.val,fnl_res,path)
                NodePath(root.right,target-root.val,fnl_res,path)
            path.pop()
        fnl_res = []
        path = []
        NodePath(root,targetSum,fnl_res,path)          
        return fnl_res      
        