dia = input("Ingresa tu dia de cumpleaños: ")
mes = input('Ingresa tu mes de cumpleanos: ')
ano = input('Ingresa tu ano de cumpleanos: ')
fecha = dia + mes + ano

while len(fecha) > 1:
	sum = 0
	for dig in fecha:
		sum += int(dig)
	fecha = str(sum)
print("Tu Dígito de la Vida es: " + fecha)