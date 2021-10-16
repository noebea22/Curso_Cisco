first = input('Escribe el primer texto: ')
second = input('Escribe el segundo texto: ')

first = first.upper()
first = first.replace(' ','')
second = second.upper()
second = second.replace(' ','')

for i in first:
    if len(first)==len(second):
        if i in second:
            ok = 'Son anagramas'
        else:
            ok = 'No son anagramas'
            break  
print(ok)

#cadenax1 = ''.join(sorted(list(cadena1.upper().replace(' ',''))))
#cadenax2 = ''.join(sorted(list(cadena2.upper().replace(' ',''))))
#if len(cadenax1) > 0 and cadenax1 == cadenax2:
#	print("Anagramas")
#else:
#	print("No son Anagramas")
