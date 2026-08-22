# this is the template that is used to build bst if the order need to be preserved
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input()) 
l=list(map(int,input().split()))
root=TreeNode(l[0])
def dfs(root,n):
    if n.val>root.val:
        if not root.right:
            root.right=n
        else:
            dfs(root.right,n)
    else:
        if not root.left:
            root.left=n
        else:
            dfs(root.left,n)                
for i in l[1:]:
    n=TreeNode(i)
    dfs(root,n)
