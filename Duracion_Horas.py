hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

y_hora = hora + (dura + min)//60
y_min = (dura + min)%60

print ("Hora de finalizacion: ", y_hora, ":", y_min)