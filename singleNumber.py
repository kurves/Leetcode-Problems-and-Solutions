def singleNumber(nums):
    #functiion to find single eements
    items={}
    for item in nums:
        items.add(item)
        print(items)
        if item.count == 1:
            print(item)

singleNumber([2,2,1])