# Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.
nums = [1,2,3]
n = len(nums)
subsets = 1 << n
ans = []
for num in range(subsets):
    subset = []
    for i in range(n):
        # Check if the ith bit of
        # the current number is set
        if num & (1 << i):
            # If the bit is set, add the
            # corresponding element from
            # the input array to the subset
            subset.append(nums[i])
    
    # Add the current subset
    # to the list of subsets
    ans.append(subset)
print(ans)