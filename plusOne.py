def plusOne(digits):
    """function to add onr to last digit"""
    rem = 1
    for i in range(len(digits)-1,-1,-1):
        total = digits[i] + rem
        digits[i] = total %10
        rem = total // 10 
    if rem:
        digits = [1] + digits
    return digits
    
plusOne([9])
