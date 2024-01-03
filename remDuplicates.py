def remDuplicates(nums):
    """function to remiove dupliactes from array"""
    # declare a set to store unique elements
    uniqueNum = 1
    
  
   #convert to list to mainatain order
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[uniqueNum] = nums[i]
            uniqueNum +=1
    return uniqueNums
   

remDuplicates([1,1,2])