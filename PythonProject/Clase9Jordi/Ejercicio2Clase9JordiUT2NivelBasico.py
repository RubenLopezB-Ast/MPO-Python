"""Ejercicio 2¶
Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
El programa debe imprimir un mensaje indicando el resultado."""

numer_ej2 = int(input("Escribe un número entero: "))
if numer_ej2 == 0:
    print("El número introducido es 0 .")
elif numer_ej2 > 0:
    print("El número introducido es positivo.")
elif numer_ej2 < 0:
    print("El número introducido es negativo.")
