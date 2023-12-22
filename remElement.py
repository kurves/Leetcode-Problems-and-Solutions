def remElement(nums, val):
    for i in range(len(nums)):
        print(i) 
        if nums[i] == val:
            nums.remove(i)

remElement([6,5,4,5,7,9],5)            