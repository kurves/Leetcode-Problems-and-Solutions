def climbingStairs(n):
    """function to get ways of getting upstairs"""
    
     
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
        return climbingStairs(n-1) + climbingclear
    dp = [0] * (n+1)        
    dp[1]=1
    dp[2]= 2
