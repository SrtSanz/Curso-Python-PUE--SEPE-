#El objetivo es crear un tres en raya funcional sin usar funciones, por consiguiente
#con lo que hemos visto en clase
# 1º Como pintar el tablero
#  x | X | 0
# ---*---*---
#  x | X | 0
# ---*---*---
#  x | X | 0
#Tip usar el print y poner tantos prints como filas tenemos
#2º Como almacenar los movimientos del tablero
#Tip es usar una matriz, de 3 x 3, que debemos a vacio y luego guardaremos los movimienos
# tablero = [[" "," ", " "],[" "," ", " "],[" "," ", " "]]
#tablero[0] => primera fila
#tablero[1] => segunda fila
#tablero[2] => tercera fila
#un indidididual
#tablero[1][0] => primer elemento de la segunda fila
#3º Introducir el usuario el movimiento
#Dos opciones la primera y mas sencilla es pedirle las coordenadas
# fila 0 columna 1
# tablero[0][1] = "X"
#Vamos a presuponer que el ser humano juega con X y la maquina con 0
#NO podemos dejar mover en una casilla que ya esta ocupada
# para saber si una casilla esta vacia comprobareos con un " "
#4º Mover la maquina
# la maquina jugarra siempre en el primer hueco disponible, es decir buscaremos
#cual es la primera posicion vacia y jugara en esa casilla
#para esto precisareis dos bucles
# Tip, dos bucles para recorrer
# for fila in range(3):
#   for columnas in range(3):
#       if tabler[fila][columna] = " ":
#           print("casilla libre")
#            tablero[fila][columna] = "0"
#            break
#5º debemos jugar hasta que alguien gane o nos quedemos sin casillas libres
# para saber si alguien gana debemos comprobar 8 casos
# Tip como imprimir el tabler debeis crear un if por cada posible combinacion de vistoria
# if tablero[0][0] == tablero[0][1] == tablero[0][2] == "X":
#   print("toda la primera fila son X, gana el usuario")
#jugar hasta que no queden casillas libres o ganar debeis usar un bucle while
#que compruebe esas condiciones