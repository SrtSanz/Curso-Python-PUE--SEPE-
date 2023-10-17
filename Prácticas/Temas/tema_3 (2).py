#Funciones en python
# se crean con la palabra reservada def
# def IDENTIFICADOR (PARAM_1,PARAM_2, ..)
#   """""" cadena de documentacion
#   CUERPO
#   return que es opcional
#La funcion más sencilla pass no recibe argumentos y no hace nada 
def foo():
    pass

#Se le puede poner una cade de documentación, que en caso de existir
#iría a continuación de la definición de la firma de la función en formato string
def foo():
    """
        Ejemplo de cadena de documentacion, es la "ayuda" de la funcion
        habitualmente se pone para que sirve la funcion
        y los parametros de entrada y salida
    """
    pass

#No es un comentario, porque realmente NO lo ignora el intérprete
# lo asigna automaticamente a un método mágico, llamado __doc__
print(foo.__doc__)

# Las fucniones en python SIEMPRE devuelven algo, por defecto None
def foo():
    pass
#una vez declarada la podemos invocar -> nombre(args..)
retorno = foo()
print(retorno)

#Podemos usar la palabra return para indicar que queremos que devuelva
#en lugar del none
def foo():
    return "Hola Mundo"
retorno = foo()
print(retorno)

#La primera es que pueden devolver CUALQUIER tipo de dato
#podemos devolver más de un valor
def foo():
    variable_1 = "Hola"
    variable_2 = "Adios"
    #los pondremos a continuación del return separados por comas
    return variable_1,variable_2

#Devuelve dos variables, lo que hace es meterlas dentro de una tupla
retorno = foo()
print(type(retorno))
print(retorno)

#Con un retorno múltiple podemos usar la asignación multiple de python
def foo():
    variable_1 = "Hola"
    variable_2 = "Adios"
    return variable_1,variable_2

retorno_1, retorno_2 = foo()
print(retorno_1)
print(retorno_2)

#las funciones pueden tener un cuerpo, que es como los if, las acciones que va a realizar
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
#por defecto si en una función definimos que recibe un parametro
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
#de la función debemos indicarlo poniendo el valor por defecto
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
#Si no llega el argumento b le asignará automaticamente el valor por defecto que es 0
print(sumar(4))
print(sumar(40))
print(sumar(4342,2323))

#Tipado de datos en las funciones
#python soporta que en la firma de la función le indiquemos el tipo de dato
#que va a ser cada parámetro
#Pero ojo solo sirve para ponerlo en el código a modo de documentación
#No tiene efectos ningunos reales en el código
def foo(x:int,y:str,z:bool):
    print("x:",x,"y:",y,"z:",z)

foo(1,2,3)
foo("a","b","c")

#Argumentos
#Por defecto obligatorios y posicionales
#para que no sean obligatorios en la firma ponemos los valores por defecto
#deben ir por orden los opcionales SIEMPRE al final.
def foo(x,y=10,z=20):
    print("x:",x,"y:",y,"z:",z)

#Esto no es válido
def foo(x=10,y,z=20):
    print("x:",x,"y:",y,"z:",z)

#Posicionales
#que los argumentos se asignan siguiendo el orden de la declaración
#pero se puede cambiar, y para ello en el momento de la invocación
#ponemos el nombre de los argumentos.
def foo(x,y,z):
    print("x:",x,"y:",y,"z:",z)
#para que sean nominales es en la invocación, deben coincidir con el nombre
#que tienen en la firma de la función.
foo(y=1,z=2,x=3)

#Se pueden combinar ambas ideas
def foo(x,y=10,z=20):
    print("x:",x,"y:",y,"z:",z)

#Si combinamos ambos, debemos respetar los obligatorios y el orden
#de los optativos siempre al final y cuando tengamos nominales y posicionales
#los posicionales siempre al principio.
foo(y=1,z=2,x=3)
foo(3)
foo(z=2,x=3)
#No son válida
foo(y=1,3)
foo(z=2,y=3)

#Podemos tener un número arbitrario de argumentos, esto se hace incluyendo un * en la firma de la función
def foo(*argumentos):
    print(type(argumentos))
    print(argumentos)

#podemos invocar esta función con todos los parámetros que queramos
foo()
foo(1)
foo(1,2)
foo(1,2,"c")
foo(1,2,"c","a")

#Esto nos pemrite hacer funciones como sumar un número arbitrario de numeros
# sum()
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    return resultado

print(suma(1))
print(suma(1,2))
print(suma(1,6,3,6,9,6,234,6))

#también la función print
#si combinamos un número arbitrario de argmentos y argumentos optativos
#siempre primero el número variable y al final los optativos
def imprimir(*argumentos, sep = " "):
    salida = ""
    for item in argumentos:
        salida = salida + str(item) + sep
    print(salida)
#esto implica que los optativos haay que invocarlos nominalmente
imprimir("hola","que",sep="SEPARAR")

#también podemos poner argumentos obligatorios, arbirrarrios y finalente optativos
def foo(x,y,*variable, otro = ""):
    print(x)
    print(y)
    print(variable)
    print(otro)

#Debemos poner primero los obligatorios
foo(23,45,"s","a", otro = "OTRO")

#Podemos tener un número arbitrario de argumentos nominales
#para esto debemos poner un ** en la firma
def foo(**parametros):
    print(type(parametros))
    print(parametros)

foo(a=12,b=44,f=44)

#Esto combinaar con todolo anterior
def foo(x,y,*variable, otro = "",**parametros):
    print(x)
    print(y)
    print(variable)
    print(otro)
    print(parametros)

foo(23,45,"s","a", otro = "OTRO",a=2,b=10)

#Recursivad
#es cuando tenemos funciones que se invocan a si mismas
#las funciones recursivas tiene cierto parecido con los bucles while
# en las funciones recursivas al igual que en los bucles while
#debemos tener una condicion de parada que debe ser alcanzable
#en la recursividad esa condicion de parada se llama "caso base"
def recursiva(numero):
    print(numero)
    recursiva(numero - 1)

recursiva(5)

#Ponemos un caso base

def recursiva(numero):
    print(numero)
    if numero == 1:#en el 1 no se vuelve a invocar sino que devuelve 1
        return 1
    else:
        recursiva(numero - 1)

recursiva(5)

#Factorial en recursivo
def factorial(numero):
    #caso base 1
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero -1)

factorial(5)

#factorial(5) = 5 * factorial(4)
#factorial(4) = 4 * factorial(3)
#factorial(3) = 3 * factorial(2)
#factorial(2) = 2 * factorial(1)
#factorial(1) = 1
#factorial(2) = 2 * 1 = 2
#factorial(3) = 3 * 2 = 6
#factorial(4) = 4 * 6 = 24
#factorial(5) = 5 * 24 = 120


#Fibonacci
# 1 1 2 3 5 8 13 ..
#Algoritmo recursivo mas facil que en iterativo
# 1 => 0
# 1 => 1
# 2 => 2 
# 3 => 3
# 5 => 4
# 8 => 5
# 13 => 6
def fibonacci(posicion):
    if ((posicion == 1) or (posicion==0)):
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(fibonacci(5))

#Como funciona:
#fibonacci(4) = fibonacci(3) + fibonacci(2)
#fibonacci(3) = fibonacci(2) + fibonacci(1)
#fibonacci(2) = fibonacci(1) + fibonacci(0)
#fibonacci(0) = 1
#fibonacci(1) = 1
#fibonacci(2) = 1 + 1 = 2
#fibonacci(3) = 2 + 1 = 3
#fibonacci(4) = 3 + 2 = 5

#Alcance de variables
#las variables que se declaran dentro de las funciones por defecto son
#locales a esa funcion, que solo se pueden dentro de la funcion

def foo():
    x = 0
    print(x)

foo()
print(x)

#Y las variables que se declaran dentro de las funciones son locales
# y si las tenemos fuera para usarlas dentro
#tenemos 2 opciones
# la primera pasarlas como parametros
# la segunda variables globales
#Paso por parametros

def foo(variable):
    #al hacer la asignacion crea una nueva variable local a la funcion
    variable = 100
    print(variable)

otra = 5
foo(otra)
print(otra)

#Otro ejemplo
def foo(lista):
    lista = ["a","b","c"]
    print(lista)

lista = [1,2,3,4,5]
foo(lista)
print(lista)

#Por ultimo, las variables MUTABLES (listas, conjuntos, diccionarios, objetos propios..)
#se pasan automaticamente por referencia y si se modifican dentro de la funcion
#quedan modificados fuera
def foo(lista):
    lista.append("a")
    lista.append("b")
    lista.append("c")
    print(lista)

lista = [1,2,3,4,5]
foo(lista)
print(lista)

#Si no quereis que suceda esto debeis pasar como copia las variables mutables
#a las funciones, haciendo por ejemplo slicing
def foo(lista):
    lista[0]="Hola"
    
    print(lista)

lista = [1,2,3,4,5]
foo(lista[:])
print(lista)


# la segunda variables globales
#es una variable que tiene un ambito superior y tiene visibilidad dentto de las funciones
#que se consideran subordinadas
#Por defecto todas las variables son globales de lectura si estan
#declaradas fuera de las funciones
variable = 10

def foo():
    print(variable)

foo()

#local

variable = 10

def foo():
    #si aqui ponemos una igualdad independientemente de si la variable es mutable
    # o no lo que hace es generar una nueva variable
    variable = 100
    print(variable)

foo()
print(variable)

#Si la variable es mutable
#se modifica dentro se ve modificada fuera
variable = [1,2,3]

def foo():
    variable[0]="Hola"
    print(variable)

foo()
print(variable)

#Y si queremos modificar la vairable dentro de la funcion y ver los cambios fuera?
#pues python nos da la palabra reservada global que se debe usar dentro de la funcion
#antes de usar la variable

variable = 100

def foo():
    #aqui le indicamos que vamos a modificar la variable global
    global variable
    variable = 1000
    print(variable)

foo()
print(variable)

#Ojo es peligroso su uso indiscriminado

suma = 0

def foo():
    global x
    x = 100
    print(x)

foo()
#Si la variable global no existe, lo que hace python es crearla
print(x)

#Las funciones pueden tener funciones dentro
#No hay limite en el anidamiento
def foo():
    #se comportan como variables locales
    def foo_2():
        print("hola")
    foo_2()


foo()
#erro no definida porque es local a foo()
foo_2()

#las funciones que estan anidadas podemos devolverlas
def foo():
    def foo_2():
        print("Hola")
    #al hacer esto devolvemos la funcion
    return foo_2

vuelta = foo()
vuelta()

#Esto se puede complicar,
#el objeticvo de esto era dar una alterntiva al uso de objetos
# para encapsular (es decir agrupar) funciones dentro de otra fucino
def calculadora(operacion):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    if(operacion == "+"):
        return suma
    else:
        return resta

cuenta = calculadora("+")
print(cuenta(8,9))
cuenta = calculadora("-")
print(cuenta(8,9))

#En la certificacin

def foo(a,b):
#a = 5
#b = 6
    def foo_2(a):
        #a = 4
        #b es la de foo asi que b = 6
        print(a + b)

    return foo_2

g = foo(5,6)
g(4)

#Funciones lambda
#es una forma de escribir nuestras funciones mas breves
#es parecido al concepto de lista de comprension pero version funciones
#las funciones lambda estan soportadas por la mayoria de los lenguajes e programacion
#sintaxis
# lambda PARAMS: OPERACION
# se pueden asignar a variables para poder reutilizarlas
# las funciones lambda son funciones a todos los efectos aunque tienen algunhas limitaciones
#otro nombre que tienen es funciones anonimas
suma = lambda a,b: a + b

#esto es equivalente
def suma(a,b):
    return a + b

#Principales diferencias y limitaciones
# las funciones tienen autoretorno, no llevan la palabra return, es mas no la puden
suma = lambda a,b: return a + b #error no funciona no puede llevar return
#esto tambien implica que las lambda solo pueden tener una unica instruccion en su cuerpo
suma = lambda a,b: c =a + b c= c +9 #mas de una instruccion error
#puede poner csas que solo devuelven una linea
suma = lambda a,b: a + b if a > b else b
suma = lambda a,b: [numero for numero in range(11)]

#Si precisais mas complejas, una funcion aparte e invocarla desde la lambda, pero esto no aporta nada
#como cualquier otra funcion pueden recibir ualquier tipo de argumento y devolver cualquier tipo

#El uso mas habitual es juntar las lambda con otras funciones de python
#que reciben funciones como argumento
# filter()
#la funcion filter nos permite aplciar un filtro a un elemeno iterable
#el filtro sera definido por una funcion que debe devolver true si pasa el filtro
#y false en caso de que el elemento sea excluido
lista = [1,2,3,4,5,6,7,8,9,10]
#queremos solo los pares
pares = filter(lambda numero: numero % 2 == 0, lista)
print(list(pares))

#equivalente en iterativo
lista = [1,2,3,4,5,6,7,8,9,10]

for numero in lista:
    if numero % 2 == 0:
        print(numero)

#asignarla a variable
lista = [1,2,3,4,5,6,7,8,9,10]
#queremos solo los pares
funcion_pares = lambda numero: numero % 2 == 0
pares = filter(funcion_pares, lista)
print(list(pares))

# map()
#aplicar una funcion a todos los elementos de un iterable y nos devuelve el flujo modificado
lista = [1,2,3,4,5,6,7,8,9,10]

cuadrados = map(lambda numero: numero * numero, lista)

print(list(cuadrados))

#seria equivalente a:
lista = [1,2,3,4,5,6,7,8,9,10]
cuadrados = []

for numero in lista:
    cuadrados.append(numero * numero)

print(cuadrado)

