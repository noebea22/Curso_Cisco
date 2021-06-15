def DisplayBoard(board):
    for i in range(0,len(board),3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   " + str(board[i]) + \
                 "   |   " + str(board[i + 1]) + \
                "   |   " + str(board[i + 2]) + "   |   ")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")
board =[]
DisplayBoard(board)


#empty = "-"
#tablero = [[empty for i in range(3)]for j in range (3)]
n=1
for i in range (3):
    for j in range (3):
        #tablero.append (n)
        n += 1
    
    
#print(tablero) 

def DisplayBoard():
    n=1
    tablero =[['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
    print(tablero)
DisplayBoard()