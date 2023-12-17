def twosum (nums,target):

    indices={}
    for i,n in enumerate(nums):
        #print(i,n)
        j = target - n
        if j in indices:
            return [indices[j],i]
        
        indices[n] = i    
    return []
          
            
        #print([i])
        #print([nums[i], nums[i]])
    
   
   
twosum([10,4,6,3],13)        
