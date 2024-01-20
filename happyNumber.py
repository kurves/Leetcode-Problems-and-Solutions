def happyNumber(n):
    """function  to determine if number is a happy numbetr"""
    
    seen = set() 
    while n != 1 and n not in seen:
    seen.add(n) 
    n = sum(int(digit)**2 for digit in str(n))
happyNumber(19)