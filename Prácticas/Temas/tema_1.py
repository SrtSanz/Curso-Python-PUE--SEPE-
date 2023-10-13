#Esto es un comentario, es una linea que el intérprete ignora
#se usa habitualmente para dejar notas en el codigo
#Creacion de variables
#identificador = valor
valor = 10

#En python los identificadores tienen ciertas reglas:
# solo pueden tener letras, numeros y "_"
# solo pueden empezar por letras y "_", no por numeros
variable = 10
_variable = 10
#No es valido
10variable= 10
#si es valido que el numero este pero no al principio
variable_10 = 10 
#tampoco son validos
$variable = 10
variable! = 10

#Python es un lenguaje tipado o no tipado?
#Python es un lenguaje FUERTEMENTE TIPADO, todas las variables en Python tienen un tipo
#Lo que sucede es que nosotros NO le asignamos el tipo a las variables sino que es python
#automaticamente lo hace por nosotros, esto se llama DuckTyping
valor = 10
#En python tenemos la función print(), que imprime lo que recibe como argumento.
print("Hola Mundo")

#Además de la funcion print tenemos otra función que es type() que devuelve el tipo de dato
#de la variable que le pasemos como argumento.
numero = 10
print(type(numero))
print(numero)

#Tipos primitivos son aquellos que vienen incluidos en Python por defecto
#Enteros
numero = 10
print(type(numero))
print(numero)

#Caracteristicas
#Estan pensados para enteros tantos positivos como negativos.
#El Rango, son los numeros comprendidos entre el más alto y más bajo que podemos representar.
#No hay limite entorno al valor máximo ni mínimo, depende de la arquitectura y del intérprete.
numero = 9121929128947957948279452798345793475894537945794573475354897534897345897345897934857349793485798354798534798347598345798534082133201932109832108321987349745298742943728934729834724328098432084320840938279847972347432947389237489327943798342798437439287438927342
print(type(numero))
print(numero)

#Por defecto trabajamos en base decimal (0-9)
#python soporta otras bases
#Binario que sólo tenemos dos símbolos 0 y 1 por consiguiente es base 2
#para indicar que un numero es binario en python le ponemos 0b delante
binario = 0b101
print(type(binario))
print(binario)
#Vemos el resultado en decimal que es 5
#primer paso separamos y sumamos cada cifra
# 0b101 = 1 + 0 + 1
#Segundo paso multiplicamos cada cifra por la base (en este caso es 2)
# 0b101 = 1 * 2 + 0 * 2 + 1 * 2
#Tercer Paso, elevo cada base a la potencia determinada por su posicion empezando en 0
# de derecha a izquierda
# 0b101 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0
#Último paso hacemos la cuenta
# 0b101 = 1 * 4 + 0 * 2 + 1 * 1 = 4 + 0 + 1 = 5
#Octal que es base 8, tenemos desde el 0 al 7
#se idica con un 0o
octal = 0o101
print(type(octal))
print(octal)
#Para la conversion es igual que con binario sólo que cambiamos la base 2 por una base 8
#separo cifras y sumo
# 0o101 = 1 + 0 + 1
#Multipplico por la base
# 0o101 = 1 * 8 + 0 * 8 + 1 * 8
#Elevamos a la poyencia
# 0o101 = 1 * 8^2 + 0 * 8^1 + 1 * 8^0
#Hacemos la cuenta
# 0o101 = 64 + 0 + 1  = 65
#Hexadecimal, que tenemos 16 símbolos del 0 al 9 y de la A a la F
#se indica poniendo un 0x al principio
hexadecimal = 0x101
print(type(hexadecimal))
print(hexadecimal)
#El 257 igual que las otras conversiones
# 0x101 = 1 * 16^2 + 0 * 16^1 + 1 * 16^0
# 0x101 = 1 * 256 + 0 * 16 + 1 * 1 = 256 + 0 + 1 = 257

#Flotantes
#Son mumeros con decimales
flotante = 1.3
print(type(flotante))
print(flotante)

#Caracteristicas
#Rango
#La precisión máxima es de 17 difgitos, corta la salida y NO avisa
flotante = 1.27868236871364364832764527862445876476453734598345784538893457932809438934028093428430284320834203820438082348432098342038420342803492830249823508052489
print(type(flotante))
print(flotante)

#admite notación científica
flotante = 1.23e3 #es mltiplicar por 10 elevado a la potencia que viene después de la e es decir 3
print(type(flotante))
print(flotante)
#puede ser negativo en ese caso es como dividir.
flotante = 1.23e-3
print(type(flotante))
print(flotante)

#operaciones OJO con el tema del redondeo
print(1.1 + 1.2)
#NO AVISA
print(0.1 + 0.1 + 0.1 - 0.3 )

#Complejos
#Aquellos que tienen parte real y parte imaginaria
complejo = 4 + 5j
print(type(complejo))
print(complejo)

#Booleanos que son aquellos que pueden ser verdadero (True) o falso (False)
verdadero = True #Python es case sensitive es decir diferencia mayúscualas de minúsculas
                 #true no es igual que True
print(type(verdadero))
print(verdadero)

falso = False
print(type(falso))
print(falso)

# Python dentro de los tipos de datos los clasifia de dos formas:
# INMUTABLES, son aquellos que no se pueden modificar una vez creados.
# MUTABLES, son aquellos que si se pueden modificar una vez creados.

#INMUTABLES => enteros, flotantes, complejos, tuplas, string, booleanos.
#MUTABLES => listas, diccionarios y conjuntos.

entero = 100
print(entero)
entero = 500
print(entero)

#Tenemos una funcion id() que devuelve el identificador único de una variable en python
entero = 100
print(id(entero))
entero = 500
print(id(entero))
#Otro ejemplo
entero = 100
print(id(entero))
entero_2 = entero
entero = 500
#ids distintos
print(id(entero))
print(id(entero_2))

#SOn todos iguales, reutiliza la memoria lo mejor posible
entero_1 = 100
entero_2 = 100
print(id(entero_1))
print(id(entero_2))

#Strings
#Los strings son un conjunto de caracteres
#en python no existe el tipo char, sino que es un string de longitud 1
#los strings en python son INMUTABLES
#Tenemos 4 formas de declarar strings en python
#Comillas dobles
cadena_1 = "Hola mundo"
print(type(cadena_1))
print(cadena_1)
#comillas simples
cadena_2 = 'Hola mundo'
print(type(cadena_2))
print(cadena_2)
#Comillas triples dobles
cadena_3 = """Hola mundo"""
print(type(cadena_3))
print(cadena_3)
#Comillas triples simples
cadena_4 = '''Hola mundo'''
print(type(cadena_4))
print(cadena_4)

#OJO Las comillas triples NO son comentarios
#la unica forma de hacer comentarios es con las #
"""
esto es un comentario

"""

#Si hay diferencia entre las versiones simples (dobles y sencillas) y las tripes(dobles y sencillas)
#Las triples habilitan la sintaxis Heredoc, que es una sintaxis que te permite literales (multilinea)

cadena = "Hola
que 
tal"
print(cadena)

cadena = """Hola
que
tal
"""
print(cadena)

#Para un multilinea en un string con dobles o sencillas hay que usar \n \t \r
cadena = "Hola\nque\ntal"
print(cadena)

#Podemos acceder a cada letra por su pocición comenzando en 0 y usando []
cadena = "Hola Mundo"
print(cadena[0])
print(cadena[1])
print(cadena[2])
#Ojo la posicion debe existir sino error
print(cadena[20])

#Son inmutables, NO se pueden cambiar letras sueltas o toda la cadena o nada
cadena = "Hola Mundo"
cadena[0] = "h"
print(cadena)

#Los string soportan el operador +, en este caso concatenaría cadenas, es decir, las junta.
cadena_1 = "hola"
cadena_2 = " mundo"
cadena_3 = cadena_1 + cadena_2
print(cadena_3)

#También soporta el operador *, que se usa con un string y un entero
cadena_1 = "hola"
cadena_2 = 10 * cadena_1
print(cadena_2)

#Son objetos y tienen métodos y también funciones que se le aplican
# la primera es len() que nos devuelve la longitud.
cadena = "hola mundo"
print(len(cadena))

#luego tenemos multitud de métodos, que devuelven copias modificadas
cadena = "hola Mundo"
#tenemos de formato
#lower() lo cambia a minúsculas
print(cadena.lower())
#upper() a mayúsculas
print(cadena.upper())
#capitalize(), pone sólo la primera letra en mayúsculas
print(cadena.capitalize())

#Tenemos métodos de comprobacion que empiezan por is.
#Sirven para comprobr si una cadena cumple algo devuelven verdero o falso
# isupper(), islower(), isdigit(), isalpha(), isnumeric()...
cadena = "hola Mundo"
print(cadena.isupper())
print(cadena.islower())
print(cadena.isnumeric())

#Tenemos que soportan slicing, que es una forma de obtener subconjuntos de datos de un tipo compuesto (strings, tuplas, listas)
#En el caso de los strings nos devueven substrings
# cadena[POS_INI:POS_FIN:STEP]
#POS_INI, es la posición de inicio del subconjutno por defecto es 0
#POS_FINAL, es la posicion final del subconjunto, OJO no se incluye en el resultado asi que en realidad
# es POS_FINAL - 1, y su valor por defecto es la longitud de la cadena.
#STEP, es el salto entre cada uno de los elementos del conjunto por defecto es 1.
cadena = "Hola Mundo"
print(cadena[0:10:1]) #copia todo
print(cadena[0:10:2]) #Hl ud el step hace que salte de dos en dos
print(cadena[5:10:1]) #Mundo
print(cadena[0:4:1]) #Hola

#OJO NO comprueba los límites
cadena = "Hola Mundo"
print(cadena[0:4:10000])#H la posición del salto es más grande que la longitud. Sólo saca el primer caracter.
print(cadena[0:4000:1])#po_fin > len llega solo hasta el final no da error.
print(cadena[4000:10:1]) #cadena vacía.

#ojo en python los strings admiten posiciones negativas.
cadena = "Hola Mundo"
print(cadena[0])
print(cadena[-1]) #empieza por el final

#También se aplica con los slices
cadena = "Hola Mundo"
print(cadena[-1:-10:1]) #OJO cadena vacia no puedo ir de -1 a -10 sumando 1
print(cadena[-1:-11:-1]) #STEPS negativos cuenta de atrás hacia adelante (invierte la cadena)
print(cadena[-5:-11:-1]) #M aloH
print(cadena[5:-1:-1]) #cadena vacía
print(cadena[5:-1:1]) #Mund

#También tenemos funciones que se le pueden aplciar a los string
#len() que nos devuelve la longtud de la cadena.
cadena = "Hola Mundo"
print(len(cadena))
#Tenemos 2 funciones más que SÓLO se pueden utilizar con strings de longitud uno "letras" sueltas
# ord(), le pasamos un caracter y nos devuelve su codigo ascii asociado
print(ord("a"))
# chr(), pasando un codigo ascii, nos devuelve la letra asociada
print(chr(65))

#Operadores
#Aritméticos, lógicos y binarios
#Aritméticos
print(1 + 2) #suma
print(1 - 2) #resta
print(1 * 2) #multiplación
print(1 / 2) #división
print(1 ** 2) #potencia
print(1 % 2) #modulo, esto es el resto de la division entera
print(1 // 2) #cociente de la division entera

#Logicos, son los que operan con Booleanos
# and, or y not
#And solo es verdad si ambos operandos son verdad
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#Or, es verdad si al menos uno de los operandos es verdad
print(False or False)
print(False or True)
print(True or False)
print(True or True)

#Not, convierte verdadero en falso y al reves
print(not True)
print(not False)

#Operadores Binarios
# & (and), | (or), ~ (not), ^ (or exclusivo), <<(desplaza izq), >> (desplazamiento der)

# &
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

#|
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

#OJO NO es lo mismo and y & ni | con or
print(10 & 5)
#Ojo trabajan a nivel de bit
#10 = 1010
#05 = 0101
# & = 0000 = 0

print(10 | 5)

#10 = 1010
#05 = 0101
# | = 1111 = 15

# ~, es la negacion
print(~0)
print(~1)

#El binario no se lleva muy alla con los negativos
# Signo Magnitud
# Al numero en positivo le agregamos un bit mas al principio que sera el bit de signo
# 0 => +
# 1 => -
# + 1 => 0001
# - 1 => 1001
#Dos problemas es una cuenta dificil para un PC
#ademas tenemso 2 ceros
# + 0 => 0 000
# - 0 => 1 000
# Complemento a uno
# Negamos bit a bit
# 1 =>        0001
# -1 en C1 => 1110
# Es ua cuenta rapida para ls PC, pero
#seguimos teniendo dos ceros
# + 0 => 0000
# - 0 => 1111
#Complemento a 2
#es hacer el complemento a uno y al resultado sumarle uno
# + 1 => 0001
# Primero en C1
# - 1 => 1110
#ahora le sumamos uno
# -1 = 1111
#Ventajas es rapido para un PC
#Y ya no hay 2 ceros
# + 0 = 0000
# - 0 = 0000
# Python trabaja en C1 pero al imprimir usa C2
# En C1
#0 = 1111
#En C2
#0 = 0000
#En C1
#-1 = 1110
#En C2
#-1 = 1111
#En C1
#-2 = 1101
#En C2
#-2 = 1110 

# ^
print(0 ^ 0) #0
print(0 ^ 1) #1
print(1 ^ 0) #1
print(1 ^ 1) #0

#Se usa para criptografia de clave simetrica
mensaje = 10
clave = 5
cifrado = mensaje ^ clave
print(cifrado)
descifrado = cifrado ^ clave
print(descifrado)

#Desplazamientos
print(1 << 2)
#1 = 0001
#1 << 2 => 0001 00 = 000100 = 4
#se añaden ceros a la derecha

#e añaden a la izquierda y perdemos tantas cifras significativas a la derecha como ceros añadimos por la izquierda
print(1 >> 2)
#1 = 0001
#1 >> 2 => 0001 => 00 00 01 = 0000

#Nos toca hablar de listas, tuplas, diccionarios y conjuntos
#Listas
# Las listas son un conjunto ordenado de elementos que admiten cualqueir tipo de dato
#en python y son MUTABLES
#para declrar las listas usamos []
lista = [1,2,3,4]
print(type(lista))
print(lista)
#NO tiene por que ser homogeneas
lista = [1,2,3,4,"hola",3.5,1 + 5j]
print(type(lista))
print(lista)
#Podemos acceder a los elementos por posicion igual que en los string
lista = [1,2,3,4]
print(lista[0])
print(lista[2])

#Son mutables asi que podemos modificar, añadir y eliminar elementos
#Modificar
lista = [1,2,3,4]
lista[0]= "Hola"
print(lista)

#para ñadir nuevos
# append() que añade al final
lista = [1,2,3,4]
lista.append("Hola")
print(lista)
#insert() que admite dos parametros uno es la posicion de insercion y el otro el objeto a insertar
lista = [1,2,3,4]
lista.insert(2,"Hola")
print(lista)

#Borrar
#operador del e iriamos por posicion
lista = [1,2,3,4]
del lista[0]
print(lista)
#El metodo reove que elimina por valor y solo la primera ocurrencia
lista = [1,2,3,4]
lista.remove(4)
print(lista)

#Podemos aplicarle el operador in para saber si un elemento existe
lista = [1,2,3,4]
print(2 in lista)
print("hola" in lista)

#tenemos metodos y funciones que se le aplican
# len(), devuelve la longitud
lista = [1,2,3,4]
print(len(lista))

#tenemos funciones que solo funcionan con listas numericas
#max(), maximo
#min(), minimo
#sum(), suma de los elementos
lista = [1,2,3,4]
print(max(lista))
print(min(lista))
print(sum(lista))

#Tenemos un metodo en string que devuelve una lista, split(), que devuelve una lista
#con los elementos diferenciados que obtine a partir del caracter de particion que recibe como argumento
fecha = "12/02/2023"
partes = fecha.split("/")
print(partes)

#Tenemos la inversa que es join() que une los elementos de una lista de strings a un unico string
lista = ["hola","adios","que"]
unidos = "PEGAMENTO".join(lista)
print(unidos)

#Podemos ordenar listas numericas y de cadenas
#sort() pr defecto de menor a mayor, se puede alterar pasandole un argumento ord
lista = [1,22,3,42,-1,3]
lista.sort()
print(lista)
#Funciona y ordena en base a la tabla ascii (numeros/MAYUSCULAS/MINUSCULAS)
lista = ["z","a","f","c"]
lista.sort()
print(lista)
#Podemos invertir
lista = [1,2,3,45,6]
lista.reverse()
print(lista)
#quivale al slice
print(lista[::-1])

#podemos limpiar la lista, es decir vaciarla de todos sus elementos
lista = [1,2,3,4]
lista.clear()
print(lista)

#borrar la variable
del lista

#Tuplas
#Son lo mismo que una lista pero en INMUTABLE
#es ecir tienen todos los metodos y funciones menos las que modifiquen sus valores
#se definen con ()
tupla = (1,2,3,4)
print(type(tupla))
print(tupla)

#Diccionarios
# Los diccionarios son estructuras de datos compuestos por conjuntos de pares clave:valor
#los diccionarios NO tienen orden, son MUTABLES y las claves no se pueden repetir
#se definen usando {}
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(type(diccionario))
print(diccionario)

#Para accder a los valores hay 2 formas
#a través de la clave, las claves pueden ser strings, numeros o cualquier objteo en python que sea serializable es decir que se pueda convertir en un string
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario["nombre"])

diccionario = {0:"cero", 1000:23232323}
print(diccionario[1000])

#la otra opcion de acceder es el metodo get
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario.get("nombre"))

#La diferencia es si no existe la clave
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario["pais"]) #Error
print(diccionario.get("pais")) #None por defecto

#y el get podemos personalizar que quieres que devuelva en luagr del None con el segundo argumento
diccionario = {"nombre":"Jane","apellido":"Doe"}
defecto = "LA CLAVE NO EXISTE"
print(diccionario.get("pais", defecto))

#Para eso hacemos una lista de diccionarios
personas = [{"nombre":"Jane","apellido":"Doe"}, {"nombre":"James","apellido":"Bond"}]

#Modificar valores y añadir es igual, la diferencia si la clave existe o no
#si la clave ya existe sobrescribimos el valor
#en caso contrario, crea
#Modificar
diccionario = {"nombre":"Jane","apellido":"Doe"}
diccionario["nombre"] = "PACO"
print(diccionario)

#Añadir
diccionario = {"nombre":"Jane","apellido":"Doe"}
diccionario["pais"] = "USA"
print(diccionario)

#Eliminar
# con del y la clave
diccionario = {"nombre":"Jane","apellido":"Doe"}
del diccionario["nombre"]
print(diccionario)

#método pop()
diccionario = {"nombre":"Jane","apellido":"Doe"}
diccionario.pop("nombre")
print(diccionario)

#el método pop() devuelve el valor borrado que lo podriamos usar
diccionario = {"nombre":"Jane","apellido":"Doe"}
valor_borrado=diccionario.pop("nombre")
print(diccionario)
print(valor_borrado)

#Podmeos usar el in para saber si una clave está en un diccionario
diccionario = {"nombre":"Jane","apellido":"Doe"}
print("pais" in diccionario)
print("nombre" in diccionario)

#Métodos

#keys() devuelve un iterable con las claves
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario.keys())
#values() devuele un iterable con los valroes
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario.values())
#items() devuelve los pares valor como tuplas
diccionario = {"nombre":"Jane","apellido":"Doe"}
print(diccionario.items())

#Conjuntos
# Una serie de elementos, no reptidos que no tienen orden y son mutables
#se definen con {}
conjunto = set()
print(type(conjunto))
print(conjunto)

conjunto = {1,2,3}
print(type(conjunto))
print(conjunto)

#Pero tienen el álgebra de conjuntos implementada
automoviles = {"BMW", "SEAT", "AUDI"}
motos = {"BMW","HONDA","KAWA"}

print(automoviles & motos) # intersección
print(automoviles | motos) # unión
print(automoviles - motos) # diferencia