"""Ejercicio 5¶
Nunca me ha gustado que Python no disponga de una manera rápida de aumentar un contador.
Haz un programa que pida al usuario un número entero e imprima el siguiente número."""

numero_g = int(input("Escribe un número"))

print(f"El siguiente número entero a {numero_g} es el número {numero_g+1}")


#Con un operador de asignación
num = int(input("Introduce un número entero: "))
num += 1
print(f"El siguiente número es: {num}")