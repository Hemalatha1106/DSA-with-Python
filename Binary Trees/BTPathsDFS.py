#https://leetcode.com/problems/binary-tree-paths?envType=problem-list-v2&envId=depth-first-search
def path(root,res,fnl_res):
    if not root:
        return
    res.append(root.val)
    if not root.left and not root.right:
        s = ""
        l = list(res)
        for i in range(len(list(l))):
            if i != len(l)-1:
                s += str(l[i])
                s += "->"
            else:
                s += str(l[i])  
        fnl_res.append(s)          
    else:    
        path(root.left,res,fnl_res)
        path(root.right,res,fnl_res)
    res.pop()
fnl_res = []
res = []
root = [1,2,3,null,5]
path(root,res,fnl_res)
print(fnl_res)      

