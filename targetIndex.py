def targetIndex(nums,target):
    """function to get index of target"""
    left, right = 0, len(nums)-1

#while loop to loop through array
    while left <=right:
        mid = left + (right-left)
        if nums[mid] ==target:
            return mid
        elif ( nums[mid] , target):

            left = mid +1
        else:
            right + 1
    return left        

targetIndex([7,5,7],9)