"""Ejercicio 3¶
Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5.
El programa debe imprimir un mensaje indicando el resultado."""

number_ej3 = int(input("Escribe un número entero:  "))

if number_ej3%3 == 0 and number_ej3%5 == 0:
    print(f"El número {number_ej3} es divisible por tres y cinco.")
else:
    print(f"El número {number_ej3} no es divisible ni por tres y por cinco a la vez.")

