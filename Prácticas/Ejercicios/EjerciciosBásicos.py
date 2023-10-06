#1. Imprimir “Hola mundo” por pantalla.
print("Hola mundo")

#2. Crear dos variables numéricas, sumarlas y mostrar el resultado
variable = 5
numero = 3
print(variable + numero)

#3. Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.
precio_sin_iva = 100
porcetaje_iva = 21

iva = precio_sin_iva *(porcetaje_iva/100)
precio_total = precio_sin_iva + iva

print(iva)
print(precio_total)

#4. De dos números, saber cual es el mayor.

num1 = 3
num2 = 9

if num1 > num2:
    print("numero 1 es mayhor")
elif num1

#5. Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.

variable = 5
if variable >= 0 or variable <=  10:
    
    print("Perfecto")

num = 7

if(0 <= num <= 10)
print("El numero está entre 0 y 10")


#6. Mostrar con un while los números del 1 al 100.
while  False:
    numero = 10
    print(numero)

------------------------------------------

num = 1
while num<= 100:
    print(num)
    num = num +1
else:
    print(num)


#7. Mostrar con un for los números del 1 al 100.
for num in range(101):
    print(num)



#8. Mostrar los números pares entre 1 al 100.

#op1
for par in range(2,101,2):
    print(par)

#op2
for par in range(1,101):
    if par % 2 == 0:
        print(par)

#op3
lista = [par for par in range(1,101) if numero % 2 ==0]
print(list(lista))

#op4
print(list(range(2,101,2)))

#9. Mostrar los caracteres de la cadena “Hola mundo”.

#op1
cadena = "Hola Mundo"

print(cadena[0:10:1])

#op2
for letra in "Hola mundo":
    print(letra)

#op3
print(list("Hola Mundo"))
print("\n".join(list("Hola mundo")))
#10. Mostrar los caracteres de la cadena “Hola mundo” al reves

cadena = "Hola Mundo"

print(cadena[10:0:-1])


#11. Generar un rango entre 0 y 10

range(11)
print(list(num))

#12. Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y
#con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula hondo

#op1
print("¿Me dices Hola?")
palabra1 = input()
print("Me dices mundo")
palabra2 = input()

print("Ahora voy a hacer magia con tus palabaras")

resultado = (palabra1[0:2:1]+ palabra2[2:4:1] + " " + palabra1[0:2:1]+ palabra2[2:5:1])
print(resultado)

#op2
cadena1 = 5

#13. Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado.
#También poner el número de intentos requeridos.

num = 67
intentos
prop = int(input("Dime un número"))

if num ==prop:
    print("Has acertado!")
elif prop > num:
    print("")


#14. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$','Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa = input("Ingresa una divisa: ")
if divisa in divisas:
    print(f"El símbolo de {divisa} es {divisas[divisa]}.")
else:
    print(f"Ingrese nuevamente, {divisa} no está en el diccionario.")

#15. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
#guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
#tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

#16. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
#pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

#17. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
#sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
#que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
#contenido del diccionario.

#18. Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

#19. Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor amayor.

#20. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre
#por pantalla en orden inverso separados por comas.

#21. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#22. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
#palíndromo.

#23. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80,
#65, 8, y muestre por pantalla el menor y el mayor de los precios.

#24. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
#años que ha cumplido (desde 1 hasta su edad).

#25. Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por comas.

#26. Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

#27. Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo (con primos).
#1
#2 1
#3 2 1
#5 3 2 1
#7 5 3 2 1

#28. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.