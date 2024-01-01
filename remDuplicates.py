def remDuplicates(nums):
   setNums = set(nums)
   print(setNums)
   length = len(list(setNums))
   print(length)
   total =0
   for i in nums:
    total += i
    print(total)

remDuplicates([1,4,5,9,0,7,4,1])