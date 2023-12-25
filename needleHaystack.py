def needleHaystack(needle, haystack):
    l= haystack.find(needle)
    if (l != -1):
        print(l) 
    else:
        return -1    
    if needle in haystack:
        print("true")
    else:
        return -1
  
        haystack.split(needle)
       
       

needleHaystack("sad","sadbutsad")