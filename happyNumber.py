def happyNumber(n):
    """function  to determine if number is a happy numbetr"""
    
    ind = n % 10
    inf= n // 10
    power = ind **2 + inf **2

    print(ind)
    print(inf)
    print(power)
happyNumber(19)