def climbingStairs(n):
    """function to get ways of getting upstairs"""
    
     
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
     
    dp = [0] * (n+1)        
    dp[1]=1
    dp[2]= 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[1-2]
    return dp[n]