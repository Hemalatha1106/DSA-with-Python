nums = [1,2,3]
ind = -1
for i in range(len(nums)-1,0,-1):
    if nums[i] > nums[i-1]:
        ind = i-1
        break
if ind == -1:
    print(nums[::-1])
    exit()
m = float('inf')    
for i in range(len(nums)-1,ind,-1):            
    if nums[i] > nums[ind] and nums[i] < m:
        m = nums[i]
        ind1 = i
nums[ind],nums[ind1] = nums[ind1],nums[ind]
nums[ind+1:] = nums[ind+1:][::-1]
print(nums)              