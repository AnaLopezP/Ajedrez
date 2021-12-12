tablero = [['TN1', 'CN1', 'AN1', 'RN', 'RYN', 'AN2', 'CN2', 'TN2' ], 
           ['PN1', 'PN2', 'PN3', 'PN4', 'PN5', 'PN6', 'PN7', 'PN8'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           ['PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8'],
           ['TB1', 'CB1', 'AB1', 'RB', 'RYB', 'AB2', 'CB2', 'TB2',]]

contador = 0

def guardar_tablero(lista, file, contador):
    file = open(file + '.txt', "a")
    file.write("Movimiento " + str(contador) + "\n")
    for i in range(0, 8):
        for j in range(0, 8):
            if j == 7:
                file.write(str(lista[i][j]) + '\n')
            else:
                file.write(str(lista[i][j]) + '\t')
    
    

def mover_ficha(fila_ficha, columna_ficha, fila_casilla, columna_casilla):
    tablero[int(fila_casilla)][int(columna_casilla)] = tablero[int(fila_ficha)][int(columna_ficha)]
    tablero[int(fila_ficha)][int(columna_ficha)] = ' '



print("¿Como quieres que se llame el fichero?")
fichero = input()
guardar_tablero(tablero, fichero, contador)
print("tu archivo ha sido creado.\n¿Quieres mover o acabar la partida?")
decision = input()
while decision == 'mover':
    print("Dime la fila y la columna de la pieza que quieres mover. Ten en cuenta los 0")
    fila_ficha = input()
    columna_ficha = input()
    print("Ahora dime a que casilla la quieres mover")
    fila_casilla = input()
    columna_casilla = input()
    mover_ficha(fila_ficha, columna_ficha, fila_casilla, columna_casilla)
    contador = contador + 1
    guardar_tablero(tablero, fichero, contador)
    print("¿Qué quiere hacer ahora?")
    decision = input()
print("Tu partida ha acabado, gracias por jugar.")

print("¿Qué movimiento quieres ver en pantalla?")

