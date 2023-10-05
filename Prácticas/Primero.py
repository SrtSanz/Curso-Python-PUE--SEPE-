print("Hola mundo")

  a  Todos
# Imprimir "Hola mundo" por pantalla

cadena = "Hola mundo"
print(cadena)

# crear dos variables numéricas, sumarlas y mostrar el resultado

n = 5
x = 7
print(n+x)

# Mostrar el precio del IVA de un producto con un valor de 100 y su precio con IVA

IVA_21 = 0.21
precio = 100
IVA = IVA_21*precio
precio_total = IVA+precio

# Cadenas

cadena_1 = "hola "
cadena_2 = "mundo"
print(cadena_1+cadena_2)

intercambio_1 = (cadena_1([0:2:1]))
intercambio_11 = (cadena_1([1:4:1]))
intercambio_2 = (cadena_2([0:2:1]))
intercambio_22 =(cadena_2([1:4:1]))
print(intercambio_1+intercambio_11+intercambio2+intercambio22)
A ver si lo he hecho bien

Marcos Sánchez López  a  Todos 14:51
v_inicial = 100

iva = 0.21

v_final = v_inicial + (v_inicial*iva)

print(v_final)
yo lo he puesto asi

Abdellah Nadifi  a  Todos 14:52
iva=21
precio=100

print ("""Precio : {}$
IVA: {}
Total : {}$""".format(iva,precio,precio+precio*iva/100))

Marcos Campillo Hernández  a  Todos 14:53
me han faltado los print

Hector Cols Mijares  a  Todos 14:54
print( 'mundo'[0:1] + 'hola'[1:]  + ' ' + 'hola'[0:1] + 'mundo'[1:])

Abdellah Nadifi  a  Todos 14:54
cadena1="hola"
cadena2="mundo"

print(cadena2[0:2:1]+cadena1[2:4:1] +' ' + cadena1[0:2:1]+cadena2[2:5:1])

Mario Capella Belenguer  a  Todos 14:54
cadena_1 = "Hola"
cadena_2 = "Mundo"
print(cadena_2[0] + cadena_1[1:100] + " " + cadena_1[0] + cadena_2[1:100])

Angel Gracia Gómez  a  Todos 14:54
Cadena_2 = "hola"
Cadena_3 = "mundo"
print("\n 4. Mostrar ambas cadenas separadas con un espacio y los 2 primeros caracteres intercambiados:")
print(Cadena_3[0:2:1]+Cadena_2[2:4:1]+" "+Cadena_2[0:2:1]+Cadena_3[2:5:1])

Alberto González Torres  a  Todos 14:54
cadena_1 = "hola"
cadena_2 = "mundo"
cadena_3 = cadena_1 + " " + cadena_2
print(cadena_3)
print(cadena_3[5:7:1]+cadena_3[2:5:1]+cadena_3[0:2:1]+cadena_3[7:10:1])

Antonio Jesús Salido Ranea  a  Todos 14:55
c1 = "Hola"
c2 = "Mundo"
c_interc = c2[:2] + c1[2:] + " " + c1[:2] + c2[2:]
print(c_interc)

Sheila Rodríguez Calvo  a  Todos 14:56
cadena1="hola"
cadena2="mundo"
print(cadena1 + " " + cadena2)
print("mu" + cadena1[2:4:1] + " " + "ho" + cadena2[2:5:1] )

Christian Brioso Hermosilla  a  Todos 14:56
print(str_cadena2[0:2] + str_cadena1[2:4]+ " " + str_cadena1[0:2] + str_cadena2[2:5])

Marcos Campillo Hernández  a  Todos 14:57
intercambio_1 = cadena_1[0:2:1]
intercambio_11 = cadena_1[1:4:1]
intercambio_2 = cadena_2[0:2:1]
intercambio_22 = cadena_2[1:4:1]
print(intercambio_1+intercambio_11+intercambio_2+intercambio_22)

Marcos Campillo Hernández  a  Todos 14:57
revisado

Hector Cols Mijares  a  Todos 14:58
print( 'mundo'[0:2] + 'hola'[2:]  + ' ' + 'hola'[0:2] + 'mundo'[2:])

John Alexander Restrepo Benavides  a  Todos 14:58
Profe yo el anterior el 3 lo hice asi:
inp = input('Digite Precio: ')
precio = float(inp)
IVA = (precio * 0.21)
print(IVA)

Marcos Campillo Hernández 15:02
cadena_1 = "hola "
cadena_2 = "mundo"
print(cadena_1+cadena_2)

intercambio_1 = cadena_1[0:2:1]
intercambio_11 = cadena_1[1:4:1]
intercambio_2 = cadena_2[0:2:1]
intercambio_22 =cadena_2[1:4:1]
print(intercambio_1+intercambio_11+intercambio2+intercambio22)