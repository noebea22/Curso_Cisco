def DisplayBoard(board):
    for i in range(0,len(board),3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   " + str(board[i]) + \
                 "   |   " + str(board[i + 1]) + \
                "   |   " + str(board[i + 2]) + "   |   ")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")

empty = "-"
tablero = [[empty for i in range(3)]for j in range (3)]

tablero [0][0] = "1"
tablero [0][1] = "2"
tablero [0][2] = "3"
tablero [1][0] = "4"
tablero [1][1] = "5"
tablero [1][2] = "6"
tablero [2][0] = "7"
tablero [2][1] = "8"
tablero [2][2] = "9"
    
print(tablero)  


#empty = "-"
#tablero = [[empty for i in range(3)]for j in range (3)]
n=1
for i in range (3):
    for j in range (3):
        #tablero.append (n)
        n += 1
    
    
print(tablero) 

def DisplayBoard():
    n=1
    tablero =[['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
    print(tablero)
DisplayBoard()