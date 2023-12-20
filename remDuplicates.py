def remDuplicates(nums):
    nums.sort()
    for i in nums:
        print(i)
    k = len(nums)
    print(k)
    l = set(nums)
    print(l)

remDuplicates([1,4,5,9,0])