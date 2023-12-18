def commonPrefix(strs):
    for i in strs:
        print(i)
        print(i[0][:2])
        if i[0][:2] == i[1][:2]:
            print(i[0][:2])
            print("true")



commonPrefix(["kurves","kumoh","mwes"])