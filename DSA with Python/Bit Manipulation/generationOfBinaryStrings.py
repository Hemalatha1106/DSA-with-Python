#Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them. ----> same pattern but with small tweeks.
#You are given a positive integer n.A binary string x is valid if all substrings of x of length 2 contain at least one "1".Return all valid strings with length n, in any order. ---> same pattern but first problem statement is base for everything.


#hema remember! to find the ith bit 0 or 1 we need to take & with last bit. to get that last bit we do right shift repeatedly. important method used in generating power set, binary string representation and this type of problems.
n = len(nums)
for m in range(1<<n):
    s = ""
    for i in range(n-1,-1,-1):
        s += str((m>>i)&1)#this is the main part. finds the ith bit is 0 or 1. here we are traversing reverse so no need to reverse the s or we should do reverse the s before evaluating.
    if s not in nums:
        print(s)
        exit()
print("") 


#2nd problem
res = []
for m in range(1<<n):
    a = ""
    for i in range(n-1,-1,-1):
        if a != "":
            if a[-1] == "0" and str((m>>i)&1) == "0":
                a = ""
                break
            else:    
                a += str((m>>i)&1)
        else:    
            a += str((m>>i)&1)        
    if len(a) == n:
        res.append(a)
print(res)

