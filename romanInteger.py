def romanInteger(s):
    Values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    prev_value = 0

    for i in reversed(s):
        value = Values[i]

    if value < prev_value:
        result -= value        

    dividend =s // 10:
    if dividend == 10:
        print("X")
