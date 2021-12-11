tablero = [['TN1', 'CN1', 'AN1', 'RN', 'RYN', 'AN2', 'CN2', 'TN2' ], 
           ['PN1', 'PN2', 'PN3', 'PN4', 'PN5', 'PN6', 'PN7', 'PN8'],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
           ['PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8'],
           ['TB1', 'CB1', 'AB1', 'RB', 'RYB', 'AB2', 'CB2', 'TB2',]]

def guardar_tablero(lista, file):
    file = open(file, "w")
    file.write(str(lista))
    file.close

print("¿Como quieres que se llame el fichero?")
fichero = input()
guardar_tablero(tablero, fichero)