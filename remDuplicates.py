def remDuplicates(nums):
    """function to remiove dupliactes from array"""
    # declare a set to store unique elements

    setNums = set(nums)
  
   #convert to list to mainatain order

    k= len(list(setNums))
    print(k,list(setNums))
   

remDuplicates([1,1,2])