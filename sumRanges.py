def summaryRanges(nums):
    # function to return the smallest sorted list
    if not nums:
        return []
    
    # Initialize variables
    result = []
    start = nums[0]
    end = nums[0]

    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            result.append((start, nums[i - 1]))
            start = nums[i]
            start = nums[i]
        else:
            end = sums[i]
            
    result.append((start, end) if start == end else f"{start}->{end}")

    return result

