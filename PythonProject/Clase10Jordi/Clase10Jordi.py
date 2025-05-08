"""Ejercicio 1 - Contador¶
Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido).
El programa debe imprimir los números en cada iteración."""

numero = int(input("Introduce un número entero positivo: \n"))
for i in range(0,numero+1,1):
    print(i)

"""Ejercicio 2 - Contador de números pares¶
Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido). 
El programa debe imprimir el resultado."""

numero = int(input("Introduce un número entero positivo(dividiendo el iterador): \n"))
numero_pares = 0
for i in range(0,numero+1):
    if i%2 == 0:
        numero_pares = numero_pares +1
print(numero_pares)

numero = int(input("Introduce un numero entero positivo (saltando de dos en dos): \n"))
pares = 0
for i in range(0, numero+1,2):
    pares = pares +1
print(pares)

"""Ejercicio 3 - Cuenta atrás¶
Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0. El programa debe imprimir cada 
número en la cuenta atrás."""

numero = int(input("Introduce un número entero positivo (cuenta atrás): \n"))
for j in range (numero,-1,-1):
    print(j)

"""Ejercicio 4 - Factorial¶
Escribe un programa que pida al usuario un número entero positivo y calcule su factorial. El programa debe imprimir el resultado. El factorial de un 
número n se define como el producto de todos los números enteros desde 1 hasta n.

Por ejemplo, el factorial de 5 (5!) es: 5*4*3*2*1 = 120. """

numero = int(input("Introduce un número positivo (factorial): \n"))
factorial = 1
for k in range (1,numero+1,1):
    factorial = factorial*k

print(factorial)

"""Ejercicio 5 - Múltiple de 3 o 5¶
Escribe un programa que pida al usuario un número entero positivo e imprima solamente los números múltiplos de 3 o de 5 dentro de ese rango.

Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3". Si el número es múltiplo de 5, 
imprime el número seguido del mensaje "es múltiplo de 5". Si el número es múltiplo de ambos no debes imprimir nada."""

numero = int(input("Introduce un número positivo: \n"))

for m in range (0, numero+1,1):
    if m%3 == 00 and m%5 ==0:
        continue
    elif m%3 == 0:
        print(f"{m} es múltiplo de tres")
    elif m%5 == 0:
        print(f"{m} en múltiplo de cinco")


"""Ejercicio 6 - Triángulo de asteriscos¶
Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura 
especificada. Por ejemplo, si el 
usuario ingresa 5, el triángulo debe verse así:"""

altura = int(input("Introduce un número entero positivo que será la altura del usuario: \n"))

for l in range (0, altura+1,1):
    print("*"*l)

"""Ejercicio 9 - Suma acumulativa¶
Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números. 
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total."""

print("Introduce números para sumarlos y para acabar introduce 0:")
numero = int(input())
resultado = 0

while numero !=0:
    resultado += numero
    numero = int(input())

print(f"El resultado es {resultado}")

"""Ejercicio 10 - Akinator numérico¶
Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número. 
El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. 
El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto."""

import random

numero_aleatorio = random.randint(1,100)
numero_usuario = int(input("Intrododuce un número del uno al cien: "))

while numero_aleatorio != numero_usuario:
    if numero_usuario > numero_aleatorio:
        print("El número es demasiado alto prueba otra vez.")
    else:
        print("El número es demasiado bajo")

    numero_usuario = int(input("Introduce otra vez un número del uno al cien"))

print("Correcto has acertado")

"""Ejercicio 11 - Media de notas¶
Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. Seguidamente se recibirán ese número de 
series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. El programa debe seguir pidiendo 
notas hasta que el usuario ingrese un -1. Al final, imprime la media.


Introduce el número de evaluaciones: 3
Notas de la evaluación 1: 6 8 4 3.5 9 -1
Notas de la evaluación 2: 7 5 8.5 -1
Notas de la evaluación 3: 9 10 8.5 -1
La media de la evaluación 1 es: 6.5
La media de la evaluación 2 es: 7.5
La media de la evaluación 3 es: 9.0"""

evaluaciones = int(input("Introduce las evaluaciones (pon /-1/ para salir: "))

for i in range(evaluaciones):
    nota = float(input("Introduce la siguiente nota: "))
    num_notas = 0
    suma_notas = 0
    while nota != -1:
        num_notas += 1
        suma_notas += nota
        nota = float(input("Introduce la siguiente nota"))
    print(f"Nota media evaluacion{i+1}: {suma_notas/num_notas}")

    """Ejercicio 12 - Mayor y menor¶
Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor. 
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor."""
    from sys import hash_info

    mayor = hash_info.inf
    menor = hash_info.inf
    numero = int(input("Introduce el valor (0 para terminar): "))

    while numero != 0:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

        numero = int(input("Introduce un valor (pon 0 para terminar): "))

print(f"Mayor: {mayor} Menor: {menor}")

