def commonPrefix(strs):
    strs.sort()
    fs= strs[0]
    ls= strs[-1]
    for i in strs:
        for j in i:
            print(j)
    print(i)
    if i[0][:2] == i[1][:2]:
        print(i[0][:2])
        print("true")



commonPrefix(["kurves","kumoh","mwes"])