def climbingStairs(n):
    """function to get ways of getting upstairs"""
    steps=[1,2]
    comp = n / steps[0]
     
    if n == 0 or n == 1:
        return 1
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)
