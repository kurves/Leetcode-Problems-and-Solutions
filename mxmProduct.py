def mxmProduct(nums):
    k = [i for i in sorted(nums)]
    print(k) 
    i=k[-1]
    j=k[-2]
    print(i,j)
    p = (i-1) * (j-1)
    print(p)


mxmProduct([2,1,6,7,3])

