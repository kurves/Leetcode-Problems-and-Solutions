def commonPrefix(strs):
    strs.sort()
    fs= strs[0]
    ls= strs[-1]

    cp = ""
    for i in range(len(fs)):
        if i < len(ls) and fs[i] == ls[i]:
            cp += fs[i]
        else:
            break
    return cp
   

    if not strs:
        return [""]     


commonPrefix(["kurves","kumoh","mwes"])