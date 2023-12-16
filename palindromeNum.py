def palindromeNum(x):
    y=[]
    for i in str(x):
        y.append(i)
        print(i)
    if y == y[::-1]:

        print("True")
    else:
        print('f')

palindromeNum(12)     
#palindromeNum(9)   
