tablero_vacio = "   C0  C1  C2\nF0   |   |   \n  ---------\nF1   |   |   \n  ---------\nF2   |   |   "
tablero = [[" "," ", " "],[" "," ", " "],[" "," ", " "]]
print('Bienvenido al juego del Tres en Ralla.')
print(tablero_vacio)
usuario = 'X'
maquina = '0'
terminar = False
continuar = True
turno = usuario 
print ('Su ficha es', usuario, '. Yo jugaré con', maquina)
print('tuno de', usuario)
print('¿Donde quiere poner?')
fila_inp = int(input('Seleccione Fila (0, 1, 2): '))
columna_inp = int(input('Seleccione Columna (0, 1, 2): '))
if fila_inp == 0 and columna_inp == 0 :
    tablero[0][0] = 'X'
    print("   C0  C1  C2\nF0 X |   |   \n  ---------\nF1   |   |   \n  ---------\nF2   |   |   ")
elif fila_inp == 0 and columna_inp == 1 :
    tablero[0][1] = 'X'
    print("   C0  C1  C2\nF0   | X |   \n  ---------\nF1   |   |   \n  ---------\nF2   |   |   ")
elif fila_inp == 0 and columna_inp == 2 :
    tablero[0][2] = 'X'
    print("   C0  C1  C2\nF0   |   | X \n  ---------\nF1   |   |   \n  ---------\nF2   |   |   ")
elif fila_inp == 1 and columna_inp == 0 :
    tablero[1][0] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1 X |   |   \n  ---------\nF2   |   |   ")
elif fila_inp == 1 and columna_inp == 1 :
    tablero[1][1] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1   | X |   \n  ---------\nF2   |   |   ")
elif fila_inp == 1 and columna_inp == 2 :
    tablero[1][2] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1   |   |X  \n  ---------\nF2   |   |   ")
elif fila_inp == 2 and columna_inp == 0 :
    tablero[2][0] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1   |   |   \n  ---------\nF2 X |   |   ")
elif fila_inp == 2 and columna_inp == 1 :
    tablero[2][1] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1   |   |   \n  ---------\nF2   | X |   ")
elif fila_inp == 2 and columna_inp == 2 :
    tablero[2][2] = 'X'
    print("   C0  C1  C2\nF0   |   |   \n  ---------\nF1   |   |   \n  ---------\nF2   |   | X ")
else :
    print('Es invalido')
for fila in range(2):
    for columna in range(1):
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = maquina
            print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )
            break
if tablero[0][0] == tablero[0][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "X":
    print("Ganaste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "X":
    print("Ganaste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[0][1] == tablero[0][2] == "0":
    print("Perdiste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "0":
    print("Perdiste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "0":
    print("Perdiste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "0":
    print("Perdiste")
else :
    turno2f = int(input('Seleccione Fila (0, 1, 2): '))
    turno2c = int(input('Seleccione Columna (0, 1, 2): '))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ' and turno2f == 0 and turno2c == 0: 
                tablero[0][0] = 'X'
            elif turno2f == 1 and turno2c == 1: 
                tablero[1][1] = 'X'
            elif turno2f == 2 and turno2c == 2: 
                tablero[2][2] = 'X'
            elif turno2f == 0 and turno2c == 1: 
                tablero[0][1] = 'X'
            elif turno2f == 0 and turno2c == 2: 
                tablero[0][2] = 'X'
            elif turno2f == 1 and turno2c == 2: 
                tablero[1][2] = 'X'
            elif turno2f == 1 and turno2c == 0: 
                tablero[1][0] = 'X'
            elif turno2f == 2 and turno2c == 1: 
                tablero[2][1] = 'X'
            elif turno2f == 2 and turno2c == 0: 
                tablero[2][0] = 'X'
            else :
                print('Es invalido')
            break
    print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )

for fila in range(3):
    for columna in range(3):
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = maquina
            print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )
            break
if tablero[0][0] == tablero[0][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "X":
    print("Ganaste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "X":
    print("Ganaste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[0][1] == tablero[0][2] == "0":
    print("Perdiste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "0":
    print("Perdiste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "0":
    print("Perdiste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "0":
    print("Perdiste")
else :
    turno2f = int(input('Seleccione Fila (0, 1, 2): '))
    turno2c = int(input('Seleccione Columna (0, 1, 2): '))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ' and turno2f == 0 and turno2c == 0: 
                tablero[0][0] = 'X'
            elif turno2f == 1 and turno2c == 1: 
                tablero[1][1] = 'X'
            elif turno2f == 2 and turno2c == 2: 
                tablero[2][2] = 'X'
            elif turno2f == 0 and turno2c == 1: 
                tablero[0][1] = 'X'
            elif turno2f == 0 and turno2c == 2: 
                tablero[0][2] = 'X'
            elif turno2f == 1 and turno2c == 2: 
                tablero[1][2] = 'X'
            elif turno2f == 1 and turno2c == 0: 
                tablero[1][0] = 'X'
            elif turno2f == 2 and turno2c == 1: 
                tablero[2][1] = 'X'
            elif turno2f == 2 and turno2c == 0: 
                tablero[2][0] = 'X'
            break
    print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )
if tablero[0][0] == tablero[0][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "X":
    print("Ganaste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "X":
    print("Ganaste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[0][1] == tablero[0][2] == "0":
    print("Perdiste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "0":
    print("Perdiste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "0":
    print("Perdiste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "0":
    print("Perdiste")
else :
    turno2f = int(input('Seleccione Fila (0, 1, 2): '))
    turno2c = int(input('Seleccione Columna (0, 1, 2): '))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ' and turno2f == 0 and turno2c == 0: 
                tablero[0][0] = 'X'
            elif turno2f == 1 and turno2c == 1: 
                tablero[1][1] = 'X'
            elif turno2f == 2 and turno2c == 2: 
                tablero[2][2] = 'X'
            elif turno2f == 0 and turno2c == 1: 
                tablero[0][1] = 'X'
            elif turno2f == 0 and turno2c == 2: 
                tablero[0][2] = 'X'
            elif turno2f == 1 and turno2c == 2: 
                tablero[1][2] = 'X'
            elif turno2f == 1 and turno2c == 0: 
                tablero[1][0] = 'X'
            elif turno2f == 2 and turno2c == 1: 
                tablero[2][1] = 'X'
            elif turno2f == 2 and turno2c == 0: 
                tablero[2][0] = 'X'
            else :
                print('Es invalido')
            break
    print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )

for fila in range(3):
    for columna in range(3):
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = maquina
            print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )
            break
if tablero[0][0] == tablero[0][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "X":
    print("Ganaste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "X":
    print("Ganaste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "X":
    print("Ganaste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "X":
    print("Ganaste")
elif tablero[0][0] == tablero[0][1] == tablero[0][2] == "0":
    print("Perdiste")
elif tablero[1][0] == tablero[1][1] == tablero[1][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[2][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][0] == tablero[2][0] == "0":
    print("Perdiste")
elif tablero[0][1] == tablero[1][1] == tablero[2][1] == "0":
    print("Perdiste")
elif tablero[0][2] == tablero[1][2] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[0][0] == tablero[1][1] == tablero[2][2] == "0":
    print("Perdiste")
elif tablero[2][0] == tablero[1][1] == tablero[0][2] == "0":
    print("Perdiste")
else :
    turno2f = int(input('Seleccione Fila (0, 1, 2): '))
    turno2c = int(input('Seleccione Columna (0, 1, 2): '))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ' and turno2f == 0 and turno2c == 0: 
                tablero[0][0] = 'X'
            elif turno2f == 1 and turno2c == 1: 
                tablero[1][1] = 'X'
            elif turno2f == 2 and turno2c == 2: 
                tablero[2][2] = 'X'
            elif turno2f == 0 and turno2c == 1: 
                tablero[0][1] = 'X'
            elif turno2f == 0 and turno2c == 2: 
                tablero[0][2] = 'X'
            elif turno2f == 1 and turno2c == 2: 
                tablero[1][2] = 'X'
            elif turno2f == 1 and turno2c == 0: 
                tablero[1][0] = 'X'
            elif turno2f == 2 and turno2c == 1: 
                tablero[2][1] = 'X'
            elif turno2f == 2 and turno2c == 0: 
                tablero[2][0] = 'X'
            break
    print('   C0  C1  C2\nF0 ', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '\n   ---------\nF1 ', tablero[1][0], '|', tablero[1][1], '|' , tablero[1][2], '\n   ---------\nF2 '  , tablero[2][0], '|', tablero[2][1], '|', tablero[2][2] )