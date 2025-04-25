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
Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura especificada. Por ejemplo, si el 
usuario ingresa 5, el triángulo debe verse así:"""

altura = int(input("Introduce un número entero positivo que será la altura del usuario: \n"))

for l in range (0, altura+1,1):
    print("*"*l)





