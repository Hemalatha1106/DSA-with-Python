nums = [3,1,2,1]
st = []
res = 0
for i in range(len(nums)):
    while st and st[-1] > nums[i]:
        st.pop()
    if len(st) == 0:
        st.append(-1)    
    if nums[i] > st[-1] and nums[i] != 0:
        st.append(nums[i])
        res += 1
print(res)        
