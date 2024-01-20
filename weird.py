def weird(n):
    even= n % 2 == 0
    odd = n % 2 !=0
    if even and 2 <= n <= 5:
        print("Not Weird")
    elif  even and 6 <= n <=20:
        print("Weird")
    elif  even and n > 20:
        print("Not Weird")
    elif odd:
        print("Weird")

weird(4)