num = [
'''###
# #
# #
# #
###''',    
''' #
 #
 #
 #
 # ''',
'''###
  #
###
#
###''',
'''###
  #
###
  #
###''',
'''# #
# #
###
  #
  #''',
'''###
#
###
  #
###''',
'''###
#
###
# #
###''',
'''###
  #
  #
  #
  #''',
'''###
# #
###
# #
###''',
'''###
# #
###
  #
  #''']
ok = False

while not ok:
  try:
    numEle = int(input("Elija un numero: "))
    ok = True
    if numEle < 0:
      ok = False
      print("Debes elegir un numero mayor o igual a cero")
      continue
  except ValueError:
    ok= False
    print("Debes elejir un numero entero")
    continue
  if numEle>9:
    ok = True
    numEle = str(numEle)
    print(type(numEle))
    for n in numEle:
      n= int(n)
      print (num[n])
      continue
  else:
   print (num[numEle])

