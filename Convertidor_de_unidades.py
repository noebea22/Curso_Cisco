def l100kmtompg(liters):
    res= (100*3.785411784*1000)/(liters*1609.344)
    return (res)
    

def mpgtol100km(miles):
    res = (3.785411784*100000)/(miles*1609.344)
    return (res)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))