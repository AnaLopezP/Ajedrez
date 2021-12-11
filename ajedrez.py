tablero = [['TN1', 'CN1', 'AN1', 'RN', 'RYN', 'AN2', 'CN2', 'TN2' ], 
           ['PN1', 'PN2', 'PN3', 'PN4', 'PN5', 'PN6', 'PN7', 'PN8'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           ['PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8'],
           ['TB1', 'CB1', 'AB1', 'RB', 'RYB', 'AB2', 'CB2', 'TB2',]]

def guardar_tablero(lista, file):
    file = open(file + '.txt', "w")
    file.write(str(lista))
    file.close

def mover_ficha(fila_ficha, columna_ficha, fila_casilla, columna_casilla):
    print(tablero[fila_ficha][columna_ficha])
    tablero[fila_ficha][columna_ficha] = tablero[fila_casilla][columna_casilla]
    print(tablero[fila_casilla][columna_casilla])
    tablero[fila_ficha][columna_ficha] = ' '
    print(tablero[fila_ficha][columna_ficha])

#print("¿Como quieres que se llame el fichero?")
#fichero = input()
#guardar_tablero(tablero, fichero)
#print("tu archivo ha sido creado.\n¿Quieres mover o acabar la partida?")
#decision = input()
#if decision == 'mover':
 #   print("Dime la fila y la columna de la pieza que quieres mover. Ten en cuenta los 0")
  #  fila_ficha = input()
   # columna_ficha = input()
    #print("Ahora dime a que casilla la quieres mover")
    #fila_casilla = input()
    #columna_casilla = input()
    #mover_ficha()
    #guardar_tablero()
fila_ficha = 1
columna_ficha = 1
fila_casilla = 1
columna_casilla = 2
mover_ficha(fila_ficha, columna_ficha, fila_casilla, columna_ficha)