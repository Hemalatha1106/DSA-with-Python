class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def buildtree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0]) 
    q = [root]
    i = 1
    while q and i < len(arr):
        node = q.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root
inorderL = []
preorderL = []
postorderL = []    
def inorder(root):
    global inorderL
    if not root:
        return None
    inorder(root.left)
    inorderL.append(root.val)
    inorder(root.right)
def preorder(root):
    global preorderL
    if not root:
        return None
    preorderL.append(root.val)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    global postorderL
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    postorderL.append(root.val)
arr = [1, None, 2, 3]
root = buildtree(arr)
inorder(root)
postorder(root)
preorder(root)
print(inorderL)
print(preorderL)
print(postorderL)