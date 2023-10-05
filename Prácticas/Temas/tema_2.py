#Estructrs de control
#La mas basica es el if - elif - else

variable = 10
#los bloqeuse definen por la identacion
if variable ==0:
    print("La variable es cero")

#Podemos tener varios elif, que son condiciones complementarias
variable = 10
#los bloqeuse definen por la identacion
if variable ==0:
    print("La variable es cero")
elif variable == 9:
    print("la variable es nueve")
elif variable == 10:
    print("La variable es diez")

#Else
variable = 10
#los bloqeuse definen por la identacion
if variable ==0:
    print("La variable es cero")
else:
    print("La variable no es cero")

#Se puede combinar todo junto
variable = 10
#los bloqeuse definen por la identacion
if variable ==0:
    print("La variable es cero")
elif variable == 9:
    print("la variable es nueve")
elif variable == 10:
    print("La variable es diez")
else:
    print("No se ha cumplido ninguna de las anteriores")

#Pyhon admite notacion matematica para los rangos
#queremos crear un if que imprima el numero que está en el rango de 0 a 10 si está la variable en ese rango

numero = 6

if (numero >= 0 and numero <= 10):
    print("La variable esta dentro del rango 0 - 10")

#Notacion matemica
numero = 6
if(0 <= numero <= 10):
    print("La variable esta dentro del rango 0 - 10")

#Ojo cortocircuitadas
print(1/0 and True)
print(False and 1/0)
print(True or 1/0)

#while

#Se ejcuta mientras se cumple una condicion
numero = 10
#Ojo bucle infito la condicion debe ser alcanzable
while numero > 0:
    print(numero)

#ejemplo bien echo
numero = 10

while numero > 0:
    print(numero)
    numero = numero -1

#ejemplo con booleana

sigue = True

while sigue:
    print("Hola")
    sigue = False

#For es para recorrer iterables
lista = [1,2,3,4]

for numero in lista:
    print(numero)

#strings
for letra in "Hola Mundo":
    print(letra)

#tuplas
tupla = (1,2,3,4)

for numero in tupla:
    print(numero)

#diccionarios, por defecto las claves
diccionario = {"nombre":"Jane", "apellido":"Doe"}

for item in diccionario:
    print(item)

#para los valores
diccionario = {"nombre":"Jane", "apellido":"Doe"}

for item in diccionario.values():
    print(item)

#mostrar la clave y el valor
diccionario = {"nombre":"Jane", "apellido":"Doe"}

for key,value in diccionario.items():
    print(key)
    print(value)

#Palabras reservadas pass, break y continue
# el pass es la instrucccion vacia, no hacemos nada
if(True):
    pass
print("Otra")

#break, salida incondicional
lista = [1,2,3,4]

for numero in lista:
    print(numero)
    break

#Aqui se ve la diferencia on el else
lista = [1,2,3,4]

for numero in lista:
    print(numero)
else:
    print("He acabado")

    lista = ["hola","adios"]

for numero in lista:
    print(numero)
    break
else:
    #No ejecuta el else porque no ha terminado de iterar
    print("He acabado")

#continue, que devuelve el control a la evaluacion del bucle
numero = 10

while numero > 0:
    numero = numero -1
    print("dentro")
    #salto incondicional a la estructura de control
    continue
    print(numero)