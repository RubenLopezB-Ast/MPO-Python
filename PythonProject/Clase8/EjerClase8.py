#Crea una lista con los números del uno al cinco.
ejer_lista = [1,2,3,4,5]
print(ejer_lista)

#Modifica el tercer elemento a diez.
ejer_lista[2]=10
print(ejer_lista[2])

#Agrega el número siete al final.
ejer_lista.append(7)
print(ejer_lista)

#Crear una tupla con los número 1, 2, y 3.
mi_tupla = (1,2,3)
print(mi_tupla)

#Intentar modificar el segundo elemento.
#mi_tupla[3] = 23
print(mi_tupla)

#Explicar el error obtenido.
#Las tuplas no se pueden modificar son inmutables (pregunta examen).

#Crea una matriz 3x3 de números consecutivos.
mi_matriz = [[1,2,3],[4,5,6],[7,8,9]]
#realmente una matriz se ve así:
#mi_matriz = [[1,2,3],
#            [4,5,6],
#             [7,8,9]]
#Como imprimir una matriz (primero meter fila y después meter columna).

print(mi_matriz[1][2])

#Modifica el elemento de la segunda fila, tercera
mi_matriz[1][2] = 10

#Imprime la matriz.
print(mi_matriz)

#
#
#