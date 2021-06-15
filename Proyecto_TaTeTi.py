print ("Trabajo Final: Proyecto tateti")
board=[]
def DisplayBoard(board):
    n=0
    board =[]
    for j in range (3):
        for i in range (1):
            print("+-------"*3, "+", sep="")
            print("|       "*3, "|", sep="")
            print("|   "+ str (3*j+i+1),"   ","|   "+ str (3*j+i+2),"   ","|   "+ str (3*j+i+3),"  "," |", sep="")
            print("|       "*3, "|", sep="")
    print("+-------"*3, "+", sep="")
DisplayBoard(board)  


#def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

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