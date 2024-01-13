def plusOne(digits):
    """function to add onr to last digit"""
    rem = 1
    for i in range(len(digits)-1,-1,-1):
        total = digits[i] + rem
        digits[i] = total %10
    lastIncrease = [digits[-1] + 1]
    print(lastIncrease)
    results= digits[:-1] +lastIncrease
    print(results)

plusOne([9])
