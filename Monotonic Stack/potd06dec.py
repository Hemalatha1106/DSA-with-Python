nums = [9,4,1,3,7]
k = 4
nge = []
nse = []
st = []
for i in range(len(nums)-1,-1,-1):
    while st and st[-1] < nums[i]:
        st.pop()
    if not st:
        nge.append(-1)
    else:    
        nge.append(st[-1])        
    st.append(nums[i])
st = []
for i in range(len(nums)-1,-1,-1):
    while st and st[-1] > nums[i]:
        st.pop()
    if not st:
        nse.append(-1)
    else:    
        nse.append(st[-1])        
    st.append(nums[i])  
nge = nge[::-1]
nse = nse[::-1]      