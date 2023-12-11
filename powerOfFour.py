def powerOfFour(n):
    if n % 4 == 0:
        print("true")

    else:
        print("false")

    return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0  
    

powerOfFour(16)
powerOfFour(9)        


