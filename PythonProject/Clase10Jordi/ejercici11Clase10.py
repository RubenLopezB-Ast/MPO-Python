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

"""Ejercicio 14¶
Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado y 
la suma de los números impares por otro. El programa debe imprimir ambos resultados."""

numero_f = int(input("Escribe un número entero positivo(ej14): "))
resultado_f= 0
for i in range(1,numero_f+1,1):
    resultado_f += i ** 3
    print(f"La suma de la pontencia de 3 de los numeros desde 1 hasta {numero_f} es: {resultado_f}")