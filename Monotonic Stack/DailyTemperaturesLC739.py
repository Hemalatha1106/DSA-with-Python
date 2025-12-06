#This is next greater and equal element maathiri but inga small tweek instead of storing element we should store the index. that's it and calculate the distance.
temperatures = [89,62,70,58,47,47,46,76,100,70]
ngt = []
st = []
for i in range(len(temperatures)-1,-1,-1):
    while st and temperatures[st[-1]] <= temperatures[i]:
        st.pop()
    if len(st)==0:
        ngt.append(0)
    elif temperatures[i] < temperatures[st[-1]]:
        ngt.append(st[-1]-i)        
    st.append(i)    
return ngt[::-1]

