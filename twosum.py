def twosum (nums,target):

    indices={}
    for i,n in enumerate(nums):
        #for j in range(i+1,len(nums)):
        j = target - n
        if j in indices:
            return [indices[j],i]
        indices[nums] = i    
        #if (nums[i] + nums[i]) == target:
           #return [i,i]

          
            
        #print([i,i])
        #print([nums[i], nums[i]])
    
   
   
twosum([3,4,6,3],13)        
