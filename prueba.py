#13. Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado.
#También poner el número de intentos requeridos.

print("Juguemos al juego de adivinar el numero. Yo he pensado en un número")

num = 26

print("Venga, dame un número")
prop = int(input())

while prop == num:
    print ("Perfecto! Has ganado!")

    if prop < num:
        print("Lo siento, prueba con un número más alto")
        prop = int(input())

    if prop > num:
        print("Lo siento, prueba con un número más bajo")
        prop = int(input())