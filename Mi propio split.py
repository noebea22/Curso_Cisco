def misplit(strng):
    lst = []
    word = ''
    if strng == '' or strng.isspace():
        return[]
    inword = strng[0].isalnum()
    for x in strng:
        if inword:
            if not x.isspace():
                word += x
            else:    
                lst.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
        lst.append(word)
    return lst        
        
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))