def wordLength(s):
    """Function to get length if last word"""

    words = s.strip().split(" ")
    lastword = words[-1]
    print(len(lastword))


wordLength("kurves  mmmm")