"""Ejercicio 11¶
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente.
El primer número siempre será menor que el segundo.

Ejemplo:

El usuario introduce 2 y 5.

El programa debe imprimir:"""
from weakref import finalize

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

"""Ejercicio 20¶
Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, cuente 
cuántos de estos números son pares y cuántos son impares. El programa debe imprimir el número de pares e impares introducidos, menos el -1."""
pares = 0
impares = 0

while True:
    numeros = int(input("\n Escribe números enteros (-1 para salir): "))
    if numeros == -1:
        break
    if numeros % 2 == 0:
        pares = pares +1
    else:
        impares = impares + 1
print(f"Hay {pares} números pares.")
print(f"Hay {impares} números impares.")

"""Ejercicio 21¶
Escribe un programa que te introduzca un número entero positivo que corresponde al número de casos a tratar. 
Seguidamente te introducen un número entero positivo que corresponde a una serie de números. Después debes recibir ese 
total de números e imprimirlos en la misma linea de la terminal, separados por un espacio y habiéndoles sumado 1 a cada 
uno de ellos."""

numero_casos = int(input("Introduce el número de casos a tratar: "))
for _ in range(numero_casos):
    numeros = int(input("Números a introducir: "))
    for _ in range(numeros):
        numero = int(input())
        print(int(numero) + 1, end=" ")
    print()

"""Ejercicio 22¶
Escribe un programa que inicialmente te indique el número de casos a tratar. Después, para cada caso, te introduzca un 
número entero positivo del qual debes imprimir todos los divisores. Un divisor de un número n es un número entero que 
divide a n sin dejar residuo. El programa debe imprimir todos los divisores del número introducido en una sola línea, 
separados por espacios."""

casos = int(input("Introduce el número de casos: "))
for _ in range(casos):
    numero = int(input("Introduce un número entero positivo: "))
    print(f"Los divisores de {numero} son: ", end=" ")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=" ")
    print()

    """Ejercicio 23¶
Escribe un programa que vaya recibiendo cadenas de texto hasta que el usuario introduzca "fin". El programa debe contar 
cuántas vocales se han introducido e imprimir el resultado. Las vocales son: a, e, i, o, u (tanto mayúsculas como 
minúsculas). El programa debe imprimir el número total de vocales introducidas sin contar la palabra "fin"."""

"""Jordi"""
contador_vocales = 0

while True:
    cadena = input("Introduce una cadena de texto (o 'fin' para salir): ")
    if cadena.lower() == "fin":
        break
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador_vocales += 1

print(f"Número total de vocales: {contador_vocales}")

letra_a = 0
letra_e = 0
letra_i = 0
letra_o = 0
letra_u = 0
while True:
    letras = (input("\nIntroduce texto (pon fin para finalizar)"))
    if letras.lower() == "fin":
        break
    for letra_a in letras:
        if letra_a.lower() in "a":
            letra_a = letra_a + 1
    for letra_e in letras:
        if letra_e.lower() in "e":
            letra_e = letra_e +1
    for letra_i in letras:
        if letra_i.lower() in "i":
            letra_i = letra_i +1
    for letra_o in letras:
        if letra_o.lower() in "o":
            letra_o =  letra_o +1
    for letra_u in letras:
        if letra_u.lower() in "u":
            letra_u = letra_u +1

vocales_total = letra_a + letra_e + letra_i + letra_o + letra_u

print(f"El número de a es: {letra_a}, el número de e es: {letra_e}, el número de i es: {letra_i}, el número de o es: {letra_o}"
      f", el número de u es: {letra_u}. Y el total de vocales introducidas es: {vocales_total}.")