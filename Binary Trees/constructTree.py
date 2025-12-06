class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
hashmap = {val: i for i, val in enumerate(inorder)}
cur_root_idx = 0
def construct(l,r):
    global cur_root_idx
    if l > r:
        return None
    root = TreeNode(preorder[cur_root_idx])
    inorder_idx = hashmap[preorder[cur_root_idx]]
    cur_root_idx += 1
    root.left = construct(l,inorder_idx-1)
    root.right = construct(inorder_idx+1,r)
    return root
root = construct(0,len(inorder)-1)
print(root.val)      