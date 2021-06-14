us_blue= 142
us_oficial= 98
us_solidario= us_oficial * 1.30 * 1.35

print("Dolar Blue:", us_blue)
print("Dolar Oficial:", us_oficial)
print("Dolar Solidario:", round(us_solidario,2))

ahorro_us= 2030

ahorro_blue= ahorro_us * us_blue
ahorro_oficial= ahorro_us * us_oficial
ahorro_solidario= ahorro_us * us_solidario
print()
print("Ahorro en Pesos")
print()
print("Ahorro al Blue:",round(ahorro_blue,2))
print("Ahorro al Oficial:",round(ahorro_oficial,2))
print("Ahorro al Solidario:",round(ahorro_solidario,2))

