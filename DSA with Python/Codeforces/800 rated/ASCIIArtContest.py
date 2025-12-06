nums = list(map(int,input().split()))
nums.sort()
if nums[-1]-nums[0] >= 10:
    print("check again")
else:
    print("final",nums[1])    