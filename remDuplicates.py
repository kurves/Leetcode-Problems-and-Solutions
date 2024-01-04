def remDuplicates(nums):
    """function to remiove dupliactes from array"""
    #declare first unique variable
    uniqueNum = 1
  #loop through
    for i in range(1,len(nums)):
        #compare the current with the previou
        if nums[i] != nums[i-1]:var
            #update uniwue count and move nums
            nums[uniqueNum] = nums[i]
            uniqueNum +=1
    return uniqueNum
   

remDuplicates([1,1,2])