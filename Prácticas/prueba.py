cadena = "Hola Mundo"
print(cadena[0:4:10000])#H la posicion del salto es más grande que la longitud sólo saca el primer caracter.
print(cadena[0:4000:1])#po_fin > len llega solo hasta el final no da error.
print(cadena[4000:10:1])