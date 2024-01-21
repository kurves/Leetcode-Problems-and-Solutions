def happyNumber(n):
    """function  to determine if number is a happy numbetr"""
    def get_next(num):
        n = sum(int(digit)**2 for digit in str(n))
    
    seen = set() 
    while n != 1 and n not in seen:
        seen.add(n) 
   
happyNumber(19)