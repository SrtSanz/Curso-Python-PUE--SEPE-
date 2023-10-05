#1. Imprimir “Hola mundo” por pantalla.
print("hola mundo")

#Opcion B
cadena = "Hola Mundo"
print(cadena)

#2. Crear dos variables numéricas, sumarlas y mostrar el resultado
numero_1 = 12
numero_2 = 34

suma = numero_1 + numero_2

print(suma)

#Opcon B
numero_1 = 12
numero_2 = 34

print(numero_1 + numero_2)

#opcion Cno cumple enunciado

print(12 + 5)


#3. Mostrar el precio del IVA de un producto con un valor de 100 y su precio final, 
# suponiendo que el IVA 21%.
precio_sin_iva = 100
porcetaje_iva = 21

iva = precio_sin_iva *(porcetaje_iva/100)
precio_total = precio_sin_iva + iva

print(iva)
print(precio_total)

#Marcos
v_inicial = 100

iva = 0.21

v_final = v_inicial + (v_inicial*iva)

print(v_final)


#Marcos C
IVA_21 = 0.21
precio = 100
IVA = IVA_21*precio
precio_total = IVA+precio

#Marshia

precio = 100
iva = 0.21
totaliva = (precio * iva)
print (totaliva + precio)

#Abddllah

iva=21
precio=100

print ("""Precio : {}$
IVA: {}
Total : {}$""".format(iva,precio,precio+precio*iva/100))

#Gonzalo
precio_sin_iva = 100
iva = precio_sin_iva * 21/100
precio_final = precio_sin_iva + iva
print ("El precio del IVA es:", iva)
print ("Precio final:", precio_final)

#4. Tenemos dos cadenas la primera es "hola" y la segunda "mundo", 
#muestra ambas cadenas con un espacio entre ellas por pantalla 
#y con los 2 primeros caracteres intercambiados. 
#Por ejemplo, hola mundo pasaría a mula hondo

cadena_1 = "hola"
cadena_2 = "mundo"

dos_primeros_cadena_1 = cadena_1[0:2:1]
dos_primeros_cadena_2 = cadena_2[0:2:1]

resto_primera = cadena_1[2:len(cadena_1):1]
resto_segunda = cadena_2[2:len(cadena_2):1]

cadena_3 = dos_primeros_cadena_2 + resto_primera + " " + dos_primeros_cadena_1 + resto_segunda
print(cadena_3)

#Hector
print( 'mundo'[0:2] + 'hola'[2:]  + ' ' + 'hola'[0:2] + 'mundo'[2:])

#Abdellah
cadena1="hola"
cadena2="mundo"

print(cadena2[0:2:1]+cadena1[2:4:1] +' ' + cadena1[0:2:1]+cadena2[2:5:1])

#Mario
cadena_1 = "Hola"
cadena_2 = "Mundo"
print(cadena_2[0] + cadena_1[2:100] + " " + cadena_1[0] + cadena_2[1:100])

#Angel
Cadena_2 = "hola"
Cadena_3 = "mundo"
print("\n 4. Mostrar ambas cadenas separadas con un espacio y los 2 primeros caracteres intercambiados:")
print(Cadena_3[0:2:1]+Cadena_2[2::1]+" "+Cadena_2[0:2:1]+Cadena_3[2:len(Cadena_3):1])

#Alberto
cadena_1 = "hola"
cadena_2 = "mundo"
cadena_3 = cadena_1 + " " + cadena_2
print(cadena_3)
print(cadena_3[5:7:1]+cadena_3[2:5:1]+cadena_3[0:2:1]+cadena_3[7:10:1])

#Antonio
c1 = "Hola"
c2 = "Mundo"
c_interc = c2[:2] + c1[2:] + " " + c1[:2] + c2[2:]
print(c_interc)

#Sheila
cadena1="hola"
cadena2="mundo"
print(cadena1 + " " + cadena2)
print("mu" + cadena1[2::1] + " " + "ho" + cadena2[2::1] )

#Christian
print(str_cadena2[0:2] + str_cadena1[2:4]+ " " + str_cadena1[0:2] + str_cadena2[2:5])

#Marcos Campillo
intercambio_1 = cadena_1[0:2:1]
intercambio_11 = cadena_1[1:4:1]
intercambio_2 = cadena_2[0:2:1]
intercambio_22 = cadena_2[1:4:1]
print(intercambio_1+intercambio_22+intercambio_2+intercambio_11)


#5. Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla


#6 devolver el maximo y minimo de una lista numerica, con enteros, los valores que quieras


#7 devolver el maximo y minimo de una lista numerica, con fllotantes, los valores que quieras


#8 devolver el maximo y minimo de una lista numerica, con complejos, los valores que quieras



#9 hayar la media de los valores de una lista numerica de enteros


#10 de la cadena:
cadena = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quijana. Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
"""
#obtener los primero 50 caracteres
#obtener los 50 ultimos
#invertir la cadena
#mostrar los carateres de las posiciones pares
