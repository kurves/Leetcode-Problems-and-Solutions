def twosum (nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[i]) == target:
                return [i,i]
          
            
        print([i,i])
        print([nums[i], nums[j]])
    
   
   
twosum([3,4,6],13)        
