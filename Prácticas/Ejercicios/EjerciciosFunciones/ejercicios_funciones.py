#Ejercicio 1
#Escribir una función que muestre por pantalla el saludo 
# ¡Hola Mundo! cada vez que se la invoque.
def saludar():
    print("Hola Mundo")

saludar()

#Ejercicio 2
#Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!.
def saludaA(quien):
    print("hola", quien)

saludo = "Jane"
saludaA(saludo)


#Ejercicio 3
#Escribir una función que reciba un número entero positivo y 
# devuelva su factorial (recordad el factorial se calcula de 
# la siguiente manera, se debe multiplicar por todos los valores 
# inferiores hasta el uno), por ejemplo 5 factorial seria:
#5! = 5 * 4 * 3 * 2 * 1.
def factorial(numero):
    resultado = 1
    for multiplicar in range(numero,1,-1):
        resultado = resultado * multiplicar
    return resultado


print(factorial(5))

#Alberto
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1) 

num = int(input("Introduce un numero positivo: "))

print(factorial(num))
print("El numero elegido es el " + str(num) + " y su factorial es: " + str(factorial(num)) + "." )

#Ejercicio 4
#Escribir una función que calcule el total de una factura 
# tras aplicarle el IVA. La función debe recibir la cantidad 
# sin IVA y el porcentaje de IVA a aplicar, y 
# devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

def total_factura(cantidad_sin_iva, iva = 21):
    importe_iva = cantidad_sin_iva * iva/100
    total = cantidad_sin_iva + importe_iva
    #total = cantidad_sin_iva * (1 + (iva/100))
    return total

print(total_factura(100))
print(total_factura(100,10))
