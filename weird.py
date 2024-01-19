def weird(n):
    even= n % 2 == 0
    odd = n % 2 !=0
    if n == even and 2 > n < 5:
        print("Weird")
    elif  n == even and 6>n <20:
        print("Weird")
    elif n == even and n > 20:
        print("Not Weird")

weird(7)