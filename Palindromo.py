texto = input('Escribe un texto: ')

texto = texto.upper()
texto = texto.replace(' ','')

for i in range(len(texto)):
    if texto[i] == texto[-i-1] and len(texto)>1:
        ok = 'Es un palindromo'
        break
    else:
        ok= 'No es un palindromo'
print(ok)
