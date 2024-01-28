def summaryRanges(nums):
    # function to return the smallest sorted list
    if not nums:
        return []
    
    # Initialize variables
    result = []
    start = nums[0]
    end = nums[0]

    
    for i in range(1, len(nums)):
    if nums[i] == end + 1:
        end = nums[i]
    else:
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end)
