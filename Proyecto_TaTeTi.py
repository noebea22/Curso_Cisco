print ("Trabajo Final: Proyecto tateti")
from random import randrange
board=[]
def DisplayBoard(board):
    board =[]
    for j in range (3):
        for i in range (1):
            print("+-------"*3, "+", sep="")
            print("|       "*3, "|", sep="")
            print("|   "+ str (3*j+i+1),"   ","|   "+ str (3*j+i+2),"   ","|   "+ str (3*j+i+3),"  "," |", sep="")
            print("|       "*3, "|", sep="")
    print("+-------"*3, "+", sep="")

def EnterMove(board):
	ok = False	# suposición falsa - lo necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if ok is False:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. Ingrésalo nuevamente.
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Campo ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado
    
      
#def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

#def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

#def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

board [1][1] = "X" 
DisplayBoard(board) 
EnterMove(board)
