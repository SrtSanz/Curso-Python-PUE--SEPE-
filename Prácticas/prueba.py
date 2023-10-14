# Tablero de juego
tablero = [' '] * 9

# Jugador actual (X o O)
jugador_actual = 'X'

tablero_X = [0] * 9
tablero_O = [0] * 9

# Indicador de si el juego ha terminado
juego_terminado = False

# Función para imprimir el tablero
def imprimir_tablero():
    print(tablero[0] + '|' + tablero[1] + '|' + tablero[2])
    print('-+-+-')
    print(tablero[3] + '|' + tablero[4] + '|' + tablero[5])
    print('-+-+-')
    print(tablero[6] + '|' + tablero[7] + '|' + tablero[8])

# Bucle principal del juego
while not juego_terminado:
    imprimir_tablero()
    tablero_en_juego = tablero_X
    if jugador_actual == 'O':
        tablero_en_juego = tablero_O
    
    # Solicitar la jugada al jugador
    jugada = int(input(f'Jugador {jugador_actual}, elige una casilla (0-8): '))
    
    # Verificar si la casilla está disponible
    if tablero[jugada] == ' ':
        tablero[jugada] = jugador_actual
        tablero_en_juego[jugada] = 1
    else:
        print('Casilla ocupada. Inténtalo de nuevo.')
        continue
    
    # Verificar si hay un ganador
    if (tablero_en_juego[0] + tablero_en_juego[1] + tablero_en_juego[2] == 3 or
        tablero_en_juego[3] + tablero_en_juego[4] + tablero_en_juego[5] == 3 or
        tablero_en_juego[6] + tablero_en_juego[7] + tablero_en_juego[8] == 3 or
        tablero_en_juego[0] + tablero_en_juego[3] + tablero_en_juego[6] == 3 or
        tablero_en_juego[2] + tablero_en_juego[5] + tablero_en_juego[8] == 3 or
        tablero_en_juego[1] + tablero_en_juego[4] + tablero_en_juego[7] == 3 or
        tablero_en_juego[0] + tablero_en_juego[4] + tablero_en_juego[8] == 3 or
        tablero_en_juego[2] + tablero_en_juego[4] + tablero_en_juego[6] == 3):
        imprimir_tablero()
        print(f'¡Jugador {jugador_actual} ha ganado!')
        juego_terminado = True
    
    # Verificar empate
    elif ' ' not in tablero:
        imprimir_tablero()
        print('¡Es un empate!')
        juego_terminado = True
    
    # Cambiar al siguiente jugador
    jugador_actual = 'O' if jugador_actual == 'X' else 'X'