# Tablero de juego
tabla = [' '] * 9

# Jugador actual (X o O)
jugador = 'X'

tablero_X = [0] * 9
tablero_O = [0] * 9

# Indicador de si el juego ha terminado
juego_terminado = False

# Función para imprimir el tablero
def imprimir_tablero():
    print(tabla[0] + '|' + tabla[1] + '|' + tabla[2])
    print('-+-+-')
    print(tabla[3] + '|' + tabla[4] + '|' + tabla[5])
    print('-+-+-')
    print(tabla[6] + '|' + tabla[7] + '|' + tabla[8])

# Bucle principal del juego
while not juego_terminado:
    imprimir_tablero()
    tablero_en_juego = tablero_X
    if jugador == 'O':
        tablero_en_juego = tablero_O
    
    # Solicitar la jugada al jugador
    jugada = int(input(f'Jugador {jugador}, elige una casilla (0-8): '))
    
    # Verificar si la casilla está disponible
    if tabla[jugada] == ' ':
        tabla[jugada] = jugador
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
        print(f'¡Jugador {jugador} ha ganado!')
        juego_terminado = True
    
    # Verificar empate
    elif ' ' not in tabla:
        imprimir_tablero()
        print('¡Es un empate!')
        juego_terminado = True
    
    # Cambiar al siguiente jugador
    jugador = 'O' if jugador == 'X' else 'X'