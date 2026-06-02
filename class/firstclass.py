from collections import deque
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
l=["1", "2", "3", "4", "5", "null", "6"]
q=deque()
root = Tree(l[0])
q.append(root)
ind=1
while q:
    if ind>=len(l):
        break
    node = q.popleft()
    if l[ind] != "null":
        node.left = Tree(l[ind])
        q.append(node.left)
    ind += 1
    if l[ind] != "null":
        node.right = Tree(l[ind])
        q.append(node.right)
    ind += 1
print(root.val)