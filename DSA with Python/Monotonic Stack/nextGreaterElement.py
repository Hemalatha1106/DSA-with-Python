arr = [4,5,2,1,4]
ans = []
st =[]
for i in range(len(arr)-1,-1,-1):
    while len(st) != 0 and st[-1] < arr[i]:
        st.pop()
    if len(st) != 0:    
        ans.append(st[-1])
    else:
        ans.append(-1)    
    st.append(arr[i])      
print(ans[::-1])          