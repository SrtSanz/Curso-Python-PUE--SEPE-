#Fncines en python
# se crean con la palabra reservada def
# def IDENTIFICADOR (PARAM_1,PARAM_2, ..)
#   """""" cadena de documentacion
#   CUERPO
#   return que es opcional
#la funcion mas sencilla
#No recibe argumentos y no hace nada 
def foo():
    pass

#Se le pude poner una cade de documentacion, que es caso de existir
#iria a continuacion de la definicion de la firma de la funcion en formato string
def foo():
    """
        Ejemplo de cadena de documentacion, es la "ayuda" de la funcion
        habitualmente se pone para que sirve la funcion
        y los parametros de entrada y salida
    """
    pass

#No es un comentario, porque realmente NO lo ignora el interprete
# lo adigna automaticamente a un metodo magico, llamado __doc__
print(foo.__doc__)

# Las fucniones en python SIEMPRE devuelven algo, por defecto None
def foo():
    pass
#una vez declarada la podemos invocar nombre(args..)
retorno = foo()
print(retorno)

#Podemos usar la palabra return para indicar que queresmo que devuelva
#en lugar del none
def foo():
    return "Hola Mundo"
retorno = foo()
print(retorno)

#La primera es que pueden devolver CUALQUIER tipo de dato
#podemos devolver mas de un valor
def foo():
    variable_1 = "Hola"
    variable_2 = "Adios"
    #los pondremos a continuacion del return separados por comas
    return variable_1,variable_2

#Devuelve dos variables, lo que hace es meterlas dentro de una tupla
retorno = foo()
print(type(retorno))
print(retorno)

#Con unretorno multiple podemos usar la asignacion multiple de python
def foo():
    variable_1 = "Hola"
    variable_2 = "Adios"
    return variable_1,variable_2

retorno_1, retorno_2 = foo()
print(retorno_1)
print(retorno_2)

#las funciones pueden tener un cuerpo, que es como los if, las acciones que a a realizar
def foo():
    a = 10
    b = 30
    suma = a + b
    return suma

retorno = foo()
print(retorno)

#Las funciones pueden recibir argumentos
def foo(numero):
    print(numero)

#Los argumentos pueden ser posicionales y nominales
#por defecto si en una funcion definimos que recibe un parametro
# son OBLIGATORIOS y POSICIONALES
foo() #error porque el argumento es obligatorio
foo(5)
#Las funciones pueden recibir CUALQUIER tipo de objeto como argumento

def sumar(a, b):
    """
        Funcion para sumar dos numeros
        Entrada: 
            a, primer numero
            b, segundo numero
        Retorno:
            la suma de los dos numeros
    """
    return a + b

print(sumar(4,6))
print(sumar(40,78))
print(sumar(4342,2323))

#Podemos convertir los argumentos en optativos, para ello en la firma 
#de la funcion debemos indicarlo poniendo el valor por defecto
def sumar(a, b = 0):
    """
        Funcion para sumar dos numeros
        Entrada: 
            a, primer numero
            b, segundo numero
        Retorno:
            la suma de los dos numeros
    """
    print(a)
    print(b)
    return a + b
#Si no llega el argumento b le asignara automaticamente el valor por defecto que es 0
print(sumar(4))
print(sumar(40))
print(sumar(4342,2323))