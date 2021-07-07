def readint(prompt, min, max):
    ok=False
    while not ok:
        try:
            v =float(input(prompt))
            v = int(v)
            if v>=min and v<=max:
                ok = True
            else:
                print('Error:Fuera de rango especificado')
                ok = False
        except ValueError:
                print('Error:entrada incorrecta')
                ok = False
    return v

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)