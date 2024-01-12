def plusOne(digits):
    """function to add onr to last digit"""
    lastIncrease = [digits[-1] + 1]
    print(lastIncrease)
    results= [digits[:-1] , ...lastIncrease]
    print(results)

plusOne([1,2,3])
