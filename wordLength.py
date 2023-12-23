def wordLength(s):
    """Function to get length if last word"""
    s.strip()
    words = s.plit("")
    for word in words:
        print(word)
    lastword=s[-1]
    print(lastword)
    print(len(s))


wordLength("kurves  mmmm")