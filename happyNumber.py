def happyNumber(n):
    """function  to determine if number is a happy numbetr"""
    def get_next(num):
        return sum(int(digit)**2 for digit in str(n))
    
    seen = set() 
    while n != 1 and n not in seen:
        seen.add(n) 
        n = get_next(n)
    return n == 1
   
happyNumber(19)