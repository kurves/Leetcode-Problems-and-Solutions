def validParen(s):
    if (s[0] =="[") & (s[-1] =="]"):
        print("true")
    elif (s[0]== "{") &(s[-1] == "}"):
        print("true")   
    else:
        print("false")     

validParen("[}")