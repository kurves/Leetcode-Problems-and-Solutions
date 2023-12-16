def palindromeNum(x):
    y=[]
    for i in str(x):
        y.append(i)
    if y[:] == y[::-1]:

        print("True")
    else:
        print('f')

palindromeNum(121)        
