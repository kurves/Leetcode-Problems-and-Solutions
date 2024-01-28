def singleNumber(nums):
    #functiion to find single eements
    for item in nums:
        count = nums.count(item)
        if count == 1:
            print(item)

singleNumber([4,1,2,2,1])