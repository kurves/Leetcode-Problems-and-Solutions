def twosum(arr,n):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j]) == n:
                return [i,j]
          
            
            #print(i, end=" ")
    
   
   
twosum([3,4,6],13)        
