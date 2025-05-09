"""Ejercicio 11¶
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente.
El primer número siempre será menor que el segundo.

Ejemplo:

El usuario introduce 2 y 5.

El programa debe imprimir:"""


numero_a = int(input("Introduce un número entero: "))
numero_b = int(input("introduce un numero entero mayor que el número anterior: "))

for i in range(numero_a,numero_b+1):
    print(i)

"""Ejercicio 12¶
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. Si el 
primer número es mayor que el segundo, imprime la secuencia en orden descendente. Debes imprimir la secuencia de números en una sola línea, 
separados por espacios.

Ejemplo:

El usuario introduce 5 y 2.

El programa debe imprimir:"""

numero_c = int(input("Introduce un número entero.: "))
numero_d = int(input("Introduce otro número entero: "))


if numero_c < numero_d:
    for i in range (numero_c,numero_d+1):
        print(i, end=" ")
else:
    for i in range (numero_c,numero_d-1,-1):
        print(i, end=" ")


"""Ejercicio 13¶
Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10)."""

numero_e = int(input("Escribe un número entero positivo: "))

for i in range(1,11,1):
    print(f"{i}x{numero_e}={numero_e*i}")

"""Ejercicio 15¶
Escribe un programa que pida al usuario un número entero positivo y calcules la suma de la potencia de 3 de cada número desde 1 hasta el número 
introducido. El programa debe imprimir el resultado.

Para que se entienda mejor, si el usuario introduce 3, el programa debe calcular:"""

numero_f = int(input("Escribe un número entero positivo(ej15): "))
resultado_f= 0
for i in range(1,numero_f+1,1):
    resultado_f += i ** 3
    print(f"La suma de la pontencia de 3 de los numeros desde 1 hasta {numero_f} es: {resultado_f}")


"""Ejercicio 14¶
Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado y la suma de los números impares 
por otro. El programa debe imprimir ambos resultados."""

numero_g = int(input("Escribe un número entero positivo: "))
resultado_g1= 0
resultado_g2 =0
for i in range(1,numero_g+1,1):
    if i%2 == 0:
        resultado_g2 = resultado_g2 + i
    else:
        resultado_g1 = resultado_g1 + i

print(f"La suma de números impares es: {resultado_g1}")
print(f"Y la suma de números pares es: {resultado_g2}")

"""Ejercicio 16¶
Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores de ese número. Un divisor de un número n es un número 
entero que divide a n sin dejar residuo. El programa debe imprimir todos los divisores del número introducido."""

numero_h = int(input("Escribe un número entero positivo (Ej:16): "))

print(f"Los divisores de {numero_h} son: ", end=" ")
for i in range(1, numero_h+1,1):
    if numero_h % i == 0:
        print(i, end=", ")
print()

"""Ejercicio 17¶
Escribe un programa que reciba un número entero positivo y una letra. El programa debe imprimir la letra tantas veces 
como el número introducido."""

numero_j = int(input("Escribe un número positivo (Ej:17): "))
letra = str(input("Escribe una letra: "))

for i in range (1, numero_j+1,1):
    print(letra, end=", ")

"""Ejercicio 18¶
Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, imprima el 
número introducido sumándole 1. El programa debe imprimir todos los números introducidos, menos el -1, sumándoles 1."""

numero = int(input("\n Ejer18. Introduce un número entero (-1 para salir): "))

while numero != -1:
    numero_nuevo = numero+1
    print(f"El número {numero} sumándole uno da como resultado {numero_nuevo}")
    numero = int(input("Introduce un nuevo número pon -1 para salir"))

"""Ejercicio 19¶
Escribe un programa que dado una serie de notas introducidas por el usuario, hasta que introduzca un -1, imprima el número 
de notas correctas introducidas, la media de las notas y cuantas de estas notas son 10. El programa debe imprimir la 
media de todas las notas introducidas, menos el -1."""

nota = int(input("\n Escribe una nota válida entre 0 y 10 (-1 para salir): "))

total_notas = 0
suma_notas = 0
sobresalientes = 0

while nota != -1:
    if 0 <= nota <= 10:
        total_notas += 1
        suma_notas = suma_notas + nota
        if nota == 10:
            sobresalientes += 1
    else:
        print("Nota inválida. Debe estar entre 0 y 10.")

    nota = int(input("Escribe otra nota (-1 para salir): "))

if total_notas > 0:
    media = suma_notas / total_notas
    print(f"\nHas introducido {total_notas} notas válidas.")
    print(f"La nota media es {media:.2f}.")
    print(f"Has sacado un 10 en {sobresalientes} ocasión(es).")
else:
    print("No se han introducido notas válidas.")
