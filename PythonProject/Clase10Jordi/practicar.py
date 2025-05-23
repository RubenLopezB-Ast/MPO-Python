"""
Escribe un programa que pide al usuario una serie de números enteros y determine cuál es el mayor y cuál es
el menor.
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0.
Al final, imprime el mayor y el menor.
"""
from sys import hash_info

mayor = -hash_info.inf
menor = hash_info.inf
numero = int(input("Introduce un valor (0 para terminar):"))

while numero !=0:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

    numero = int(input("Introduce un valor (0 para finalizar): "))

if mayor == 0 and menor == 0:
    print("No se han introducido números")
print(f"Mayor: {mayor} Menor: {menor}")