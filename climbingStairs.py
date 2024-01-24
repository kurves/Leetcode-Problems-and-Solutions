def climbingStairs(n):
    """function to get ways of getting upstairs"""
    
     
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)
