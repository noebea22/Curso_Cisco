print ("Trabajo Final: Proyecto tateti")
board=[]
def DisplayBoard(board):
    n=1
    board =[[n for i in range (3)]for j in range (3)]
    for i in range (3):
        for j in range (3):
            board [i][j] = n
            n += 1
            board[1][1]= "x"
    print(board)

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