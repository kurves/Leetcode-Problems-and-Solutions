def singleNumber(nums):
    #functiion to find single eements
    for item in nums:
        count = nums.count(item)
        print(count)

singleNumber([2,2,1])