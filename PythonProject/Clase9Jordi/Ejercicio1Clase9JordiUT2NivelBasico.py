"""Ejercicio 1¶
Escribe un programa que pida al usuario un número entero y determine si es par o impar.
El programa debe imprimir un mensaje indicando el resultado."""

numer_ej1 = int(input("Escribe tu número entero: "))

if numer_ej1%2 == 0:
    print("Tu número es par.")
else:
    print("El número es impar.")