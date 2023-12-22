def remElement(nums, val):
    l=0
    for i in range(len(nums)):
       
        if nums[i] != val:
            nums[l] = nums[i]
            l+=1
    return l        

remElement([6,5,4,5,7,9],5)            