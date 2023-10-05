#Para solicitar valores por teclado tenemos la funcion inut(PROMT)

entrada = input("Introduce el numero ")
print(entrada)
print(type(entrada))

#Siempre devuelve un string, para leer u entero debemos convertirlo
entrada = int(input("Introduce el numero "))
print(entrada)
print(type(entrada))

#para generar rangos de nuemro tenemos la funcion range()
#range(INI,FIN,STEP)

for numero in range(10): #dede 0 hasta 10
    print(numero)

for numero in range(2,10): #dede 2 hasta 10
    print(numero)

for numero in range(0,10,2): #dede 0 hasta 10 de 2 en dos
    print(numero)