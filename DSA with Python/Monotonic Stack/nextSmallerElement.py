nums = [6,8,0,1,3]
st = []
res = []
for i in range(len(nums)-1,-1,-1):
    while st and st[-1] > nums[i]:
        st.pop()
    if len(st) == 0:
        res.append(-1)
    elif st[-1] < nums[i]:
        res.append(st[-1])
    st.append(nums[i])    
print(res[::-1])    
            