#Listas
mi_lista = [10,25,30,40,50]

#Posición
print(mi_lista[0])

#Modificar valor de la lista
mi_lista[1]=999
print(mi_lista[1])

#Len cuenta el largo de la mi_lista
print(len(mi_lista))

#Iterar es pasar cada posición de una lista por línea

#Append agrega datos al final de la lista.
mi_lista.append(60)
print(mi_lista)

#Insert cambia el elemento que se elija de la lista aumentando la lista una posición.
mi_lista.insert(2,20202)
print(mi_lista)

#Remove elimina el primer dato  que contenga el valor que le demos de mi lista de izquierda a derecha.
mi_lista.remove(30)
print(mi_lista)

#Pop elimina el elemento de la posición que le digamos (i) y lo devuelve si no se expecifica el i elimnina el último
#elemento.
mi_lista.pop(2)
print(mi_lista)
mi_lista.pop()
print(mi_lista)

#Sort organiza la lista de menor a mayor
mi_lista.sort()
print(mi_lista)

#Reverse invierte el orden de la lista
mi_lista.reverse()
print(mi_lista)


