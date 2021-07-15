mensaje = input('Ingresa tu mensaje: ')
cifrado = ''
ok = False
while not ok:
    try:
        cambio = int(input ('Ingresa un valor de cambio entero del 1 al 25: '))
        ok= True
        if cambio < 1 or cambio > 25:
            ok= False
            print('Debes ingresar un valor del 1 al 25')
            continue
    except ValueError:
        ok= False
        print ('Debes ingresar un numero entero')
        continue

for ch in mensaje:
    if ch.isalpha():
        codigo = ord(ch) + cambio
        if ch.islower() and codigo > ord('z'):            
            codigo = codigo - ord('z') + 96
            cifrado += chr(codigo)
        elif ch.isupper() and codigo > ord('Z'):
            codigo = codigo - ord('Z') + 64
            cifrado += chr(codigo)
        else:
            cifrado += chr(codigo)
    else:
        cifrado += ch
print(cifrado)       



        
