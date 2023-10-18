#1. Imprimir “Hola mundo” por pantalla.
print("Hola Mundo")

#2. Crear dos variables numéricas, sumarlas y mostrar el resultado
numero_1 = 10
numero_2 = 30

resultado = numero_1 + numero_2

print(resultado)

#3. Mostrar el precio del IVA de un producto con un valor de 100 
# y su precio final.

precio_sin_iva = 100
tipo_iva = 0.21

importe_iva = precio_sin_iva * tipo_iva
importe_total = precio_sin_iva + importe_iva

print(importe_iva)
print(importe_total)


#4. De dos números, saber cual es el mayor.
numero_1 = 20
numero_2 = 30

if numero_1 > numero_2:
    print("Numero 1 es mayor")
elif numero_2 > numero_1:
    print("Numero 2 es mayor")
else:
    print("So iguales")

#Opcion B
numero_1 = 20
numero_2 = 30

if numero_1 > numero_2:
    print("Numero 1 es mayor")
else:
    print("Numero 2 es mayor o igual")

#Opcion C
numero_1 = 20
numero_2 = 30
lista = [numero_1, numero_2]
print(max(lista))



#5. Crea una variable numérica y si esta entre 0 y 10,
#  mostrar un mensaje indicándolo.
numero = 7
if(numero >= 0 and numero <= 10):
    print("El numero esta entre 0 y 10")

#Opcion B
numero = 7
if(0 <= numero <= 10):
    print("El numero esta entre 0 y 10")

#6. Mostrar con un while los números del 1 al 100.
numero = 1

while numero <=100:
    print(numero)
    numero = numero + 1

#Opcion B
numero = 1

while numero <100:
    print(numero)
    numero = numero + 1
else:
    print(numero)

#7. Mostrar con un for los números del 1 al 100.

for numero in range(1,101):
    print(numero)

#Opcion B
for numero in range(1,100):
    print(numero)
else:
    print(100)

#Opcion D
numero = 1

for temp in range(1,101):
    print(numero)
    numero = numero + 1

#8. Mostrar los números pares entre 1 al 100.
for numero in range(1,101):
    if numero % 2 == 0:
        print(numero)

#Opcion B
for numero in range(2,101,2):
    print(numero)

#opcion B prima
print(list(range(2,101,2)))

#Opcion D
lista = [numero for numero in range(1,101) if numero % 2 ==0]
print(list(lista))

#Opcion E
lista = [numero for numero in range(2,101,2)]
print(list(lista))


#9. Mostrar los caracteres de la cadena “Hola mundo”.

for letra in "Hola Mundo":
    print(letra)

#Opcion B
cadena = "Hola Mundo"
for letra in cadena:
    print(letra)

#Opcion C
print("\n".join(list("Hola Mundo")))

#10. Mostrar los caracteres de la cadena “Hola mundo” al reves.

for letra in "Hola Mundo"[::-1]:
    print(letra)

#Opcion B
cadena = "Hola Mundo"
for letra in cadena[::-1]:
    print(letra)

#Opcion C
print("\n".join(list("Hola Mundo")[::-1]))

#indices negativos
cadena = "Hola Mundo"
for indice in range(-1,-len(cadena),-1):
    print(cadena[indice])

#11. Generar un rango entre 0 y 10

range(11)

#Opcion A
rango = range(11)
print(list(rango))

#opcion B
for numero in range(11):
    print(numero)

#12. Pide dos cadenas por teclado, 
# muestra ambas cadenas con un espacio entre ellas y 
# con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula hondo
cadena_1 = input("Introduce primera cadena ")
cadena_2 = input("Introduce segunda cadena ")

dos_primeros_cadena_1 = cadena_1[0:2:1]
dos_primeros_cadena_2 = cadena_2[0:2:1]

resto_primera = cadena_1[2:len(cadena_1):1]
resto_segunda = cadena_2[2:len(cadena_2):1]

cadena_3 = dos_primeros_cadena_2 + resto_primera + " " + dos_primeros_cadena_1 + resto_segunda
print(cadena_3)

#13. Juguemos al juego de adivinar el numero, generaremos un número 
# entre 1 y 100.
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si 
# es mayor o menor que el número buscado. 
# También poner el número de intentos requeridos.
numero_a_adivinar = 67
intentos = 1

numero_usuario = input("Introduce el numero ")

while not numero_usuario.isnumeric():
    numero_usuario = input("Error vuelve a introducir el numero ")
else:
    numero_usuario = int(numero_usuario)

while numero_a_adivinar != numero_usuario:
    if numero_usuario > numero_a_adivinar:
        print("El numero es menor al que has introducido")     
    else:
        print("El numero es mayor al introducido")

    intentos = intentos + 1
    numero_usuario = int(input("Introduce el numero "))
else:
    print("has ganado")

print("Has necesitado " + str(intentos) + " intentos")
print("Has necesitado {} intentos".format(intentos))

#Cristian
import random
num_intentos = 0
num_secreto = random.randint(1,100)
salida = False
while not salida:
    num_elegido = int(input("Intenta adivinar el numero secreto (1-100):"))
    num_intentos += 1
    if num_elegido > num_secreto:
        print("Te has pasadoo, prueba con uno mas pequeño.")
    elif num_elegido < num_secreto:
        print("Te has quedado corto, prueba con uno mas grande.")
    elif num_elegido == num_secreto:
        print("Eres todo un adivino!")
        salida = True
    else:
        print("Ha habido un error. Prueba de nuevo")
        num_intentos -= 1
else:
    print("Acertaste con ", num_intentos, " intentos.")

#14. Escribir un programa que guarde en una variable 
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo 
# o un mensaje de aviso si la divisa no está en el diccionario.
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce la divisa ")

if divisa in diccionario:
    print(diccionario[divisa])
else:
    print("La divisa no esta en el diccionario")

#Opcion B
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce la divisa ")

salida = diccionario.get(divisa, "La divisa no esta en el diccionario")

print(salida)

#Opcion C
# Euro euro EURO ...
#para solucionar esto usaremos el capitalize() pone la primera letra en mayusuclas
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce la divisa ")
divisa = divisa.capitalize()

salida = diccionario.get(divisa, "La divisa no esta en el diccionario")

print(salida)

#Opcion E
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce la divisa ")
divisa = divisa.capitalize()

salida = divisa if divisa in diccionario else "La divisa no esta en el diccionario"

print(salida)

#15. Escribir un programa que pregunte al usuario su 
# nombre, edad, dirección y teléfono y 
# lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <dirección> 
# y su número de teléfono es <teléfono>.

diccionario = {}

nombre = input("Introduce el nombre ")
edad = input("Introduce la edad ")
telefono = input("Introduce el telefono ")
direccion = input("Introduce la direccion ")

diccionario = {
    "nombre":nombre,
    "edad": edad,
    "telefono": telefono,
    "direccion": direccion
}

salida = diccionario["nombre"] + " tiene " + diccionario["edad"] + " años, vive en " + diccionario["direccion"]

print(salida)

#Opcion B

persona = {
    "nombre":input("Introduce el nombre "),
    "edad": input("Introduce la edad "),
    "telefono": input("Introduce el telefono "),
    "direccion": input("Introduce la direccion ")
}

salida = persona["nombre"] + " tiene " + persona["edad"] + " años, vive en " + persona["direccion"]

print(salida)

#Opcion C
persona = {
    "nombre":input("Introduce el nombre "),
    "edad": int(input("Introduce la edad ")),
    "telefono": input("Introduce el telefono "),
    "direccion": input("Introduce la direccion ")
}

salida = persona["nombre"] + " tiene " + str(persona["edad"]) + " años, vive en " + persona["direccion"]

print(salida)


#Opcion D
persona = {
    "nombre":input("Introduce el nombre "),
    "edad": int(input("Introduce la edad ")),
    "telefono": input("Introduce el telefono "),
    "direccion": input("Introduce la direccion ")
}

print(persona["nombre"], " tiene ", str(persona["edad"]), " años, vive en ", persona["direccion"])

#Opcion E
persona = {
    "nombre":input("Introduce el nombre "),
    "edad": int(input("Introduce la edad ")),
    "telefono": input("Introduce el telefono "),
    "direccion": input("Introduce la direccion ")
}

salida =  "{} tiene {} años, vive en {}".format(persona["nombre"],persona["edad"], persona["direccion"])

print(salida)

#16. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
# muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
fecha = input("Introduce una fecha (dd/mm/aaaa)")

fecha_partida = fecha.split("/")
dia = fecha_partida[0]
mes = fecha_partida[1]
ano = fecha_partida[2]

diccionario_meses = {"01":"Enero","02":"Febrero","03":"Marzo"}

salida = dia + " de " + diccionario_meses[mes] + " de " + ano
print(salida)

#Opcion B
fecha = input("Introduce una fecha (dd/mm/aaaa)")

fecha_partida = fecha.split("/")
dia = fecha_partida[0]
mes = fecha_partida[1]
ano = fecha_partida[2]

lista_meses = ["Enero","Febrero","Marzo", "Abril"]

salida = dia + " de " + lista_meses[int(mes)-1] + " de " + ano
print(salida)

#Opcion C
fecha = input("Introduce una fecha (dd/mm/aaaa)")

dia = fecha[0:2:1]
mes = fecha[3:5:1]
ano = fecha[7::1]


lista_meses = ["Enero","Febrero","Marzo", "Abril"]

salida = dia + " de " + lista_meses[int(mes)-1] + " de " + ano
print(salida)

#17. Escribir un programa que cree un diccionario vacío y lo vaya 
# llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato 
# debe imprimirse el contenido del diccionario.
persona = {}

while True:
    clave = input("Introduce que dato quieres guardar (telefono, edad..")
    valor = input("Introduce el valor del campo ")
    persona[clave] = valor
    print(persona)

#Opcion B hacer que pare
persona = {}
seguir = True

while seguir:
    clave = input("Introduce que dato quieres guardar (telefono, edad..) o introduce S para salir")
    if clave=="S":
        seguir = False
    else:
        valor = input("Introduce el valor del campo ")
        persona[clave] = valor
        print(persona)

#18. Escribir un programa que almacene las asignaturas de un
#  curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.
lista_asignaturas = ["Matemáticas", "Física", "Química","Historia","Lengua"]

for asignatura in lista_asignaturas:
    print(asignatura)

#Opcoin B
lista_asignaturas = ["Matemáticas", "Física", "Química","Historia","Lengua"]

print(lista_asignaturas)

#19. Escribir un programa que pregunte al usuario los números 
# ganadores de la lotería primitiva, 
# los almacene en una lista y 
# los muestre por pantalla ordenados de menor a mayor.

numeros = []
#para indicar que no usamos la variable poner un "_"
for _ in range(6):
    numero = input("Introduce el numero ")
    numeros.append(int(numero))

numeros.sort()
print(numeros)

#Opcion B
numeros = []
contador = 0

while contador <= 5:
    numero = input("Introduce el numero ")
    numeros.append(int(numero))
    contador = contador + 1

numeros.sort()
print(numeros)

#20. Escribir un programa que almacene en una lista los números del 
# 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numeros = []

for numero in range(1,11):
    numeros.append(str(numero))

numeros = numeros[::-1]

salida = ",".join(numeros)

print(salida)

#Opcion B
numeros = range(1,11)
numeros = list(numeros)

salida = ""
for numero in numeros[::-1]:
    salida = salida + str(numero) + ","

salida = salida[0:len(salida)-1]
print(salida)

#Opcion C
salida = str(list(range(1,11)))
salida = salida[1:len(salida)-1]
print(salida)

#Opcion E
print(str(list(range(1,11)))[1:len(str(list(range(1,11))-1)])

#21. Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.
abecedario = ["a","b","c","d","e"]
#Mejor opcion si nos usamos las funciones chr() y ord()
#asi con un bucle podemos crearlo sin meter todo a mano
abecedario = []
for codigo in range(ord("a"),ord("z")+1):
  abecedario.append(chr(codigo))

print(abecedario)

for posicion in range(-len(abecedario),-1,-1):
    if posicion % 3 == 0:
        del abecedario[posicion]

print(abecedario)

#Marcos
ls_abecedario = []

for numero in range(ord('a'),ord('z')):
    ls_abecedario.append(chr(numero))
for posicion in range(len(ls_abecedario), 1, -1):
    if posicion % 3 == 0:
        ls_abecedario.pop(posicion - 1)
print(ls_abecedario)

#Gonzalo
abc = []
i = 65 

while i <= 90:
    abc.append(chr(i))
    i += 1
print(abc)

abc_sinmulti_3 = []
contador = 0
while contador < len(abc):
    if contador % 3 != 0:
        abc_sinmulti_3.append(abc[contador])
    contador += 1
print("Abc sin posiciones multiplos de 3 " +  str(abc_sinmulti_3))

#Hector
for pos in abecedario[2::3]:
    eliminables.append(pos)
for letra in eliminables:
    abecedario.remove(letra)

#22. Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla si es un palíndromo.
palabra = input("Introduce una palabra ")
palabra = palabra.upper()
if(palabra == palabra[::-1]):
    print("Es palindromo")
else:
    print("no es palindromo")

#Opcion B
palabra = input("Introduce una palabra ")
salida = "Es palindromo" if palabra == palabra[::-1] else "No es paindromo"
print(salida)

#Opcion C
palabra = input("Introduce una palabra ")
invertida = palabra[::-1]
if(palabra == invertida):
    print("Es palindromo")
else:
    print("no es palindromo")
#23. Escribir un programa que almacene en una lista los 
# siguientes precios, 50, 75, 46, 22, 80, 65, 8, y 
# muestre por pantalla el menor y el mayor de los precios.
lista_precios = [50, 75, 46, 22, 80, 65, 8]
print(min(lista_precios))
print(max(lista_precios))

#24. Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).
edad = int(input("Introduce tu edad "))
for numero in range(1,edad+1):
    print(numero)

#While
edad = int(input("Introduce tu edad "))
contador = 1

while contador <= edad:
    print(contador)
    contador = contador + 1

#25. Escribir un programa que pida al usuario un número 
# entero positivo y muestre por pantalla todos los números 
# impares desde 1 hasta ese número separados por comas.
numero = int(input("Introduce un numero"))

for valor in range(numero):
    if valor % 2 == 1:
        print(valor,end=",")

#Opcion B
numero = int(input("Introduce un numero"))
lista = []
for valor in range(numero):
    if valor % 2 == 1:
        lista.append(str(valor))

print(",".join(lista))

#Opcion C
numero = int(input("Introduce un numero"))
salida = ""
for valor in range(numero):
    if valor % 2 == 1:
        salida = salida + str(valor) + ","

salida = salida[0,len(salida)-1]
print(salida)

#Opcion D
numero = int(input("Introduce un numero"))
lista = []
for valor in range(numero):
    if valor % 2 == 1:
        lista.append(str(valor))

salida = str(lista)
salida = [1:len(len)-1]

print(salida)

#26. Escribir un programa que pida al usuario un número 
# entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

altura = int(input("Introduce altura "))

for linea in range(1,altura+1):
    print(linea * "*")

#Opcion B
altura = int(input("Introduce altura "))

for i in range(altura):
    salida = ""
    for c in range(i):
        salida = salida + "*"
    print(salida)

#27. Escribir un programa que pida al usuario un 
# número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo (con primos).
#1
#2 1
#3 2 1
#5 3 2 1
#7 5 3 2 1

#Primero mostrar triangulo (ejercicio anterior)
altura = int(input("Introduce altura "))

for i in range(altura):
    print(linea * "*")

#Segundo el conteunio no es con * sino con numero primros
#calcular numeros primos
# Un numero es primo si y solo si, es divisible por la unidad y por si mismo
esPrimo = True

numero = 14

for divisor in range(numero-1,1,-1):
    if numero % divisor == 0:
        esPrimo = False
        break
if esPrimo == False:
    print("No es primo")
else:
    print("El numero es primo")

#Cuantos numeros primos tenemos que generar? tantos primos como la altura
altura = int(input("Introduce altura "))
lista_primos = []
numero = 1

while len(lista_primos) < altura:
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if numero % divisor == 0:
            esPrimo = False
            break
    if esPrimo == True:
        lista_primos.append(numero)
    numero = numero + 1
print(lista_primos)

#Debo imprimir en la altura adecuada
altura = int(input("Introduce altura "))
lista_primos = []
numero = 1

while len(lista_primos) < altura:
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if numero % divisor == 0:
            esPrimo = False
            break
    if esPrimo == True:
        lista_primos.append(numero)
    numero = numero + 1
lista_primos = lista_primos[::-1]
for i in range(altura):
    print(lista_primos[0:i])

#Ahora debemso sacaar el slice por detras
altura = int(input("Introduce altura "))
lista_primos = []
numero = 1

while len(lista_primos) < altura:
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if numero % divisor == 0:
            esPrimo = False
            break
    if esPrimo == True:
        lista_primos.append(numero)
    numero = numero + 1
lista_primos = lista_primos[::-1]
for posicion in range(-1,-(altura+1),-1):
  print(lista_primos[-1:posicion:-1])

#Abdellah
varpositivo=int(input('Por fa entra un numero positivo :'))
listaPrimos=[]
for ia in range(1,varpositivo+1):
    #test si numero primo
    i=2
    etat=False
    while i<ia:
        if ia%i==0:
            etat=True
            break
        i=i+1
    if etat==False:
        listaPrimos.append(ia)
        listaPrimos.sort()
        listaPrimos.reverse()
        chrr=''
        for aa in listaPrimos:
            chrr = chrr +' ' + str(aa)

        print(chrr)

#Manuel
numero = int(input("Introduce un numero entero positivo:"))
resultado =[]
contador1=1
resultado = ""
fin = numero +1
for contador1 in range (1,fin):
    contador2 = 1
    primo = True
    while (contador2< contador1):
        resto = contador1 % contador2
        if (resto == 0) and (contador2 !=1):
            primo=False
        contador2+=1
    if primo == True:
        resultado =  str(contador1)+" "+resultado
        print(resultado)

#Angel

Numero = int(input('Ingresa un numero entero positivo'))
Numeros_primos = []
Primos = 1
while len(Numeros_primos) < Numero:
    Es_primo = True
    for divisor in range(2, int(Primos ** 0.5) + 1):
        if Primos % divisor == 0:
            Es_primo = False
            break
    if Es_primo:
        Numeros_primos.append(Primos)
    Primos += 1
for i in range(Numero+1):
    Fila = Numeros_primos[0:i:1]
    Fila.reverse()
    print(" ".join(map(str, Fila)))

#Gonzalo
numero = int(input("Introduce un número entero: "))
primos = []
for i in range(1, numero + 1):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        primos.append(i)
        primos.sort()
        primos.reverse()

for i in range(len(primos)):
    for j in range(i + 1):
        if i < len(primos):
            print(primos[j], end=" ")
    print()

#Hector
entrada = input('Introduzca un número entero positivo: --> ')
if entrada.isnumeric():
    altura = int(entrada)
    primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # Entiendo que el objetivo del programa no es la generación de el enésimo número primo
    if altura > 0 and altura < len(primos):
        for y in range(0, altura):
            cunyaos = [str(numx) for numx in primos ][:y+1]  # Para ahorrarme el for para generar la lista de strings
            print(' '.join(cunyaos[::-1]))
    else:
        print('El programa no puede procesar el valor introducido')
        
#28. Escribir un programa que almacene la cadena de
# caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que 
# introduzca la contraseña correcta.

variable = "contraseña"

pass_usuario = input("Introduce el password ")

while pass_usuario != variable:
    print("Error te has equivocado")
    pass_usuario = input("Introduce el password ")
else:
    print("Felicidades contraseña correcta")