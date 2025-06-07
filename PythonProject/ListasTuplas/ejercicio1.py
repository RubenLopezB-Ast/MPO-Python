"""Ejercicio 1 - Capitales y países¶
Escribe un programa que almacene en un diccionario las capitales de varios países, se introducirán los datos con la
forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
El programa debe permitir al usuario consultar la capital de un país introduciendo su nombre. Si el país no está
en el diccionario, el programa debe informar al usuario.
1. variables
2. bucle que lee y registra las entradas de pais-capital
3.pedir un país y mirar si existe en el diccionario"""
from Clase11Jordi.ejerciciosClase11Jordi import opcion
from ListasTuplas.tuplas import inventario, nombre

# paises = {}
# entradaej1 = input("Indica un valor de la forma ´Pais:Capital´ o escribe FIN INSERCIONES para finalizar").lower()
#
# while entradaej1 != "FIN INSERCIONES".lower():
#     pais = entradaej1.split("-")[0]
#     capital = entradaej1.split("-")[1]
#     paises[pais]= capital
#     entradaej1 = input("Indica un valor de la forma ´Pais:Capital´ o escribe FIN INSERCIONES para finalizar").lower()
#
# print(paises)
#
# pais_usuario = input("Introduce el nombre del país que quieres consultar").lower()
# if pais_usuario in paises:
#     print(f"La capital de {pais_usuario} es {paises[pais_usuario]}")
# else:
#     print("No existe esa entrada en el diccionario o el formato no es el correcto.")


"""Ejercicio 2 - Contar palabras en un texto¶
Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto. El 
programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas 
frecuencias. Ignora la puntuación y considera las palabras en minúsculas.
´Hola que tal que te cuentas´
frecuencia = {
    ´hola´:1,
    ´que´:2,
    ´tal´:1,
    ´cuentas´:1
}

1. Definir las variables
2. Bucle que recorra las palabras y mire si:
    2.1 Si ya esistian: sumo 2 a la frecuencia anterior
    2.2 Creo un entrada en el diccionario con frecuenia 1
3.Imprimir diccionario
"""
# palabrasEj3 = {}
# textoEj3 = input("Introduce una frase\n ").lower().split()
#
# for palabraEj3 in textoEj3:
#     if palabraEj3 in palabrasEj3:
#         palabrasEj3[palabraEj3] += 1
#     else:
#         palabrasEj3[palabraEj3] = 1
#
# print(palabrasEj3)

"""Ejercicio 3 - Inventario de productos¶
Escribe un programa que gestione un inventario de productos utilizando un diccionario. El programa debe permitir al 
usuario añadir productos con su nombre y cantidad, eliminar productos, y consultar la cantidad de un producto 
específico. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

"""

# inventarioE3 = {}
# opcionjE3 = -1
#
# while opcionjE3 != 4:
#     print("Escoge una opción: ")
#     print("1. Añadir producto")
#     print("2. Eliminar producto")
#     print("3. Consultar producto")
#     print("4. Salir")
#     opcionjE3 = int(input("Introduce una opción: "))
#
#     if opcionjE3 == 1:
#         nombreE3 = input("Introduce un producto: ")
#         cantidadE3 = int(input("Introduce una cantidad: "))
#         inventarioE3[nombreE3] = cantidadE3
#     elif opcionjE3 == 2:
#         nombreE3 = input("Introduce el producto a eliminiar: ")
#         if nombreE3 in inventarioE3:
#             del inventarioE3[nombreE3]
#             print(f"Producto { nombreE3} eliminado del inventario")
#         else:
#             print(f"No existe el producto {nombreE3} en el inventario")
#     elif opcionjE3 == 3:
#         nombreE3 = input("Introduce el producto a consultar: ")
#         if nombreE3 in inventarioE3:
#             print(f"El producto {nombreE3} tiene una cantidad de {inventarioE3[nombreE3]} unidades")
#         else:
#             print(f"No existe el producto {nombreE3} en el inventario")
#     elif opcionjE3 >4 or opcionjE3 < 1:
#         print(f"La opción {opcionjE3} no existe en la lista de comandos")
#
# print("Saliendo . . . ")


"""Ejercicio 4 - Tupla de números¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en 
una tupla. Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número 
mínimo de la tupla."""

numerosE4 = input("Introduce una lisra de números separados por coma \n").split(",")
numerosE4 = [int(numE4) for numE4 in numerosE4]
tuplaE4 = tuple(numerosE4)

suma = 0
promedio = 0.0
maximoE4 = float("inf")
minimoE4 = float("inf")

for numeroE4 in tuplaE4:
    suma += numeroE4
    if numeroE4 > maximoE4:
        maximoE4 = numeroE4
    if numeroE4 < minimoE4:
        minimoE4 = numeroE4

promedio = sum / len(tuplaE4)

print(f"Suma: {suma}")
print((f"Promedio: {promedio}"))
print(f"Máximo: {maximoE4}")
print(f"Mínimo: {minimoE4}")