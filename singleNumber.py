def singleNumber(nums):
    #functiion to find single eements
    items={}
    for item in nums:
        if item.count == 1:
            print(item)

singleNumber([2,2,1])